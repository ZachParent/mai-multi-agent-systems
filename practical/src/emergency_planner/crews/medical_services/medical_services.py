from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from ...data_models import FireFighterDispatch


@CrewBase
class MedicalServicesCrew:
    """Medical Services Crew"""

    @agent
    def fire_fighter(self) -> Agent:
        return Agent(config=self.agents_config["fire_fighter"])

    @task
    def receive_dispatch(self, input_pydantic: FireFighterDispatch) -> Task:
        return Task(config=self.tasks_config["receive_dispatch"])

    @task
    def plan_route(self, input_pydantic: FireFighterDispatch) -> Task:
        return Task(config=self.tasks_config["plan_route"])

    @crew
    def crew(self) -> Crew:
        """Creates the Public Communication Crew"""
        return Crew(agents=self.agents, tasks=self.tasks, process=Process.sequential)
