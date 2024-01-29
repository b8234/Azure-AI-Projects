# Azure Custom Vision Image Upload and Tagging for Model Training

## Description
This project is part of the Microsoft AI MS Learn series. It focuses on preparing a dataset for training an image classification model using Azure Cognitive Services Custom Vision . The Python script automates the process of uploading images and tagging them with regions, leveraging data defined in a JSON file, to facilitate the training of a custom vision model

## Objectives
- Use Azure Custom Vision Training Client to prepare a dataset for model training.
- Automate the uploading and region-based tagging of images.
- Demonstrate the initial steps in creating a custom image classification model using Azure AI.

## Technologies Used
- Azure Cognitive Services Custom Vision for model training.
- Python for scripting and managing the dataset preparation.
- JSON for storing image tagging information.

## Setup and Installation
To set up and run this project:

```
git clone <repository-url>
cd <project-directory>
```
Ensure Python and necessary packages are installed.

## Configuration
- Set up and configure a Custom Vision project in Azure.
- Set up the necessary environment variables in a `.env` file:
  ```
  TrainingEndpoint=your_training_endpoint
  TrainingKey=your_training_key
  ProjectID=your_custom_vision_project_id
  ```

## How to Use
- Organize your images in the 'images' folder and define their tags and regions in 'tagged-images.json'.
- Run the script to upload and tag images in your Custom Vision project:

```
python script_name.py
```

## Example Output
The script will indicate the status of the image upload process, including any failures or issues in tagging.

## Learning Outcomes
- Gained experience in preparing datasets for custom vision model training.
- Developed skills in automating dataset management for AI applications.
- Enhanced understanding of the workflow in creating and training custom vision models using Azure AI.

## Acknowledgments
This project is a practical application inspired by the [Azure Cognitive Services Custom Vision documentation](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/).
