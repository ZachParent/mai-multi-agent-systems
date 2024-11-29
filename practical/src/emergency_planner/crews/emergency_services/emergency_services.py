from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew

@CrewBase
class EmergencyServicesCrew:
    """Emergency Services Crew"""

    @agent
    def communication_operator(self) -> Agent:
        return Agent(config=self.agents_config['communication_operator'])


    @task
    def receive_report(self) -> Task:
        return Task(config=self.tasks_config['receive_report'])


    @crew
    def crew(self) -> Crew:
        """Creates the Public Communication Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential
        )
