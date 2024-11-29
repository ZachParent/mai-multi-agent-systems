
from crew import PublicCommunicationCrew

def run():
    """Run the Public Communication Crew"""
    crew_instance = PublicCommunicationCrew().crew()
    result = crew_instance.kickoff()
    print(result.output)

if __name__ == "__main__":
    run()
