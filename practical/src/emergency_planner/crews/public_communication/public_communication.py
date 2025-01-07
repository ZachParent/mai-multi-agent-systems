import json
import os
from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from dotenv import load_dotenv
from data_models.public_communication import DraftArticle, EmergencyReport, IntegratedArticle, PublicCommunicationReport, RelatedCases, ReviewedArticle
from tools.incident_retrieval_tool import IncidentAnalysisTool

# Load environment variables
load_dotenv(os.path.join("practical", "src", ".env"))

# Get DB path and file from environment variables
raw_db_path = os.getenv("DB_PATH")
db_file = os.getenv("DB_FILE")

# Ensure cross-platform compatibility by normalizing paths
normalized_path = os.path.normpath(raw_db_path)
db_path = os.path.join(normalized_path, db_file)

incident_analysis_tool = IncidentAnalysisTool(db_path, result_as_answer=True)

def add_schema_to_task_config(task_config, schema):
    """
    Add the schema JSON to the expected output of the task configuration.
    """
    task_config = task_config.copy()
    task_config["expected_output"] += f"\n {json.dumps(schema['properties']).replace('{','{{').replace('}','}}')}"
    return task_config

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
    
    # @task
    # def receive_report(self) -> Task:
    #     config = add_schema_to_task_config(
    #         self.tasks_config["receive_report"], EmergencyReport.model_json_schema()
    #     )
    #     return Task(config=config, output_pydantic=EmergencyReport)

    @task
    def search_related_cases(self) -> Task:
        config = add_schema_to_task_config(
            self.tasks_config["search_related_cases"], RelatedCases.model_json_schema()
        )
        return Task(config=config, tools=[incident_analysis_tool])# output_pydantic=RelatedCases)

    @task
    def draft_initial_article(self) -> Task:
        config = add_schema_to_task_config(
            self.tasks_config["draft_initial_article"], DraftArticle.model_json_schema()
        )
        return Task(config=config)

    @task
    def integrate_additional_information(self) -> Task:
        config = add_schema_to_task_config(
            self.tasks_config["integrate_additional_information"], IntegratedArticle.model_json_schema()
        )
        return Task(config=config)

    @task
    def review_and_authorize_publication(self) -> Task:
        config = add_schema_to_task_config(
            self.tasks_config["review_and_authorize_publication"], ReviewedArticle.model_json_schema()
        )
        return Task(config=config)

    @task
    def provide_social_media_feedback(self) -> Task:
        return Task(config=self.tasks_config["provide_social_media_feedback"])
    
    @task
    def publish_final_communication(self) -> Task:
        config = add_schema_to_task_config(
            self.tasks_config["publish_final_communication"], PublicCommunicationReport.model_json_schema()
        )
        return Task(config=config)

    @crew
    def crew(self) -> Crew:
        """Creates the Public Communication Crew"""
        return Crew(agents=self.agents, tasks=self.tasks, process=Process.sequential,verbose=True)
