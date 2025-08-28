import os
from dotenv import load_dotenv
from crew.crew import product_crew

# Load environment variables from .env file
load_dotenv()

# Run the crew
product_name = input("Enter the product name you want to research: ")
result = product_crew.kickoff(inputs={'product_name': product_name})

# Print the final report
print("\n\nFinal Report:\n")
print(result)