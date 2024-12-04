from pydantic import BaseModel
from typing import List
from .shared import Location, FireType, FireSeverity, InjuryType, HazardType

class FireFightingMaterial(BaseModel):
    material_name: str
    material_quantity: int

class AllocateFirefightingResourcesOutput(BaseModel):
    resources: List[FireFightingMaterial]

class FirefightingActivity(BaseModel):
    firefighting_activity: str
    priority_level: str

class DeployFireCombatantsOutput(BaseModel):
    firecombatants_deployed: int
    estimated_arrival_time: str
    firefighting_activities: List[FirefightingActivity]

class ReportFirefightingResponseOutput(BaseModel):
    summary: str
    timestamp: str
    success: bool