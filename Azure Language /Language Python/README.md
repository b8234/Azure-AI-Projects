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

To configure your application with the Azure AI Language Service, follow these steps:

### 1. Provisioning Azure AI Language Resource and Storage Account:

If you don’t already have one in your subscription, you’ll need to provision an Azure AI Language service resource in your Azure subscription.

1. Open the [Azure portal](https://portal.azure.com) and sign in using the Microsoft account associated with your Azure subscription.
2. Search for "Azure AI services" in the search field at the top.
3. Select "Create" under "Language Service" in the results.
4. Continue to create your resource with the following settings:
   - Subscription: Your Azure subscription.
   - Resource group: Choose or create a resource group.
   - Region: Choose any available region.
   - Name: Enter a unique name.
   - Pricing tier: Select F0 (free), or S (standard) if F is not available.
   - Responsible AI Notice: Agree.
5. Select "Review + create" and then "Create" to provision the resource.
6. Once the resource is deployed, go to the deployed resource and view the "Keys and Endpoint" page to obtain the AI service key and endpoint.

### 2. Creating Custom Named Entity Recognition Project:

1. Access the [Azure AI Language Studio portal](https://language.cognitive.azure.com/) and sign in using the Microsoft account associated with your Azure subscription.
2. If prompted to choose a Language resource, select the appropriate settings for your Azure subscription and AI Language resource.
3. Click on "Language Studio" at the top of the portal.
4. From the "Create new" menu, select "Conversational language understanding".
5. Configure the project with basic information such as name, primary language, and description.
6. Connect the project to the Azure AI Language resource you created earlier.

### 3. Labeling Data and Training the Model:

1. Label the data by adding intents and utterances to the project.
2. Train the model using the labeled data:
   - Navigate to the "Training jobs" section and start a new training job with appropriate settings.

### 4. Evaluating Model Performance and Deployment:

1. Evaluate the model's performance by reviewing scoring, metrics, and testing results.
2. Deploy the trained model for entity extraction through the API:
   - Navigate to the "Deploying a model" section and add a deployment with a chosen name.

### 5. Create a `.env` file with Azure service credentials:

1. Create a new file in your project directory named `.env`.
2. Open the `.env` file in a text editor.
3. Add the following lines to the file, replacing `your_language_service_key` and `your_language_service_endpoint` with the actual values obtained from the Azure portal:

```plaintext
LS_CONVERSATIONS_KEY=your_language_service_key
LS_CONVERSATIONS_ENDPOINT=your_language_service_endpoint
```

After completing these steps, you should have all the necessary information, including the AI service key, endpoint, project name, and deployment name, which you can then use in your application configuration.


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
