from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools.tools import ScrapeWebsiteTool, WebsiteSearchTool, SerperDevTool

# Uncomment the following line to use an example of a custom tool
# from sports_flow.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool


@CrewBase
class SportsCrew:
    """SportsFlow crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def sports_news_gatherer(self) -> Agent:
        return Agent(
            config=self.agents_config["sports_news_gatherer"],
            tools=[
                SerperDevTool(),
                ScrapeWebsiteTool(),
                WebsiteSearchTool(),
            ],
            # tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
            verbose=True,
        )

    @task
    def gather_sports_news(self) -> Task:
        return Task(
            config=self.tasks_config["gather_sports_news"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the SportsFlow crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
