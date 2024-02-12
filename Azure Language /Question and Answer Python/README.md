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

# Configuration

### Provision an Azure AI Language Resource

If you don’t already have one in your subscription, you’ll need to provision an Azure AI Language service resource. Additionally, to create and host a knowledge base for question answering, you need to enable the Question Answering feature.

1. Open the [Azure portal](https://portal.azure.com) and sign in using the Microsoft account associated with your Azure subscription.
2. Search for "Azure AI services" in the search field at the top and select "Create" under "Language Service" in the results.
3. Select the "Custom question answering" block. Then select Continue to create your resource with the specified settings:
   - Subscription: Your Azure subscription
   - Resource group: Choose or create a resource group
   - Region: Choose any available location
   - Name: Enter a unique name
   - Pricing tier: Select F0 (free), or S (standard) if F is not available
   - Azure Search region: Choose a location in the same global region as your Language resource
   - Azure Search pricing tier: Free (F) (If this tier is not available, select Basic (B))
   - Responsible AI Notice: Agree
4. Select "Create + review", then select "Create".

**Note**: Custom Question Answering uses Azure Search to index and query the knowledge base of questions and answers.

Wait for deployment to complete, and then go to the deployed resource. View the "Keys and Endpoint" page. You will need the information on this page later in the exercise.

### Create a Question Answering Project

To create a knowledge base for question answering in your Azure AI Language resource, you can use the Language Studio portal to create a question answering project. In this case, you’ll create a knowledge base containing questions and answers about Microsoft Learn.

1. Access the [Azure AI Language Studio portal](https://language.cognitive.azure.com/) and sign in using the Microsoft account associated with your Azure subscription.
2. If prompted to choose a Language resource, select the appropriate settings for your Azure subscription and AI Language resource.
3. Create a new project for question answering and configure it with basic information:
   - Name: LearnFAQ
   - Description: FAQ for Microsoft Learn
   - Default answer when no answer is returned: Sorry, I don't understand the question
4. Add sources to the knowledge base:
   - Import questions and answers from an existing FAQ page or document.
   - Add predefined "chit chat" questions and answers to support common conversational exchanges.

### Edit the Knowledge Base

Your knowledge base has been populated with question and answer pairs from the Microsoft Learn FAQ, supplemented with a set of conversational chit-chat question and answer pairs. You can extend the knowledge base by adding additional question and answer pairs.

1. In your LearnFAQ project in Language Studio, select the Edit knowledge base page to see the existing question and answer pairs.
2. In the knowledge base, on the Question answer pairs tab, select ＋, and create a new question answer pair with the following settings:
   - Source: [Microsoft Learn FAQ](https://docs.microsoft.com/en-us/learn/support/faq)
   - Question: What are Microsoft credentials?
   - Answer: Microsoft credentials enable you to validate and prove your skills with Microsoft technologies.
3. In the page for the "What are Microsoft credentials?" question that is created, expand Alternate questions. Then add the alternate question: How can I demonstrate my Microsoft technology skills?

### Train and Test the Knowledge Base

Now that you have a knowledge base, you can test it in Language Studio.

1. Save the changes to your knowledge base.
2. Test the knowledge base in Language Studio by entering various messages and reviewing the responses.

### Deploy the Knowledge Base

The knowledge base provides a back-end service that client applications can use to answer questions. Now you are ready to publish your knowledge base and access its REST interface from a client.

1. In the LearnFAQ project in Language Studio, select the Deploy knowledge base page.
2. At the top of the page, select Deploy. Then select Deploy to confirm you want to deploy the knowledge base.
3. When deployment is complete, select Get prediction URL to view the REST endpoint for your knowledge base and note that the sample request includes parameters for:
   - projectName: The name of your project (which should be LearnFAQ)
   - deploymentName: The name of your deployment (which should be production)
4. Close the prediction URL dialog box.

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

