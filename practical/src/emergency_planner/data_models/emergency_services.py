from pydantic import BaseModel
from typing import List
from .shared import Location, FireType, FireSeverity, InjuryType, HazardType

# Receive and Assess Call Task Input
class EmergencyCall(BaseModel):
    transcript: str

# Receive and Assess Call Task Output
class EmergencyDetails(BaseModel):
    fire_type: FireType  # Type of fire (e.g., ordinary, electrical, gas, etc.)
    location: Location  # Coordinates (x, y)
    injured_details: List[InjuryType]  # List of risk levels of injured people
    fire_severity: FireSeverity  # Severity of fire: low, medium, or high
    hazards: List[HazardType]  # Hazards present, e.g., gas cylinders, chemicals
    indoor: bool  # True if fire is indoor, False otherwise
    trapped_people: int  # Number of people trapped (0 if none)


# Notify Other Crews Task Output
class CallAssessment(BaseModel):
    fire_type: FireType
    location: Location
    injured_details: List[InjuryType]
    fire_severity: FireSeverity
    hazards: List[HazardType]
    indoor: bool
    trapped_people: int
    firefighters_required: bool  # True if firefighters are required, False otherwise
    medical_services_required: bool  # True if medical services are required, False otherwise


class FireAssessment(BaseModel):
    fire_type: FireType
    location: Location
    fire_severity: FireSeverity
    hazards: List[HazardType]
    indoor: bool
    trapped_people: int


class MedicalAssessment(BaseModel):
    location: Location
    injured_details: List[InjuryType]
    fire_severity: FireSeverity
    hazards: List[HazardType]
