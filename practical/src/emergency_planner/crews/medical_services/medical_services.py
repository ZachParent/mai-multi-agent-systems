from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from data_models import RankedHospitals, AllocatedHospitalResources, DeployedParamedics, MedicalResponseReport
from data_models.shared import add_schema_to_task_config
from tools.distance_tool import RouteDistanceTool
from tools.incident_retrieval_tool import IncidentAnalysisTool

route_distance_tool = RouteDistanceTool()
#incident_analysis_tool = IncidentAnalysisTool("incidents.db")

@CrewBase
class MedicalServicesCrew:
    """Medical Services Crew"""

    @agent
    def medical_services_operator(self) -> Agent:
        return Agent(config=self.agents_config["medical_services_operator"])

    @agent
    def hospital_coordinator(self) -> Agent:
        return Agent(config=self.agents_config["hospital_coordinator"])

    @agent
    def paramedics(self) -> Agent:
        return Agent(config=self.agents_config["paramedics"])

    @task
    def rank_hospitals(self) -> Task:
        config = add_schema_to_task_config(
            self.tasks_config["rank_hospitals"], RankedHospitals.model_json_schema()
        )
        return Task(config=config, tools=[route_distance_tool]) #, incident_analysis_tool])

    @task
    def allocate_hospital_resources(self) -> Task:
        config = add_schema_to_task_config(
            self.tasks_config["allocate_hospital_resources"], AllocatedHospitalResources.model_json_schema()
        )
        return Task(config=config)

    @task
    def deploy_paramedics(self) -> Task:
        config = add_schema_to_task_config(
            self.tasks_config["deploy_paramedics"], DeployedParamedics.model_json_schema()
        )
        return Task(config=config)

    @task
    def report_medical_response(self) -> Task:
        config = add_schema_to_task_config(
            self.tasks_config["report_medical_response"], MedicalResponseReport.model_json_schema()
        )
        return Task(config=config)

    @crew
    def crew(self) -> Crew:
        """Creates the Medical Services Crew"""
        return Crew(agents=self.agents, tasks=self.tasks, process=Process.sequential)
