#!/usr/bin/env python
from random import randint

from pydantic import BaseModel

from crewai.flow.flow import Flow, listen, start

from .crews.emergency_services.emergency_services import EmergencyServicesCrew
from .crews.fire_fighters.fire_fighters import FireFightersCrew
from .data_models import EmergencyPlannerState, EmergencyCall

class EmergencyPlannerFlow(Flow[EmergencyPlannerState]):
    def _create_initial_state(self) -> EmergencyPlannerState:
        return EmergencyPlannerState(
            emergency_call=None,
            fire_fighter_dispatch=None
        )

    @start()
    def receive_call(self):
        print("Receiving call")
        self.state.emergency_call = EmergencyCall(location="123 Main St", description="Fire", timestamp="2021-01-01 12:00:00")
        result = EmergencyServicesCrew().crew().kickoff(inputs={"emergency_call": self.state.emergency_call})
        print("Emergency call received", result.raw)
        self.state.fire_fighter_dispatch = result.raw

    @listen(receive_call)
    def dispatch_fire_fighters(self):
        print("Dispatching fire fighters")
        result = EmergencyServicesCrew().crew().kickoff(inputs={"emergency_call": self.state.emergency_call})
        print("Fire fighters dispatched", result.raw)
        self.state.fire_fighter_dispatch = result.raw
    
    @listen(dispatch_fire_fighters)
    def plan_route(self):
        print("Planning route")
        result = FireFightersCrew().crew().kickoff(inputs={"fire_fighter_dispatch": self.state.fire_fighter_dispatch})
        print("Route planned", result.raw)
        self.state.fire_fighter_dispatch = result.raw

    @listen(plan_route)
    def save_route(self):
        print("Saving route")
        with open("data/outputs/route.txt", "w") as f:
            f.write(self.state.fire_fighter_dispatch)


def kickoff():
    emergency_planner_flow = EmergencyPlannerFlow()
    emergency_planner_flow.kickoff()


def plot():
    emergency_planner_flow = EmergencyPlannerFlow()
    emergency_planner_flow.plot()


if __name__ == "__main__":
    kickoff()
