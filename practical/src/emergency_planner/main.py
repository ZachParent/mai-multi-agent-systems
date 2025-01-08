import logging
import json
from crewai.flow.flow import Flow, listen, start, router, and_, or_

from .crews.emergency_services.emergency_services import EmergencyServicesCrew
from .crews.firefighters.firefighters import FirefightersCrew
from .crews.medical_services.medical_services import MedicalServicesCrew
from .crews.public_communication.public_communication import PublicCommunicationCrew
from .data_models import (
    EmergencyPlannerState,
    FireAssessment,
    MedicalAssessment,
    EmergencyReport,
)

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

EMERGENCY_CALL = (
    "A fire of electrical origin has broken out at coordinates (x: 41.71947, y: 2.84031). The fire is classified as high severity, posing significant danger to the area. Hazards present include gas cylinders and flammable chemicals, further escalating the risk. The fire is indoors, and there are 5 people currently trapped. Additionally, there are 2 injured individuals with minor and severe injuries respectively requiring immediate attention."
)
MAX_MAYOR_APPROVAL_RETRY_COUNT = 3


class EmergencyPlannerFlow(Flow[EmergencyPlannerState]):
    def _create_initial_state(self) -> EmergencyPlannerState:
        return EmergencyPlannerState(
            call_transcript=None,
            call_assessment=None,
            firefighters_response_report=None,
            medical_response_report=None,
            public_communication_report=None,
        )

    @start()
    def get_call_transcript(self):
        logger.info("Getting call transcript")
        self.state.call_transcript = EMERGENCY_CALL
        logger.info("Call transcript received", self.state.call_transcript)

        # Read public input
        # publicannouncements.kickoff()

    @listen(get_call_transcript)
    def emergency_services(self):
        logger.info("Receiving call")
        result = (
            EmergencyServicesCrew()
            .crew()
            .kickoff(inputs={"transcript": EMERGENCY_CALL})
        )
        self.state.call_assessment = json.loads(result.raw)
        logger.info("Emergency call received", result.raw)

    @listen(emergency_services)
    def firefighters(self):
        logger.info("Dispatching fire fighters")
        fire_assessment = FireAssessment(**self.state.call_assessment)
        result = (
            FirefightersCrew()
            .crew()
            .kickoff(inputs={"fire_assessment": fire_assessment})
        )
        self.state.firefighters_response_report = json.loads(result.raw)
        logger.info("Fire fighters dispatched", result.raw)

    @listen(emergency_services)
    def medical_services(self):
        if not self.state.call_assessment['medical_services_required']:
            logger.info("Medical services not required")
            return
        logger.info("Dispatching medical services")
        self.state.call_assessment['injured_count'] = len(self.state.call_assessment['injured_details'])
        medical_assessment = MedicalAssessment(**self.state.call_assessment)
        result = (
            MedicalServicesCrew()
            .crew()
            .kickoff(inputs={"medical_assessment": medical_assessment})
        )
        self.state.medical_response_report = json.loads(result.raw)
        logger.info("Medical services dispatched", result.raw)

    @listen(or_(and_(firefighters, medical_services), "retry_public_communication"))
    def public_communication(self):
        logger.info("Handling public communication")
        emergency_report = EmergencyReport(
            call_assessment=self.state.call_assessment,
            firefighters_response_report=self.state.firefighters_response_report,
            medical_response_report=self.state.medical_response_report,
            timestamp=self.state.firefighters_response_report['timestamp'],
            fire_type=self.state.call_assessment['fire_type'],
            fire_severity=self.state.call_assessment['fire_severity'],
            location_x=self.state.call_assessment['location'][0],
            location_y=self.state.call_assessment['location'][1]
        )
        result = (
            PublicCommunicationCrew()
            .crew()
            .kickoff(inputs={"emergency_report": emergency_report})
        )
        self.state.public_communication_report = json.loads(result.raw)
        logger.info("Public communication handled", result.raw)

    @router(public_communication)
    def check_approval(self):
        logger.info("Checking approval")
        if self.state.public_communication_report.mayor_approved:
            logger.info("Public communication approved by mayor")
            return "save full emergency report"
        elif self.state.mayor_approval_retry_count >= MAX_MAYOR_APPROVAL_RETRY_COUNT:
            logger.info("Public communication not approved by mayor")
            logger.info(
                f"Max retries reached ({self.state.mayor_approval_retry_count} of {MAX_MAYOR_APPROVAL_RETRY_COUNT})"
            )
            return "save full emergency report"
        logger.info("Public communication not approved by mayor")
        self.state.mayor_approval_retry_count += 1
        logger.info(
            f"Retrying public communication ({self.state.mayor_approval_retry_count} of {MAX_MAYOR_APPROVAL_RETRY_COUNT})"
        )
        return "retry_public_communication"

    @listen("save full emergency report")
    def save_full_emergency_report(self):
        logger.info("Saving full emergency report")
        full_emergency_report = f"""
        # Emergency Report

        ## Call Transcript
        {self.state.call_transcript}

        ## Firefighters Response
        *{self.state.firefighters_response_report.timestamp}*
        {self.state.firefighters_response_report.summary}

        ## Medical Response
        *{self.state.medical_response_report.timestamp}*
        {self.state.medical_response_report.summary}

        ## Public Communication Report
        *{self.state.public_communication_report.timestamp}*
        {self.state.public_communication_report.public_communication_report}

        ### Approved by Mayor
        {self.state.public_communication_report.mayor_approved}

        ### Mayor's Comments
        {self.state.public_communication_report.mayor_comments}

        ### Social Media Feedback
        {self.state.public_communication_report.social_media_feedback}

        """
        with open("data/outputs/full_emergency_report.md", "w") as f:
            f.write(full_emergency_report)
        logger.info("Full emergency report saved")


def kickoff():
    emergency_planner_flow = EmergencyPlannerFlow()
    emergency_planner_flow.kickoff()


def plot():
    emergency_planner_flow = EmergencyPlannerFlow()
    emergency_planner_flow.plot()


if __name__ == "__main__":
    kickoff()
