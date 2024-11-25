from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from research_crew.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class ResearchCrewCrew():
	"""ResearchCrew crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def content_planner(self) -> Agent:
		return Agent(
			config=self.agents_config['content_planner'],
			verbose=True
		)

	@task
	def plan(self) -> Task:
		return Task(
			config=self.tasks_config['plan'],
			agent=self.content_planner()
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the ResearchCrew crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=2,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)