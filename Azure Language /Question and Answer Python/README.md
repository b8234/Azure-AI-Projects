# Azure AI Question Answering Project

## Description
This project is part of the Microsoft AI MS Learn series. It uses Azure AI's Question Answering Client. The script is designed to interact with the Azure AI Language service to process and answer questions based on a predefined knowledge base or project.

## Objectives
- Utilize Azure AI's Question Answering Client to answer user queries.
- Implement Azure AI services to fetch relevant answers with confidence scores.
- Showcase practical application of Azure AI in building question-answering systems.

## Technologies Used
- Azure AI Question Answering Services.
- Python for scripting and communicating with Azure services.
- Azure SDK to facilitate Azure service integration.

## Setup and Installation
To set up this project:

```
git clone <repository-url>
cd <project-directory>
pip install azure-ai-language python-dotenv
```

## Configuration
- Create Azure AI resources (Question Answering service) in Azure.
- Add a `.env` file with the necessary Azure service details:
  ```
  AI_SERVICE_KEY=your_ai_service_key
  AI_SERVICE_ENDPOINT=your_ai_service_endpoint
  QA_PROJECT_NAME=your_qa_project_name
  QA_DEPLOYMENT_NAME=your_qa_deployment_name
  ```

## How to Use
Run the script and input your question when prompted:

```
python script_name.py
```
The script will provide answers based on the Azure AI's Question Answering service.

## Example Output
For each query, the script outputs the most relevant answer, its confidence score, and the source of the information.

## Learning Outcomes
- Developed skills in integrating Azure AI services for natural language processing tasks.
- Gained experience in creating conversational AI applications using Azure's cognitive services.
- Enhanced understanding of developing AI solutions that interact and respond to user inputs.

## Acknowledgments
This project was inspired by the exercises in the [Microsoft AI MS Learn series](link_to_the_relevant_MS_Learn_module).
