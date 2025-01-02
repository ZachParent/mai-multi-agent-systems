from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew

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
        return Task(config=self.tasks_config["receive_call"])

    @task
    def notify_other_crews(self) -> Task:
        return Task(config=self.tasks_config["notify_other_crews"])

    @crew
    def crew(self) -> Crew:
        """Creates the Emergency Services Crew"""
        return Crew(agents=self.agents, tasks=self.tasks, process=Process.sequential)

