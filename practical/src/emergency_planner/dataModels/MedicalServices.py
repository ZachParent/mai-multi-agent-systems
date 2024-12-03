from pydantic import BaseModel
from typing import List, Tuple

# Receive Report Task
class MedicalReport(BaseModel): 
    report_id: str
    location: Tuple[float, float] 
    injured_details: List[str] 
    fire_severity: str
    hazards: List[str]

class ReceiveReportOutput(BaseModel):
    report: MedicalReport
    timestamp: str

# Rank Hospitals Task
class Hospital(BaseModel):
    hospital_id: str
    location: str
    available_beds: int
    available_ambulances: int
    available_paramedics: int

class RankHospitalsOutput(BaseModel):
    report: MedicalReport
    ranked_hospitals: List[Hospital]
    timestamp: str

# Allocate Hospital Resources Task
class HospitalResources(BaseModel):
    hospital_id: str
    beds_reserved: int
    ambulances_dispatched: int
    paramedics_deployed: int

class AllocateHospitalResourcesOutput(BaseModel):
    report: MedicalReport
    hospital_resource_allocation = List[HospitalResources]
    timestamp: str

# Deploy Paramedics Task
class MedicalEquipment(BaseModel):
    equipment_name: str
    use_case: str

class DeployParamedicsOutput(BaseModel):
    report: MedicalReport
    total_paramedics_deployed: int
    total_ambulances_dispatched: int
    estimated_arrival_times: List[str]
    equipment: List[MedicalEquipment]

# Medical Response Report
class MedicalResponseReportOutput(BaseModel):
    summary: str
    timestamp: str