from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from ...data_models import FireAssessment


@CrewBase
class FirefightersCrew:
    """Fire Fighters Crew"""

    @agent
    def firefighter(self) -> Agent:
        return Agent(config=self.agents_config["firefighter"])

    @task
    def receive_dispatch(self, input_pydantic: FireAssessment) -> Task:
        return Task(config=self.tasks_config["receive_dispatch"])

    @crew
    def crew(self) -> Crew:
        """Creates the Public Communication Crew"""
        return Crew(agents=self.agents, tasks=self.tasks, process=Process.sequential)
