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
git clone https://github.com/b8234/Azure-AI-Projects.git
cd Azure-AI-Projects/Azure\ Language/Question\ and\ Answer\ Python/qna-app
```

**Install Dependencies**:

```bash
pip3 install python-dotenv azure-core azure-ai-language-questionanswering
```
Or install the required dependencies via requirements, run the following command:

```bash
pip3 install -r requirements.txt
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
python3 qna-app.py
```
The script will provide answers based on Azure AI's Question Answering service.

## Example Output
Example output is in the Output folder.

## Learning Outcomes
- Developed skills in integrating Azure AI services for natural language processing tasks.
- Gained experience in creating conversational AI applications using Azure's cognitive services.
- Enhanced understanding of developing AI solutions that interact and respond to user inputs.

## Acknowledgments
This project was inspired by the exercises in the [Microsoft AI MS Learn series](https://learn.microsoft.com/en-us/training/).

## Contact

If you have any questions or feedback, feel free to [open an issue](https://github.com/b8234/Azure-AI-Projects/issues/new). I welcome your input and suggestions to improve this repository further.

