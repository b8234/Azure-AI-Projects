# Custom Document Classification with Azure AI Text Analytics

## Description
This project is part of the Microsoft AI MS Learn series. It uses Azure AI Text Analytics for custom document classification. The script processes text data from an `articles` directory and employs Azure AI to classify each document into predefined categories.

## Objectives
- Utilize Azure Text Analytics for custom document classification.
- Implement text data processing and classification using Azure AI services.
- Demonstrate the application of Azure AI in categorizing text documents based on custom criteria.

## Technologies Used
- Azure AI Text Analytics for document classification.
- Python for scripting and automation.
- Azure SDK for integrating Azure services.

## Setup and Installation
To set up and run this project:

```
git clone https://github.com/b8234/Azure-AI-Projects.git
cd Azure-AI-Projects/Azure\ Language/Text\ Classification\ Python/classify-text
```

**Install Dependencies**:

```bash
pip3 install python-dotenv azure-core azure-ai-textanalytics
```
Or install the required dependencies via requirements, run the following command:

```bash
pip3 install -r requirements.txt
```


## Configuration

#### Provision an Azure AI Language Resource

To enable custom text classification, provision an Azure AI Language service resource:

1. Open the Azure portal at [https://portal.azure.com](https://portal.azure.com) and sign in with your Microsoft account.
2. Search for "Azure AI services" in the search field at the top and create a Language Service resource.
3. Select the box that includes Custom text classification, then select Continue to create your resource.
4. Configure the resource with the following settings:
   - Subscription: Your Azure subscription.
   - Resource group: Select or create a resource group.
   - Region: Choose any available region.
   - Name: Enter a unique name.
   - Pricing tier: Select F0 (free) or S (standard) if F is not available.
   - Storage account: New storage account
   - Storage account name: Enter a unique name.
   - Storage account type: Standard LRS
   - Responsible AI notice: Selected.
5. Select Review + create, then select Create to provision the resource.
6. Wait for deployment to complete, then go to the deployed resource.
7. View the Keys and Endpoint page. You will need this information later.

#### Upload Sample Articles

Once you've created the Azure AI Language service and storage account, upload example articles:

1. Download sample articles from [https://aka.ms/classification-articles](https://aka.ms/classification-articles) and extract the files to a folder.
2. In the Azure portal, navigate to the storage account you created.
3. Select Configuration below Settings, enable the option to Allow Blob anonymous access, then select Save.
4. Select Containers below Data storage in the left menu.
5. Select + Container, name it "articles", and set Anonymous access level to Container.
6. After creating the container, select it, then select Upload.
7. Upload the sample articles.

#### Create a Custom Text Classification Project

After configuration is complete, create a custom text classification project:

1. Open the Azure AI Language Studio portal at [https://language.cognitive.azure.com/](https://language.cognitive.azure.com/) and sign in.
2. If prompted, select your Azure subscription and language resource.
3. In the Create new menu, select Custom text classification.
4. On the Connect storage page, all values will already be filled, so select Next.
5. On the Select project type page, choose Single label classification, then select Next.
6. On the Enter basic information page, set the following:
   - Name: ClassifyLab
   - Text primary language: English (US)
   - Description: Custom text lab
7. Select Next.
8. On the Choose container page, set the Blob store container dropdown to your "articles" container.
9. Select No, I need to label my files as part of this project, then select Next.
10. Select Create project.

#### Label Your Data

Label, or tag, your data to train your model how to classify text:

1. Select Data labeling.
2. On the right, select + Add class and create classes: Classifieds, Sports, News, Entertainment.
3. Assign each article the appropriate class and dataset (training or testing) using the Activity pane on the right.
4. Select Save labels to save your labels.

#### Train Your Model

Train your model after labeling your data:

1. Select Training jobs.
2. Start a training job, name it ClassifyArticles, and select Use a manual split of training and testing data.
3. Select Train.

#### Evaluate Your Model

Evaluate and improve your model:

1. Select Model performance and choose your ClassifyArticles model to view its scoring and performance metrics.
2. Select Test set details tab to see any errors in predictions.

#### Deploy Your Model

Deploy your model to start classifying text through the API:

1. Select Deploying model.
2. Add a deployment, enter "articles" in the deployment name field, and select ClassifyArticles in the Model field.
3. Select Deploy.

Keep your project and deployment names for the next steps.

- Add a `.env` file with Azure service details:
  ```
  AI_SERVICE_KEY=your_ai_service_key
  AI_SERVICE_ENDPOINT=your_ai_service_endpoint
  PROJECT=your_project_name
  DEPLOYMENT=your_deployment_name
  ```

## How to Use
Run the script and it will automatically classify documents in the 'articles' directory:

```
python3 classify-text.py
```

## Example Output
Example output is in the Output folder.

## Learning Outcomes
- Gained experience in using Azure AI services for advanced text classification tasks.
- Developed proficiency in Python for Azure AI integrations and text data processing.
- Enhanced understanding of applying AI in the context of document classification and content analysis.

## Acknowledgments
This project is inspired by the exercises in the [Microsoft AI MS Learn series](https://learn.microsoft.com/en-us/training/).

## Contact

If you have any questions or feedback, feel free to [open an issue](https://github.com/b8234/Azure-AI-Projects/issues/new). I welcome your input and suggestions to improve this repository further.
