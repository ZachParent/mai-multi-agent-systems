from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew

@CrewBase
class FireFightersCrew:
    """Fire Fighters Crew"""

    @agent
    def fire_fighter(self) -> Agent:
        return Agent(config=self.agents_config['fire_fighter'])


    @task
    def receive_call(self) -> Task:
        return Task(config=self.tasks_config['receive_call'])
    
    @task
    def plan_route(self) -> Task:
        return Task(config=self.tasks_config['plan_route'])

    @crew
    def crew(self) -> Crew:
        """Creates the Public Communication Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential
        )
