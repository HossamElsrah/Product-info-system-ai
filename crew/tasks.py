from crewai import Task
from .agents import researcher, analyst, reporter

# Define the Research Task
research_task = Task(
    description=(
        "Conduct a thorough online search for the product '{product_name}'. "
        "Find its official website, key features, technical specifications, "
        "and user reviews from trusted websites."
    ),
    expected_output=(
        "A detailed summary of the product's features, specifications, and a collection of user reviews."
    ),
    agent=researcher
)

# Define the Analysis Task
analysis_task = Task(
    description=(
        "Analyze the information gathered by the researcher. "
        "Identify the main pros and cons of the product. "
        "Write a comprehensive report that summarizes all findings, "
        "including a final verdict on the product."
    ),
    expected_output=(
        "A comprehensive final report on the product, including a summary of pros, "
        "cons, and an overall verdict."
    ),
    agent=analyst
)

# Define the Reporting Task
reporting_task = Task(
    description=(
        "Take the comprehensive report from the analyst and format it for final presentation. "
        "Ensure the report is well-structured, with clear headings for pros, cons, "
        "and the final verdict. The final output must be a clean, ready-to-publish document."
    ),
    expected_output=(
        "A professionally formatted final report that is ready for publishing."
    ),
    agent=reporter
)