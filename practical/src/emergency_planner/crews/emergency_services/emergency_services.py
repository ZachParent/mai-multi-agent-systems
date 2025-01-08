from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from ...data_models.emergency_services import EmergencyCall, EmergencyDetails, CallAssessment
from ...data_models.shared import add_schema_to_task_config

@CrewBase
class EmergencyServicesCrew:
    """Emergency Services Crew"""

    @agent
    def emergency_call_agent(self) -> Agent:
        return Agent(config=self.agents_config["emergency_call_agent"])

    @agent
    def notification_agent(self) -> Agent:
        return Agent(config=self.agents_config["notification_agent"])

    @task
    def receive_call(self) -> Task:
        config = add_schema_to_task_config(
            self.tasks_config["receive_call"], EmergencyDetails.model_json_schema()
        )
        return Task(config=config)

    @task
    def notify_other_crews(self) -> Task:
        config = add_schema_to_task_config(
            self.tasks_config["notify_other_crews"], CallAssessment.model_json_schema()
        )
        return Task(config=config)

    @crew
    def crew(self) -> Crew:
        """Creates the Emergency Services Crew"""
        return Crew(agents=self.agents, tasks=self.tasks, process=Process.sequential)

