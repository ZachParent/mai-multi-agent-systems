from typing import Tuple
from typing import Literal

Location = Tuple[float, float]

FireType = Literal["ordinary", "electrical", "gas", "chemical", "other"]

FireSeverity = Literal["low", "medium", "high"]

InjuryType = Literal["minor", "moderate", "severe"]

HazardType = Literal["gas cylinders", "chemicals"]