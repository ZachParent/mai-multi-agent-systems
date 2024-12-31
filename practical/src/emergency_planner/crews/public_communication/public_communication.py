from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from tools.incident_retrieval_tool import IncidentAnalysisTool

incident_analysis_tool = IncidentAnalysisTool()

@CrewBase
class PublicCommunicationCrew:
    """Public Communication Crew"""

    @agent
    def communication_operator(self) -> Agent:
        return Agent(config=self.agents_config["communication_operator"])

    @agent
    def archive_keeper(self) -> Agent:
        return Agent(config=self.agents_config["archive_keeper"])

    @agent
    def article_writer(self) -> Agent:
        return Agent(config=self.agents_config["article_writer"])

    @agent
    def mayor(self) -> Agent:
        return Agent(config=self.agents_config["mayor"])

    @agent
    def social_media_commentator(self) -> Agent:
        return Agent(config=self.agents_config["social_media_commentator"])

    @task
    def receive_report(self) -> Task:
        return Task(config=self.tasks_config["receive_report"])

    @task
    def search_related_cases(self) -> Task:
        return Task(config=self.tasks_config["search_related_cases"], tools= [incident_analysis_tool])

    @task
    def draft_initial_article(self) -> Task:
        return Task(config=self.tasks_config["draft_initial_article"])

    @task
    def integrate_additional_information(self) -> Task:
        return Task(config=self.tasks_config["integrate_additional_information"])

    @task
    def review_and_authorize_publication(self) -> Task:
        return Task(config=self.tasks_config["review_and_authorize_publication"])

    @task
    def provide_social_media_feedback(self) -> Task:
        return Task(config=self.tasks_config["provide_social_media_feedback"])

    @crew
    def crew(self) -> Crew:
        """Creates the Public Communication Crew"""
        return Crew(agents=self.agents, tasks=self.tasks, process=Process.sequential)
