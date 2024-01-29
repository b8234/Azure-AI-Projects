# Azure Custom Vision Model Training Project

## Description
This project is part of the Microsoft AI MS Learn series. It uses Azure Cognitive Services Custom Vision. The Python script automates the process of uploading training images, tagging them, and training a classification model.

## Objectives
- Use Azure Custom Vision to train a custom image classification model.
- Automate the uploading and tagging of training images using the Custom Vision Training Client.
- Demonstrate the process of training and iterating over an image classification model.

## Technologies Used
- Azure Cognitive Services Custom Vision for model training.
- Python for scripting and interacting with Azure services.
- Custom Vision Training Client for programmatically managing the training process.

## Setup and Installation
To set up and run this project:

```
git clone <repository-url>
cd <project-directory>
```
Ensure Python and necessary packages are installed.

## Configuration
- Create and configure a Custom Vision project in Azure.
- Set up the necessary environment variables in a `.env` file:
  ```
  TrainingEndpoint=your_training_endpoint
  TrainingKey=your_training_key
  ProjectID=your_custom_vision_project_id
  ```

## How to Use
- Place the training images in the 'more-training-images' directory, organized by tags.
- Run the script to upload images, tag them, and start the training process:

```
python script_name.py
```

## Example Output
The script outputs the status of the image upload, tagging, and model training process, eventually indicating the completion of the model training.

## Learning Outcomes
- Gained experience in using Azure Cognitive Services for custom model training.
- Developed skills in automating the training process of an image classifier.
- Enhanced understanding of practical AI applications in custom image classification.

## Acknowledgments
This project is a practical application inspired by the [Azure Cognitive Services Custom Vision documentation](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/).
