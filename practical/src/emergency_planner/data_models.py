from enum import Enum
from pydantic import BaseModel
from typing import List, Optional, Tuple

class FireStatus(Enum):
    FIRE_STARTED = "Fire Started"
    FIRE_EXTINGUISHED = "Fire Extinguished"

class EmergencyCall(BaseModel):
    location: str
    description: str
    timestamp: str

class FireFighterDispatch(BaseModel):
    location: str
    description: str
    status: FireStatus
    timestamp: str

class EmergencyPlannerState(BaseModel):
    emergency_call: Optional[EmergencyCall]
    fire_fighter_dispatch: Optional[FireFighterDispatch]


# Medical Services

from dataModels.MedicalServices import *

# Public Communication

from dataModels.PublicCommunication import *
