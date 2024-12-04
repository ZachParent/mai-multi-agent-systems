from pydantic import BaseModel
from typing import Optional
from .emergency_services import *
from .firefighters import *
from .medical_services import *
from .public_communication import *


class EmergencyPlannerState(BaseModel):
    call_assessment: Optional[CallAssessment]
    firefighters_response_report: Optional[FirefightersResponseReport]
    medical_response_report: Optional[MedicalResponseReport]
    # TODO: public_communication_report: PublicCommunicationReport
