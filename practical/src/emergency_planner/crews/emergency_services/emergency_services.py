from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from ...data_models import EmergencyCall


@CrewBase
class EmergencyServicesCrew:
    """Emergency Services Crew"""

    @agent
    def communication_operator(self) -> Agent:
        return Agent(config=self.agents_config["communication_operator"])

    @task
    def receive_call(self, output_pydantic: EmergencyCall) -> Task:
        return Task(config=self.tasks_config["receive_call"])

    @task
    def dispatch_fire_fighters(self, input_pydantic: EmergencyCall) -> Task:
        return Task(config=self.tasks_config["dispatch_fire_fighters"])

    @crew
    def crew(self) -> Crew:
        """Creates the Public Communication Crew"""
        return Crew(agents=self.agents, tasks=self.tasks, process=Process.sequential)
