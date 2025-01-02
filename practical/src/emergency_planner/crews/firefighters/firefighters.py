from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from data_models import FireAssessment

@CrewBase
class FirefighterAgentCrew:
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
    def receive_report(self) -> Task:
        return Task(config=self.tasks_config["receive_report"])

    @task
    def allocate_firefighting_resources(self) -> Task:
        return Task(config=self.tasks_config["allocate_firefighting_resources"])

    @task
    def deploy_fire_combatants(self) -> Task:
        return Task(config=self.tasks_config["deploy_fire_combatants"])

    @task
    def report_firefighting_response(self) -> Task:
        return Task(config=self.tasks_config["report_firefighting_response"])

    @crew
    def crew(self) -> Crew:
        """Creates the Firefighter Agent Crew"""
        return Crew(agents=self.agents, tasks=self.tasks, process=Process.sequential)
