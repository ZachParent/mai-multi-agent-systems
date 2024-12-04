from typing import Tuple
from typing import Literal

# Location is a tuple of floats representing coordinates (x, y)
Location = Tuple[float, float]

FireType = Literal["ordinary", "electrical", "gas", "chemical", "other"]