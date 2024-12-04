from .emergency_services import *
from .firefighters import *
from .medical_services import *
from .public_communication import *

class EmergencyPlannerState(BaseModel):
    call_assessment: CallAssessment
    firefighters_response_report: FirefightersResponseReport
    medical_response_report: MedicalResponseReport
    # TODO: public_communication_report: PublicCommunicationReport
