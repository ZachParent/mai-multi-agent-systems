from typing import Tuple
from typing import Literal
import json

Location = Tuple[float, float]

FireType = Literal["ordinary", "electrical", "gas", "chemical", "other"]

FireSeverity = Literal["low", "medium", "high"]

InjuryType = Literal["minor", "moderate", "severe"]

HazardType = Literal["gas cylinders", "chemicals", "flammable chemicals"]


def add_schema_to_task_config(task_config, schema):
    """
    Add the schema JSON to the expected output of the task configuration.
    """
    task_config = task_config.copy()
    task_config[
        "expected_output"
    ] += f"\n {json.dumps(schema).replace('{','{{').replace('}','}}')}"
    return task_config
