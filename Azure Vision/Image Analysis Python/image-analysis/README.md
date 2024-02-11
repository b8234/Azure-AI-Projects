# Analyze Images - Computer Vision

## Description
This project is a part of the Microsoft AI MS Learn series and focuses on implementing Azure Cognitive Services' Computer Vision to analyze images. The Python script utilizes the Computer Vision API to extract features like categories, descriptions, and tags from a provided image, demonstrating a key application of cloud-based AI in image processing.

## Objectives
- Utilize Azure Cognitive Services' Computer Vision for image analysis.
- Extract categories, descriptions, and tags from images using Azure AI capabilities.
- Demonstrate practical image processing skills in a cloud environment.

## Technologies Used
- Azure Cognitive Services - Computer Vision.
- Python for scripting and interaction with Azure services.
- Python Imaging Library (PIL) for image handling.

## Setup and Installation
To set up and run this project:

```
git clone https://github.com/b8234/Azure-AI-Projects.git
cd Azure-AI-Projects/Azure\ Vision/Image\ Analysis\ Python/image-analysis
```

Run command to install packages:

```
pip3 install azure-cognitiveservices-vision-computervision python-dotenv pillow
```

Or install the required dependencies via requirements.txt, run the following command:

```bash
pip3 install -r requirements.txt
```

## Configuration
- Set up Azure Cognitive Services in the Azure portal.
- Create a `.env` file with your Computer Vision service credentials:
  ```
  VISION_KEY=your_vision_key
  VISION_ENDPOINT=your_vision_endpoint
  ```

## How to Use
To run the script:

```
python3 image_analysis.py 
```
Replace `image_analysis.py` with the name of your script, and provide an image path if needed.

## Example Output
Example output is in the Output folder.

## Learning Outcomes
- Gained experience in using Azure Cognitive Services for advanced image processing.
- Developed skills in integrating cloud AI services with Python applications.
- Enhanced understanding of Computer Vision concepts and their practical applications.

## Acknowledgments
This project is inspired by exercises in the [Microsoft AI MS Learn series](https://learn.microsoft.com/en-us/training/).

## Contact

If you have any questions or feedback, feel free to [open an issue](https://github.com/b8234/Azure-AI-Projects/issues/new). I welcome your input and suggestions to improve this repository further.
