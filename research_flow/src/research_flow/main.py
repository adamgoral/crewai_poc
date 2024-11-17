#!/usr/bin/env python
from random import randint
import os
from typing import Optional
from pydantic import BaseModel

from crewai.flow.flow import Flow, listen, start

from .crews.research_crew.research_crew import ResearchCrew


class ResearchState(BaseModel):
    opportunities: Optional[str] = None
    models: Optional[str] = None


class ResearchFlow(Flow[ResearchState]):

    @start()
    def generate_trading_models(self):
        print("Generating trading models")
        result = (
            ResearchCrew()
            .crew()
            .kickoff(inputs={"topic": "FX"})
        )
        self.state.opportunities = result.raw

    @listen(generate_trading_models)
    def save_trading_models(self):
        print("Saving models")
        print("Models generated:", self.state.opportunities)
        self.state.models = self.state.opportunities


def kickoff():
    flow = ResearchFlow()
    flow.kickoff()


def plot():
    flow = ResearchFlow()
    flow.plot()


if __name__ == "__main__":
    kickoff()
