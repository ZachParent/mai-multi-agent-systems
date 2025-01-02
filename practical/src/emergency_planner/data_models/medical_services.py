from pydantic import BaseModel
from typing import List, Literal
from datetime import datetime
from .shared import Location
from .emergency_services import MedicalAssessment

# Input: MedicalAssessment


# Rank Hospitals Task
class Hospital(BaseModel):
    hospital_id: str
    location: Location
    available_beds: int
    available_ambulances: int
    available_paramedics: int

    @classmethod
    def get_schema(cls) -> str:
        schema = '\n'
        for field_name, field_instance in cls.__fields__.items():
            schema += f'{field_name}, described as: {field_instance.description}\n'
        return schema


class RankedHospitals(BaseModel):
    medical_assessment: MedicalAssessment
    ranked_hospitals: List[Hospital]
    timestamp: datetime

    @classmethod
    def get_schema(cls) -> str:
        schema = '\n'
        for field_name, field_instance in cls.__fields__.items():
            schema += f'{field_name}, described as: {field_instance.description}\n'
        return schema


# Allocate Hospital Resources Task
class HospitalResources(BaseModel):
    hospital_id: str
    beds_reserved: int
    ambulances_dispatched: int
    paramedics_deployed: int

    @classmethod
    def get_schema(cls) -> str:
        schema = '\n'
        for field_name, field_instance in cls.__fields__.items():
            schema += f'{field_name}, described as: {field_instance.description}\n'
        return schema


class AllocatedHospitalResources(BaseModel):
    medical_assessment: MedicalAssessment
    hospital_resource_allocation: List[HospitalResources]
    timestamp: datetime

    @classmethod
    def get_schema(cls) -> str:
        schema = '\n'
        for field_name, field_instance in cls.__fields__.items():
            schema += f'{field_name}, described as: {field_instance.description}\n'
        return schema


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

    @classmethod
    def get_schema(cls) -> str:
        schema = '\n'
        for field_name, field_instance in cls.__fields__.items():
            schema += f'{field_name}, described as: {field_instance.description}\n'
        return schema


class DeployedParamedics(BaseModel):
    medical_assessment: MedicalAssessment
    total_paramedics_deployed: int
    total_ambulances_dispatched: int
    estimated_arrival_times: List[datetime]
    equipment: List[MedicalEquipment]

    @classmethod
    def get_schema(cls) -> str:
        schema = '\n'
        for field_name, field_instance in cls.__fields__.items():
            schema += f'{field_name}, described as: {field_instance.description}\n'
        return schema


# Medical Response Report
class MedicalResponseReport(BaseModel):
    summary: str
    timestamp: datetime

    @classmethod
    def get_schema(cls) -> str:
        schema = '\n'
        for field_name, field_instance in cls.__fields__.items():
            schema += f'{field_name}, described as: {field_instance.description}\n'
        return schema
