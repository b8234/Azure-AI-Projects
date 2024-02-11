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
pip install azure-ai-textanalytics python-dotenv
```

## Configuration
- Create Azure Text Analytics resources in Azure.
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
python script_name.py
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
