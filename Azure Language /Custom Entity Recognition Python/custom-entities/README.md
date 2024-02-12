# Custom Entity Recognition with Azure AI Text Analytics

## Description
This project is part of the Microsoft AI MS Learn series. It uses Azure AI Text Analytics for custom entity recognition. The Python script processes text data from a directory, applying Azure's AI to extract and analyze custom entities


## Objectives
- Implement Azure Text Analytics for custom entity recognition.
- Integrate Azure AI services with Python to process text data.
- Demonstrate practical skills in handling and analyzing unstructured text data.

## Technologies Used
- Azure AI Text Analytics.
- Python for scripting and automation.
- Azure SDK for seamless integration with Azure services.

## Setup and Installation
To set up this project:
```
git clone https://github.com/b8234/Azure-AI-Projects.git
cd Azure-AI-Projects/Azure\ Language/Custom\ Entity\ Recognition\ Python/custom-entities
```

**Install Dependencies**:

```bash
pip3 install python-dotenv azure-ai-textanalytics azure-core
```
Or install the required dependencies via requirements, run the following command:

```bash
pip3 install -r requirements.txt
```

## Configuration

To configure your application with the Azure AI Language Service, follow these steps:

### 1. Provisioning Azure AI Language Resource and Storage Account:

1. Sign in to the [Azure portal](https://portal.azure.com/).
2. Create an Azure AI Language Service resource with custom text classification & extraction feature enabled:
   - Click on the "Create a resource" button.
   - Search for "Language" and select "Azure AI Language".
   - Choose the appropriate subscription, resource group, region, and name for your AI Language resource.
   - Select "F0 (free)" or "S (standard)" pricing tier, depending on your preference and availability.
   - Enable the "Custom text classification & extraction" feature.
   - Click on "Review + create" and then "Create" to provision the resource.
3. Retrieve necessary information:
   - Once the resource is deployed, navigate to the resource in the Azure portal.
   - Go to the "Keys and Endpoint" page to obtain the AI service key and endpoint.

### 2. Creating Custom Named Entity Recognition Project:

1. Access the [Azure AI Language Studio portal](https://language.cognitive.azure.com/).
2. Sign in using the Microsoft account associated with your Azure subscription.
3. Create a new custom named entity recognition project:
   - If prompted to choose a language resource, select the appropriate settings for your Azure subscription and AI Language resource.
   - Click on "Language Studio" at the top of the portal.
   - From the "Create new" menu, select "Custom named entity recognition".
   - Configure the project with basic information such as name, text primary language, and description.
   - Connect the project to the storage account you created earlier and specify the blob store container for data.

### 3. Labeling Data and Training the Model:

1. Label the data by adding entities like "ItemForSale", "Price", and "Location" to the text documents within the project.
2. Train the model using the labeled data:
   - Navigate to the "Training jobs" section in the left pane.
   - Start a new training job, providing settings such as model name and testing data split.

### 4. Evaluating Model Performance and Deployment:

1. Evaluate the model's performance by reviewing scoring, metrics, and testing results in the Azure AI Language Studio portal.
2. Deploy the trained model for entity extraction through the API:
   - Navigate to the "Deploying a model" section in the left pane.
   - Add a deployment, specifying a name for the deployment and selecting the trained model.

After completing these steps, you should have all the necessary information, including the AI service key, endpoint, project name, and deployment name, which you can then use in your application configuration.

## Add Key, Endpoint, Project Name, and Deployment Name to .env file to run script.


- Add a `.env` file with the Azure service details:
  ```
  AI_SERVICE_KEY=your_ai_service_key
  AI_SERVICE_ENDPOINT=your_ai_service_endpoint
  PROJECT=your_project_name
  DEPLOYMENT=your_deployment_name
  ```

## How to Use
Run the script using:
```
python3 custom-entities.py
```
The script will analyze text files in the 'ads' directory for custom entities.

## Example Output
The script outputs custom entities recognized in each text file, including the entity text, category, and confidence score.

## Learning Outcomes
- Gained experience in implementing custom entity recognition using Azure AI.
- Enhanced Python programming skills, particularly in integrating with Azure Cognitive Services.
- Developed a deeper understanding of applying AI for text analytics in real-world scenarios.

## Acknowledgments
This project was inspired by the exercises in the [Microsoft AI MS Learn series](https://learn.microsoft.com/en-us/training/).

## Contact

If you have any questions or feedback, feel free to [open an issue](https://github.com/b8234/Azure-AI-Projects/issues/new). I welcome your input and suggestions to improve this repository further.
