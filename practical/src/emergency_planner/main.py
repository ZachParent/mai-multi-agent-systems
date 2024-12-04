import logging
from crewai.flow.flow import Flow, listen, start, and_

from .crews.emergency_services.emergency_services import EmergencyServicesCrew
from .crews.firefighters.firefighters import FirefightersCrew
from .crews.medical_services.medical_services import MedicalServicesCrew
from .crews.public_communication.public_communication import PublicCommunicationCrew
from .data_models import EmergencyPlannerState, FireAssessment, MedicalAssessment, EmergencyReport

logger = logging.getLogger(__name__)


EMERGENCY_CALL = "There's been a fire at 123 Main St, 12345. I think there are people trapped."

class EmergencyPlannerFlow(Flow[EmergencyPlannerState]):
    def _create_initial_state(self) -> EmergencyPlannerState:
        return EmergencyPlannerState(call_assessment=None, firefighters_response_report=None, medical_response_report=None)

    @start()
    def receive_emergency_call(self):
        logger.info("Receiving call")
        result = (
            EmergencyServicesCrew()
            .crew()
            .kickoff(inputs={"transcript": EMERGENCY_CALL})
        )
        self.state.call_assessment = result.raw
        logger.info("Emergency call received", result.raw)

    @listen(receive_emergency_call)
    def dispatch_fire_fighters(self):
        logger.info("Dispatching fire fighters")
        fire_assessment = FireAssessment(
            **self.state.call_assessment.model_dump()
        )
        result = (
            FirefightersCrew()
            .crew()
            .kickoff(inputs={"fire_assessment": fire_assessment})
        )
        self.state.firefighters_response_report = result.raw
        logger.info("Fire fighters dispatched", result.raw)

    @listen(receive_emergency_call)
    def dispatch_medical_services(self):
        logger.info("Dispatching medical services")
        medical_assessment = MedicalAssessment(
            **self.state.call_assessment.model_dump()
        )
        result = (
            MedicalServicesCrew()
            .crew()
            .kickoff(inputs={"medical_assessment": medical_assessment})
        )
        self.state.medical_response_report = result.raw
        logger.info("Medical services dispatched", result.raw)

    @listen(and_(receive_emergency_call, dispatch_fire_fighters, dispatch_medical_services))
    def handle_public_communication(self):
        logger.info("Handling public communication")
        emergency_report = EmergencyReport(
            call_assessment=self.state.call_assessment,
            firefighters_response_report=self.state.firefighters_response_report,
            medical_response_report=self.state.medical_response_report
        )
        result = (
            PublicCommunicationCrew()
            .crew()
            .kickoff(inputs={"emergency_report": emergency_report})
        )
        # TODO: store the public communication report
        logger.info("Public communication handled", result.raw)
    
    @listen(handle_public_communication)
    def save_full_emergency_report(self):
        logger.info("Saving full emergency report")
        full_emergency_report = f"""
        # Emergency Report

        ## Call Transcript
        {EMERGENCY_CALL}

        ## Firefighters Response
        *{self.state.firefighters_response_report.timestamp}*
        {self.state.firefighters_response_report.summary}

        ## Medical Response
        *{self.state.medical_response_report.timestamp}*
        {self.state.medical_response_report.summary}

        ## Public Communication Report
        *TODO*
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
