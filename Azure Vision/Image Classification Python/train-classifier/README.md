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
git clone https://github.com/b8234/Azure-AI-Projects.git
cd Azure-AI-Projects/Azure\ Vision/Image\ Classification\ Python/train-classifier
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
Example output is in the Example Output folder.

## Learning Outcomes
- Gained experience in using Azure Cognitive Services for custom model training.
- Developed skills in automating the training process of an image classifier.
- Enhanced understanding of practical AI applications in custom image classification.

## Acknowledgments
This project is inspired by exercises in the [Microsoft AI MS Learn series](https://learn.microsoft.com/en-us/training/).

## Contact

If you have any questions or feedback, feel free to [open an issue](https://github.com/b8234/Azure-AI-Projects/issues/new). I welcome your input and suggestions to improve this repository further.
