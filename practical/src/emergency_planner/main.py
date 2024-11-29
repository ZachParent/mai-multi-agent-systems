#!/usr/bin/env python
from random import randint

from pydantic import BaseModel

from crewai.flow.flow import Flow, listen, start

from .crews.public_communication.public_communication import PublicCommunicationCrew
from .crews.emergency_services.emergency_services import EmergencyServicesCrew


class PoemState(BaseModel):
    sentence_count: int = 1
    poem: str = ""


class PoemFlow(Flow[PoemState]):

    @start()
    def generate_sentence_count(self):
        print("Generating sentence count")
        self.state.sentence_count = randint(1, 5)
    
    @listen(generate_sentence_count)
    def generate_poem(self):
        print("Generating poem")
        result = "Hello from the generate_poem method"
        self.state.poem = result

    # @listen(generate_sentence_count)
    # def generate_poem(self):
    #     print("Generating poem")
    #     result = (
    #         PublicCommunicationsCrew()
    #         .crew()
    #         .kickoff(inputs={"sentence_count": self.state.sentence_count})
    #     )

    #     print("Poem generated", result.raw)
    #     self.state.poem = result.raw

    @listen(generate_poem)
    def save_poem(self):
        print("Saving poem")
        with open("poem.txt", "w") as f:
            f.write(self.state.poem)


def kickoff():
    poem_flow = PoemFlow()
    poem_flow.kickoff()


def plot():
    poem_flow = PoemFlow()
    poem_flow.plot()


if __name__ == "__main__":
    kickoff()
