from pydantic import BaseModel
from typing import List, Literal
from datetime import datetime
from .shared import Location

# Input: MedicalAssessment

# Fetch Hospitals Task
class HospitalLoc(BaseModel):
    hospital_id: str
    location: Location
    available_beds: int
    available_ambulances: int
    available_paramedics: int

class HospitalsInformation(BaseModel):
    ranked_hospitals: List[HospitalLoc]
    timestamp: datetime

# Rank Hospitals Task
class HospitalDist(BaseModel):
    hospital_id: str
    distance_to_emergency: float
    available_beds: int
    available_ambulances: int
    available_paramedics: int


class RankedHospitals(BaseModel):
    ranked_hospitals: List[HospitalDist]
    timestamp: datetime


# Allocate Hospital Resources Task
class HospitalResources(BaseModel):
    hospital_id: str
    distance_to_emergency: float
    beds_reserved: int
    ambulances_dispatched: int
    paramedics_deployed: int


class AllocatedHospitalResources(BaseModel):
    hospital_resource_allocation: List[HospitalResources]
    timestamp: datetime


# Deploy Paramedics Task
class MedicalEquipment(BaseModel):
    equipment_name: Literal[
        "oxygen_mask",
        "stretcher",
        "defibrillator",
        "IV_drip",
        "other",
    ]
    use_case: str


class DeployedParamedics(BaseModel):
    total_paramedics_deployed: int
    total_ambulances_dispatched: int
    estimated_arrival_times: List[datetime]
    equipment: List[MedicalEquipment]


# Medical Response Report
class MedicalResponseReport(BaseModel):
    summary: str
    timestamp: datetime
