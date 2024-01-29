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
git clone <repository-url>
cd <project-directory>
pip install azure-ai-textanalytics python-dotenv
```

## Configuration
- Create Azure Text Analytics resources in the Azure portal.
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
python script_name.py
```

## Example Output
The script will output the classification for each document in the directory, including the category and confidence score.

## Learning Outcomes
- Gained experience in using Azure AI services for advanced text classification tasks.
- Developed proficiency in Python for Azure AI integrations and text data processing.
- Enhanced understanding of applying AI in the context of document classification and content analysis.

## Acknowledgments
This project is inspired by the exercises in the [Microsoft AI MS Learn series](link_to_the_relevant_MS_Learn_module).
