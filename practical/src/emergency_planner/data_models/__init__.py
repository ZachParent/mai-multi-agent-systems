from pydantic import BaseModel
from typing import Optional
from .emergency_services import *
from .firefighters import *
from .medical_services import *
from .public_communication import *


class EmergencyPlannerState(BaseModel):
    call_transcript: Optional[str]
    call_assessment: Optional[CallAssessment]
    firefighters_response_report: Optional[FirefightersResponseReport]
    medical_response_report: Optional[MedicalResponseReport]
    public_communication_report: Optional[PublicCommunicationReport]
    mayor_approval_retry_count: int = 0

# Example data for each component of the EmergencyPlannerState
CALL_ASSESSMENT_DEMO = CallAssessment(
    fire_type="electrical",
    location=(41.71947, 2.84031),
    injured_details=["minor", "severe"],
    fire_severity="high",
    hazards=["gas cylinders", "flammable chemicals"],
    indoor=True,
    trapped_people=5,
    firefighters_required=True,
    medical_services_required=True
)

FIREFIGHTERS_RESPONSE_REPORT_DEMO = FirefightersResponseReport(
    summary="The firefighting response involved deploying 10 fire combatants to address an electrical high-severity fire at an indoor location. The estimated arrival time was 2023-09-22T14:30:00Z. Primary attack and ventilation activities were assigned with high and medium priority, respectively. There were 5 trapped people and hazards included gas cylinders and flammable chemicals.",
    timestamp=datetime(2023, 9, 22, 15, 45, 0)
)

MEDICAL_RESPONSE_REPORT_DEMO = MedicalResponseReport(
    summary="The medical response plan is in place with Hospital1 and Hospital2 allocated for resource support. Paramedics are deployed to the emergency location with estimated arrival times of 2023-02-20T14:45:00Z and 2023-02-20T15:00:00Z, respectively. The equipment list includes oxygen masks, stretchers, defibrillators, and IV drips for both patients' stabilization and treatment.",
    timestamp=datetime(2023, 2, 20, 14, 30, 0)
)

PUBLIC_COMMUNICATION_REPORT_DEMO = PublicCommunicationReport(
  public_communication_report= "# Emergency Report: Electrical Fire in Barcelona\nThe public is advised that a high-severity electrical fire has been reported at an indoor location at [41.71947, 2.84031]. The fire department has deployed 10 firefighters to address the situation.\n\n## Immediate Safety Information\n*   There are 5 people trapped inside the building.\n*   Hazards present: gas cylinders and flammable chemicals.\n*   Medical services have been requested for injured individuals.\n\n## Fire Department Response\nThe firefighting response involved deploying 10 fire combatants to address an electrical high-severity fire at the indoor location. Primary attack and ventilation activities were assigned with high and medium priority, respectively.\n\n## Related Cases\nSimilar incidents in the past include:\n*   Case ID: 24 - Barcelona (High Severity)\n    *   Firefighting response involved deploying 10 fire combatants to address an electrical high-severity fire at an indoor location.\n*   Case ID: 23 - Barcelona (High Severity)\n    *   Firefighting response involved deploying 10 fire combatants to address an electrical high-severity fire at an indoor location.\n\n## Medical Response Plan\nA medical response plan is in place with Hospital1 and Hospital2 allocated for resource support. Paramedics are deployed to the emergency location with estimated arrival times of 2023-09-22T14:45:00Z and 2023-09-22T15:00:00Z, respectively.\n\n## Integrated Sources\n*   Fire Department Reports\n*   Medical Response Plan Documents\n*   Local News Outlets\n\n## Last Update\nThis report is based on information available up to [timestamp]. Please check for updates.",
  mayor_approved=True,
  mayor_comments="The report appears to be well-researched and includes relevant information for public safety. However, consider adding specific details about the cause of the fire and any preventative measures being taken to avoid similar incidents in the future. Additionally, verify the accuracy of the related cases mentioned.",
  social_media_feedback="Positive feedback from the community."
)

# Constructing the complete EmergencyPlannerState
EMERGENCY_PLANNER_STATE_DEMO = EmergencyPlannerState(
    call_transcript="Emergency call transcript example.",
    call_assessment=CALL_ASSESSMENT_DEMO,
    firefighters_response_report=FIREFIGHTERS_RESPONSE_REPORT_DEMO,
    medical_response_report=MEDICAL_RESPONSE_REPORT_DEMO,
    public_communication_report=PUBLIC_COMMUNICATION_REPORT_DEMO,
    mayor_approval_retry_count=1
)