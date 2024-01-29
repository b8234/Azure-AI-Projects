# Azure Custom Vision Object Detection with Visualization

## Description
This project is part of the Microsoft AI MS Learn series. It uses Azure Cognitive Services Custom Vision for object detection in images. The Python script not only detects objects in an image but also visualizes the results by plotting bounding boxes and labels using matplotlib.

## Objectives
- Implement Azure Custom Vision for object detection in images.
- Visualize detection results using matplotlib and PIL (Python Imaging Library).
- Showcase the capability to combine Azure AI with Python libraries for enhanced data presentation.

## Technologies Used
- Azure Cognitive Services Custom Vision for object detection.
- Python for scripting and data visualization.
- Matplotlib and PIL for image processing and visualization.
- NumPy for image array manipulation.

## Setup and Installation
To set up and run this project:

```
git clone <repository-url>
cd <project-directory>
pip install azure-cognitiveservices-vision-customvision matplotlib Pillow numpy
```

## Configuration
- Set up Azure Custom Vision resources in the Azure portal.
- Create a `.env` file with the necessary Azure service details:
  ```
  PredictionEndpoint=your_prediction_endpoint
  PredictionKey=your_prediction_key
  ProjectID=your_project_id
  ModelName=your_model_name
  ```

## How to Use
- Place the image you want to analyze in the same directory as the script.
- Run the script:

```
python script_name.py
```

## Example Output
The script processes the image, detects objects, and generates a new image with bounding boxes and labels around each detected object. The output is saved as 'output.jpg'.

## Learning Outcomes
- Gained experience in using Azure AI services for advanced object detection.
- Developed skills in creating visualizations for AI model outputs.
- Enhanced understanding of integrating Azure Cognitive Services with Python visualization libraries.

## Acknowledgments
This project is a practical application inspired by the [Azure Cognitive Services Custom Vision documentation](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/).
