from pydantic import BaseModel
from typing import List, Literal
from datetime import datetime
from .emergency_services import FireAssessment

# input: FireAssessment


# Allocate Firefighting Resources Task
class FireFightingMaterial(BaseModel):
    material_name: Literal[
        "pickup_truck",
        "ladder_engine",
        "water_tanker",
        "foam_tanker",
        "dry_chemical_tanker",
        "air_tanker",
    ]
    material_quantity: int


class AllocatedFirefightingResources(BaseModel):
    fire_assessment: FireAssessment
    resources: List[FireFightingMaterial]


# Deploy Fire Combatants Task
class FirefightingActivity(BaseModel):
    firefighting_activity: str
    priority: Literal["low", "medium", "high"]


class DeployedFireCombatants(BaseModel):
    fire_assessment: FireAssessment
    firecombatants_deployed: int
    estimated_arrival_time: datetime
    firefighting_activities: List[FirefightingActivity]


# Report Firefighting Response Task
class FirefightersResponseReport(BaseModel):
    summary: str
    timestamp: datetime
