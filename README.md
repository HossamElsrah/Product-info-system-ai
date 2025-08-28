# Product Information System

### Overview

The **Product Information System** is a powerful AI-powered application designed to provide comprehensive details and analysis on any product. This system leverages a sophisticated multi-agent framework built with **CrewAI** to automate product research, and a **FastAPI** backend to expose this functionality through a user-friendly API.

The primary goal is to transform raw product inquiries into a structured, informative report, making it an ideal backend for mobile applications, e-commerce sites, or internal business tools.

-----

### Key Features

  * **Multi-Agent AI:** The core of the system is a three-agent crew that works collaboratively:
      * **Senior Researcher:** A specialized agent that scours the web to gather facts, technical specifications, and key information about a given product. It acts as the primary data collector.
      * **Product Analyst:** This agent processes the raw data from the researcher, synthesizes it, and generates a clear, well-structured final report. Its role is to organize and present the information logically.
      * **Financial Analyst:** This agent's specific task is to research and analyze the pricing, market position, and potential value of the product, providing a crucial business perspective to the final report.
  * **RESTful API:** A robust API built with FastAPI that allows for simple product queries via HTTP requests. The API handles all the heavy lifting of triggering the AI agents and returning a clean JSON response.
  * **Containerized Deployment:** The entire application is packaged in a Docker container, ensuring consistent and reproducible behavior across different environments, from local development to production on the cloud.

-----

### Technologies Used

  * **Python 3.11:** The core programming language.
  * **CrewAI:** For orchestrating the multi-agent system.
  * **FastAPI:** To build the high-performance API.
  * **Docker:** For application containerization and easy deployment.
  * **Uvicorn:** The ASGI server to run the FastAPI application.

-----

### Getting Started

These instructions will get a copy of the project up and running on your local machine.

#### **Prerequisites**

  * **Python 3.11** or higher
  * **Docker Desktop** (or any Docker engine)

#### **Installation**

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/product-info-system-ai.git
    cd product-info-system-ai
    ```
2.  **Set up your environment variables:**
    Create a `.env` file in the root directory of the project with your API keys. Replace the placeholder values with your actual keys.
    ```env
    OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
    # Other API keys like SERPER_API_KEY can be added here
    ```
3.  **Build the Docker image:**
    This command will build the Docker image and install all necessary dependencies.
    ```bash
    docker build -t product-info-api .
    ```
4.  **Run the Docker container:**
    This will run the application and map port `8000` from the container to your local machine, making the API accessible.
    ```bash
    docker run -p 8000:8000 product-info-api
    ```

-----

### **API Endpoints**

Once the container is running, the API documentation is available at `http://localhost:8000/docs`.

**Example Request:**
To get a product report, send a `POST` request to the `/analyze` endpoint with a JSON body containing the product name.

  * **Endpoint:** `/analyze`
  * **Method:** `POST`
  * **Body:**
    ```json
    {
      "product_name": "GoPro Hero 11"
    }
    ```
  * **Example `curl` command:**
    ```bash
    curl -X 'POST' \
      'http://localhost:8000/analyze' \
      -H 'Content-Type: application/json' \
      -d '{
      "product_name": "GoPro Hero 11"
    }'
    ```
