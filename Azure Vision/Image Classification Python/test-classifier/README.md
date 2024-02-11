# Azure Custom Vision Image Classification Project

## Description
This project is a part of the Microsoft AI MS Learn series and focuses on implementing Azure Cognitive Services' Custom Vision for image classification. Utilizing a trained model, the Python script classifies images in a specified directory, predicting their labels based on the model's training

## Objectives
- Leverage Azure Custom Vision for classifying images.
- Utilize a pre-trained model to predict image labels.
- Automate the process of image classification using Azure Cognitive Services.

## Technologies Used
- Azure Cognitive Services Custom Vision.
- Python for scripting and interfacing with Azure services.
- ApiKeyCredentials for authentication.

## Setup and Installation
To set up and run this project:

```
git clone https://github.com/b8234/Azure-AI-Projects.git
cd Azure-AI-Projects/Azure\ Vision/Image\ Classification\ Python/test-classifier
```
Run command to install packages:

```
pip3 install azure-cognitiveservices-vision-customvision msrest python-dotenv
```

Or install the required dependencies via requirements, run the following command:

```bash
pip3 install -r requirements.txt
```

## Configuration
- Create and train a model in Azure Custom Vision.
- Set up the necessary environment variables in a `.env` file:
  ```
  PredictionEndpoint=your_prediction_endpoint
  PredictionKey=your_prediction_key
  ProjectID=your_project_id
  ModelName=your_model_name
  ```

## How to Use
- Place the images you want to classify in the 'test-images' directory.
- Run the script:

```
python3 test-classifier.py
```

## Example Output
Example output is in the Example Output folder.

## Learning Outcomes
- Gained experience in using Azure Cognitive Services for custom image classification.
- Developed skills in integrating Azure AI services with Python applications.
- Enhanced understanding of practical AI applications in the field of computer vision.

## Acknowledgments
This project is a practical application inspired by the [Azure Cognitive Services Custom Vision documentation](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/).
