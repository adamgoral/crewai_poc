#!/usr/bin/env python

from crewai.flow.flow import Flow, listen, start
from pydantic import BaseModel

from .crews.sports_crew.sports_crew import SportsCrew


class ResearchState(BaseModel):
    opportunities: str | None = None
    models: str | None = None

class TipsState(BaseModel):
    tips: str | None = None

class ResearchFlow(Flow[TipsState]):

    @start()
    def run_sports_crew(self):
        print("Generating trading models")
        result = (
            SportsCrew()
            .crew()
            .kickoff(inputs={})
        )
        self.state.tips = result.raw

    @listen(run_sports_crew)
    def save_tips(self):
        print("Saving tips")
        print("Tips generated:")
        print(self.state.tips)
        self.state.tips = self.state.tips


def kickoff():
    flow = ResearchFlow()
    flow.kickoff()


def plot():
    flow = ResearchFlow()
    flow.plot()


if __name__ == "__main__":
    kickoff()
