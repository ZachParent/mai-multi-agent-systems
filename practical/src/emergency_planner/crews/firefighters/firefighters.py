import json

from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew

from ...data_models.firefighters import AllocatedFirefightingResources, DeployedFireCombatants, FirefightersResponseReport


def add_schema_to_task_config(task_config, schema):
    """
    Add the schema JSON to the expected output of the task configuration.
    """
    task_config = task_config.copy()
    task_config["expected_output"] += f"\n {json.dumps(schema['properties']).replace('{','{{').replace('}','}}')}"
    return task_config


@CrewBase
class FirefightersCrew:
    """Firefighter Agent Crew"""

    @agent
    def fire_chief(self) -> Agent:
        return Agent(config=self.agents_config["fire_chief"])

    @agent
    def equipment_technician(self) -> Agent:
        return Agent(config=self.agents_config["equipment_technician"])

    @agent
    def firefighter(self) -> Agent:
        return Agent(config=self.agents_config["firefighter"])

    @task
    def allocate_firefighting_resources(self) -> Task:
        config = add_schema_to_task_config(
            self.tasks_config["allocate_firefighting_resources"], AllocatedFirefightingResources.model_json_schema()
        )
        return Task(config=config)

    @task
    def deploy_fire_combatants(self) -> Task:
        config = add_schema_to_task_config(
            self.tasks_config["deploy_fire_combatants"], DeployedFireCombatants.model_json_schema()
        )
        return Task(config=config)

    @task
    def report_firefighting_response(self) -> Task:
        config = add_schema_to_task_config(
            self.tasks_config["report_firefighting_response"], FirefightersResponseReport.model_json_schema()
        )
        return Task(config=config)

    @crew
    def crew(self) -> Crew:
        """Creates the Firefighter Agent Crew"""
        return Crew(agents=self.agents, tasks=self.tasks, process=Process.sequential, verbose=True)
