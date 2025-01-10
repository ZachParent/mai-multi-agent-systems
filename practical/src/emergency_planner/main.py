import logging
import json
from crewai.flow.flow import Flow, listen, start, router, and_, or_
from pathlib import Path
from .crews.emergency_services.emergency_services import EmergencyServicesCrew
from .crews.firefighters.firefighters import FirefightersCrew
from .crews.medical_services.medical_services import MedicalServicesCrew
from .crews.public_communication.public_communication import PublicCommunicationCrew
from .data_models import (
    CallAssessment,
    EmergencyPlannerState,
    FireAssessment,
    FirefightersResponseReport,
    MedicalAssessment,
    MedicalResponseReport,
    PublicCommunicationReport,
    EmergencyReport,
    EMERGENCY_PLANNER_STATE_DEMO
)

logger = logging.getLogger(__name__)

EMERGENCY_CALL_TRANSCRIPTS_FILENAME = Path(__file__).parent.parent.parent / "data" / "inputs" / "call_transcripts.txt"
EMERGENCY_REPORT_FILENAME = Path(__file__).parent.parent.parent / "data" / "outputs" / "emergency_report.md"
TRANSCRIPT_COUNT = 2
MAX_MAYOR_APPROVAL_RETRY_COUNT = 3

TRANSCRIPT_INDEX = 0
INIT_POPULATED_STATE = False

class EmergencyPlannerFlow(Flow[EmergencyPlannerState]):
    def _create_initial_state(self) -> EmergencyPlannerState:
        if INIT_POPULATED_STATE:
            return EMERGENCY_PLANNER_STATE_DEMO
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
        with open(EMERGENCY_CALL_TRANSCRIPTS_FILENAME, "r") as f:
            self.state.call_transcript = f.readlines()[TRANSCRIPT_INDEX]
        logger.info("Call transcript received", self.state.call_transcript)

    @listen(get_call_transcript)
    def emergency_services(self):
        logger.info("Receiving call")
        result = (
            EmergencyServicesCrew()
            .crew()
            .kickoff(inputs={"transcript": self.state.call_transcript})
        )
        self.state.call_assessment = CallAssessment.model_validate_json(result.raw)
        logger.info("Emergency call received", result.raw)


    @listen(emergency_services)
    def firefighters(self):
        logger.info("Dispatching fire fighters")
        fire_assessment = FireAssessment.model_validate(self.state.call_assessment.model_dump())
        result = (
            FirefightersCrew()
            .crew()
            .kickoff(inputs={"fire_assessment": fire_assessment.model_dump_json()})
        )
        self.state.firefighters_response_report = FirefightersResponseReport.model_validate_json(result.raw)
        logger.info("Fire fighters dispatched", result.raw)

    @listen(emergency_services)
    def medical_services(self):
        if not self.state.call_assessment.medical_services_required:
            logger.info("Medical services not required")
            return
        logger.info("Dispatching medical services")
        medical_assessment = MedicalAssessment.model_validate({**self.state.call_assessment.model_dump(), "injured_count": len(self.state.call_assessment.injured_details)})
        result = (
            MedicalServicesCrew()
            .crew()
            .kickoff(inputs={"medical_assessment": medical_assessment.model_dump_json()})
        )
        self.state.medical_response_report = MedicalResponseReport.model_validate_json(result.raw)
        logger.info("Medical services dispatched", result.raw)

    @listen(or_(and_(firefighters, medical_services), "retry_public_communication"))
    def public_communication(self):
        logger.info("Handling public communication")
        emergency_report = EmergencyReport(
            call_assessment=self.state.call_assessment,
            firefighters_response_report=self.state.firefighters_response_report,
            medical_response_report=self.state.medical_response_report,
            timestamp=self.state.firefighters_response_report.timestamp,
            fire_type=self.state.call_assessment.fire_type,
            fire_severity=self.state.call_assessment.fire_severity,
            location_x=self.state.call_assessment.location[0],
            location_y=self.state.call_assessment.location[1]
        )
        result = (
            PublicCommunicationCrew()
            .crew()
            .kickoff(inputs={"emergency_report": emergency_report.model_dump_json()})
        )
        self.state.public_communication_report = PublicCommunicationReport.model_validate_json(result.raw)
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
{self.state.public_communication_report.public_communication_report}

### Approved by Mayor
{self.state.public_communication_report.mayor_approved}

### Mayor's Comments
{self.state.public_communication_report.mayor_comments}

### Social Media Feedback
{self.state.public_communication_report.social_media_feedback}
"""
        with open(EMERGENCY_REPORT_FILENAME, "w") as f:
            f.write(full_emergency_report)
        logger.info("Emergency report saved")


def kickoff():
    emergency_planner_flow = EmergencyPlannerFlow()
    emergency_planner_flow.kickoff()


def plot():
    emergency_planner_flow = EmergencyPlannerFlow()
    emergency_planner_flow.plot()


if __name__ == "__main__":
    kickoff()
