# Conversation Analysis - Azure Language Service

## Description
This project is part of the Microsoft AI MS Learn series. It uses Azure Language Service's Conversation Analysis Client. The Python script interacts with the Azure AI Language service to analyze natural language input, identifying intents, entities, and appropriate actions in user queries.

## Objectives
- Leverage Azure Language Service for processing conversational language.
- Implement intent recognition and entity extraction from user input.
- Demonstrate the application of Azure AI in understanding and responding to natural language queries.

## Technologies Used
- Azure AI Language Services for conversation analysis.
- Python for building the interaction script.
- Azure SDK to facilitate the communication between the script and Azure services.

## Setup and Installation
To set up this project:

```
git clone <repository-url>
cd <project-directory>
pip install azure-ai-language python-dotenv
```

## Configuration
- Set up Azure Language Service resources in Azure.
- Create a `.env` file with Azure service credentials:
  ```
  LS_CONVERSATIONS_KEY=your_language_service_key
  LS_CONVERSATIONS_ENDPOINT=your_language_service_endpoint
  ```

## How to Use
Run the script and enter text when prompted:

```
python script_name.py
```
The script will analyze the entered text and provide insights based on the Azure AI Language Service's analysis.

## Example Output
The script will output the top intent recognized in the text, along with any entities identified and their confidence scores. Additionally, it will demonstrate how this information can be used to determine actions or responses.

## Learning Outcomes
- Acquired practical experience with Azure Language Services in a conversational AI context.
- Enhanced skills in Python for integrating Azure AI services in an application.
- Developed an understanding of applying AI for real-time language analysis and intent recognition.

## Acknowledgments
This project is inspired by exercises in the [Microsoft AI MS Learn series](link_to_the_relevant_MS_Learn_module).
