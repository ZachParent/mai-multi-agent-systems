from pydantic import BaseModel
from typing import List
from datetime import datetime
from .shared import Location

# Receive Report Task
class MedicalEmergencyReport(BaseModel):
    report_id: str
    location: Location
    injured_details: List[str] 
    fire_severity: str
    hazards: List[str]
    timestamp: datetime

# Rank Hospitals Task
class Hospital(BaseModel):
    hospital_id: str
    location: str
    available_beds: int
    available_ambulances: int
    available_paramedics: int

class RankedHospitals(BaseModel):
    report: MedicalEmergencyReport
    ranked_hospitals: List[Hospital]
    timestamp: datetime

# Allocate Hospital Resources Task
class HospitalResources(BaseModel):
    hospital_id: str
    beds_reserved: int
    ambulances_dispatched: int
    paramedics_deployed: int

class AllocatedHospitalResources(BaseModel):
    report: MedicalEmergencyReport
    hospital_resource_allocation = List[HospitalResources]
    timestamp: datetime

# Deploy Paramedics Task
class MedicalEquipment(BaseModel):
    equipment_name: str
    use_case: str

class DeployedParamedics(BaseModel):
    report: MedicalEmergencyReport
    total_paramedics_deployed: int
    total_ambulances_dispatched: int
    estimated_arrival_times: List[datetime]
    equipment: List[MedicalEquipment]

# Medical Response Report
class MedicalResponseReport(BaseModel):
    summary: str
    timestamp: datetime
