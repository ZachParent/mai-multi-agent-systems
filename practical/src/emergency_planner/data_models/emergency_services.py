from pydantic import BaseModel
from typing import List
from .shared import Location, FireType, FireSeverity, InjuryType, HazardType


class CallAssessment(BaseModel):
    fire_type: FireType  # Type of fire (e.g., ordinary, electrical, gas, etc.)
    location: Location  # Coordinates (x, y)
    injured_details: List[InjuryType]  # List of risk levels of injured people
    fire_severity: FireSeverity  # Severity of fire: low, medium, or high
    hazards: List[HazardType]  # Hazards present, e.g., gas cylinders, chemicals
    indoor: bool  # True if fire is indoor, False otherwise
    trapped_people: int  # Number of people trapped (0 if none)


class FireAssessment(BaseModel):
    report_id: str
    location: Location  # Coordinates (x, y)
    fire_type: FireType  # Type of fire fire_severity
    fire_severity: FireSeverity  # Severity of fire: low, medium, or high
    trapped_people: int  # Number of trapped individuals
    hazards: List[HazardType]  # Hazards present
    hazards_present_indoor: bool  # True if fire is indoor, False otherwise


class MedicalAssessment(BaseModel):
    report_id: str
    location: Location  # Coordinates (x, y)
    injured_details: List[InjuryType]  # Risk levels of injured people
    fire_severity: FireSeverity  # Severity of fire: low, medium, or high
    hazards: List[str]  # Hazards present
