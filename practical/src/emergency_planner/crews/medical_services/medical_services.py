from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from data_models import MedicalAssessment, RankedHospitals, AllocatedHospitalResources, DeployedParamedics, MedicalResponseReport

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
    def receive_report(self) -> Task:
        return Task(config=self.tasks_config["receive_report"], output_pydantic=MedicalAssessment)

    @task
    def rank_hospitals(self) -> Task:
        return Task(config=self.tasks_config["rank_hospitals"], output_pydantic=RankedHospitals)

    @task
    def allocate_hospital_resources(self) -> Task:
        return Task(config=self.tasks_config["allocate_hospital_resources"], output_pydantic=AllocatedHospitalResources)

    @task
    def deploy_paramedics(self) -> Task:
        return Task(config=self.tasks_config["deploy_paramedics"], output_pydantic=DeployedParamedics)

    @task
    def report_medical_response(self) -> Task:
        return Task(config=self.tasks_config["report_medical_response"], output_pydantic=MedicalResponseReport)

    @crew
    def crew(self) -> Crew:
        """Creates the Medical Services Crew"""
        return Crew(agents=self.agents, tasks=self.tasks, process=Process.sequential)
