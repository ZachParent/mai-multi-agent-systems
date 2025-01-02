import json
import logging
import os
from typing import Any, Dict, List

# ------------------------------------------------------------------------
# Import your crews:
from crews.public_communication.public_communication import PublicCommunicationCrew
from crews.emergency_services.emergency_services import EmergencyServicesCrew
from crews.firefighters.firefighters import FirefightersCrew
from crews.medical_services.medical_services import MedicalServicesCrew

# ------------------------------------------------------------------------
# Import the Pydantic data models for type usage & consistency:
from data_models import (
    EmergencyReport,
    PublicCommunicationReport,
    FirefightersResponseReport,
    MedicalResponseReport,
    CallAssessment,
    EmergencyPlannerState,
)

# ------------------------------------------------------------------------
# Setup Logging
# ------------------------------------------------------------------------
LOG_FOLDER = os.path.join(os.path.dirname(__file__), "test", "logs")
os.makedirs(LOG_FOLDER, exist_ok=True)
LOG_FILENAME = os.path.join(LOG_FOLDER, "test.log")

# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create formatters
formatter = logging.Formatter('%(asctime)s %(levelname)s:%(message)s')

# Create handlers:
# 1) File handler (append mode)
file_handler = logging.FileHandler(LOG_FILENAME, mode='a')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

# 2) Console (stream) handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# ------------------------------------------------------------------------
# Where to store results
# ------------------------------------------------------------------------
RESULTS_FOLDER = os.path.join(os.path.dirname(__file__), "test", "results")
os.makedirs(RESULTS_FOLDER, exist_ok=True)

# ------------------------------------------------------------------------
# Loading JSON from "inputs/test_crews.json"
# ------------------------------------------------------------------------
INPUTS_FOLDER = os.path.join(os.path.dirname(__file__), "test", "inputs")
# JSON_FILE = os.path.join(INPUTS_FOLDER, "test_crews.json")
JSON_FILE = os.path.join(INPUTS_FOLDER, "test_ES.json")

def load_test_cases(json_path: str) -> List[Dict[str, Any]]:
    """
    Loads a JSON file containing multiple test cases.
    Expects a top-level 'test_cases' array of objects.
    """
    with open(json_path, 'r') as f:
        data = json.load(f)
    if not isinstance(data, dict) or 'test_cases' not in data:
        raise ValueError("Invalid JSON. Must contain a top-level 'test_cases' list.")
    return data['test_cases']


def instantiate_crew(crew_name: str) -> Any:
    """
    Given a crew name, returns the corresponding crew instance.
    """
    crew_map = {
        # "PublicCommunicationCrew": PublicCommunicationCrew,
        "EmergencyServicesCrew": EmergencyServicesCrew,
        # "FirefightersCrew": FirefightersCrew,
        #"MedicalServicesCrew": MedicalServicesCrew,
    }
    CrewClass = crew_map.get(crew_name)
    if not CrewClass:
        raise ValueError(f"No matching crew found for: {crew_name}")
    return CrewClass()

def process_crew_test(crew_name: str, crew_inputs: Dict[str, Any], test_index: int) -> None:
    """
    Instantiate the chosen crew, pass the inputs, log, and save the result.
    """
    logger.info("[Test #%d] Starting %s with inputs: %s", test_index, crew_name, crew_inputs)

    crew = instantiate_crew(crew_name)
    logger.info("Agents loaded")
    for agent in crew.crew().agents:
        logger.info(f"Role: {agent.role}")

    # Iterate through tasks to log intermediate outputs
    for task in crew.crew().tasks:
        logger.info("[Test #%d] Executing task: %s", test_index, task.description)
        result = task.execute_sync(agent=task.agent, context=task.context, tools=task.tools)
        logger.info("[Test #%d] Task '%s' completed. Intermediate Result: %s", test_index, task.description, result.raw)

    # Final result after all tasks
    final_result = crew.crew().kickoff(inputs=crew_inputs)
    logger.info("[Test #%d] %s finished. Final Result: %s", test_index, crew_name, final_result.raw)

    # Save result in results folder
    output_file = os.path.join(RESULTS_FOLDER, f"{crew_name}_output_{test_index}.txt")
    with open(output_file, 'w') as f:
        f.write(f"=== Results for Test #{test_index} | {crew_name} ===\n")
        f.write(str(final_result.raw))

    logger.info("[Test #%d] Result saved to %s", test_index, output_file)

def main() -> None:
    """Main entry point for running one or multiple crew tests based on JSON input."""
    logger.info("=== Starting Multi-Crew Test ===")
    test_cases = load_test_cases(JSON_FILE)

    for i, test_case in enumerate(test_cases, start=1):
        crew_name = test_case.get('crew_to_test')
        crew_inputs = test_case.get('crew_inputs', {})
        process_crew_test(crew_name, crew_inputs, i)

    logger.info("=== Multi-Crew Test Completed ===")

if __name__ == "__main__":
    main()
