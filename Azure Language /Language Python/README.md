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
git clone https://github.com/b8234/Azure-AI-Projects.git
cd Azure-AI-Projects/Azure\ Language/Language\ Python/clock-client
```

**Install Dependencies**:

```bash
pip3 install python-dotenv azure-core azure-ai-language-conversations
```
Or install the required dependencies via requirements, run the following command:

```bash
pip3 install -r requirements.txt
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
python3 clock-client.py
```
The script will analyze the entered text and provide insights based on the Azure AI Language Service's analysis.

## Example Output
Example output is in the Output folder

## Learning Outcomes
- Acquired practical experience with Azure Language Services in a conversational AI context.
- Enhanced skills in Python for integrating Azure AI services in an application.
- Developed an understanding of applying AI for real-time language analysis and intent recognition.

## Acknowledgments
This project is inspired by exercises in the [Microsoft AI MS Learn series](https://learn.microsoft.com/en-us/training/).

## Contact

If you have any questions or feedback, feel free to [open an issue](https://github.com/b8234/Azure-AI-Projects/issues/new). I welcome your input and suggestions to improve this repository further.
