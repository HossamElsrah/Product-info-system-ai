# crew/crew.py
from crewai import Crew, Process
from .agents import researcher, analyst, reporter
from .tasks import research_task, analysis_task, reporting_task
from tools.custom_tools import search_tool


researcher.tools = [search_tool]

# Create the crew
product_crew = Crew(
    agents=[researcher, analyst, reporter],
    tasks=[research_task, analysis_task, reporting_task],
    process=Process.sequential,
    verbose=True
)