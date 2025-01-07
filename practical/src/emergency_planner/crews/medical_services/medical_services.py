from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from data_models import RankedHospitals, AllocatedHospitalResources, DeployedParamedics, MedicalResponseReport, HospitalsInformation
from data_models.shared import add_schema_to_task_config
from tools.distance_tool import RouteDistanceTool
from tools.hospital_reader_tool import HospitalReaderTool
from tools.hospital_updater_tool import HospitalUpdaterTool

route_distance_tool = RouteDistanceTool()
hospital_reader_tool = HospitalReaderTool()
hospital_updater_tool = HospitalUpdaterTool()

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
    def fetch_hospital_information(self) -> Task:
        config = add_schema_to_task_config(
            self.tasks_config["fetch_hospital_information"], HospitalsInformation.model_json_schema()
        )
        return Task(config=config, tools=[hospital_reader_tool])

    @task
    def rank_hospitals(self) -> Task:
        config = add_schema_to_task_config(
            self.tasks_config["rank_hospitals"], RankedHospitals.model_json_schema()
        )
        return Task(config=config, tools=[route_distance_tool])

    @task
    def plan_hospital_response(self) -> Task:
        config = add_schema_to_task_config(
            self.tasks_config["plan_hospital_response"], AllocatedHospitalResources.model_json_schema()
        )
        return Task(config=config)

    @task
    def allocate_hospital_resources(self) -> Task:
        config = self.tasks_config["allocate_hospital_resources"]
        return Task(config=config, tools=[hospital_updater_tool])

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
