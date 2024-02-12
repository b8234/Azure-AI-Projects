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

```bash
git clone https://github.com/b8234/Azure-AI-Projects.git
cd Azure-AI-Projects/Azure\ Vision/Object\ Detection\ Python
```
Run command to install packages in respective folders:

Install packages in train-detector folder

```bash
pip3 install azure-cognitiveservices-vision-customvision msrest python-dotenv
```
Install packages in test-detector folder

```bash
pip3 install azure-cognitiveservices-vision-customvision matplotlib Pillow numpy
```

Or install the required dependencies via requirements in respective folders, run the following command:

```bash
pip3 install -r requirements.txt
```

## Configuration

### Set up Custom Vision Project in Azure

To train an object detection model, you'll need to create a Custom Vision project using the Custom Vision portal. Follow these steps to set up your project and prepare it for training:

1. **Sign in to the Custom Vision Portal**:
   - Open a new browser tab and navigate to [https://customvision.ai](https://customvision.ai).
   - Sign in using the Microsoft account associated with your Azure subscription.

2. **Create a New Project**:
   - Once signed in, create a new project with the following details:
     - **Name:** Detect Fruit
     - **Description:** Object detection for fruit.
     - **Resource:** Select the Custom Vision resource you created previously.
     - **Project Types:** Choose Object Detection.
     - **Domains:** General.
   - Wait for the project to be created and opened in the browser.

3. **Add and Tag Images**:
   - In your object detection project, select **Add images** and upload all the images from the `train-detector/images` folder where you cloned the repository. This folder contains images of fruit.
   - After uploading, select the first image to open it.
   - Hover over any object in the image until an automatically detected region is displayed. You can also manually drag around the object to create a region if needed.
   - Once the region surrounds the object, add a new tag with the appropriate object type (apple, banana, or orange).
   - Tag each object in the image, resizing the regions and adding new tags as required.
   - Use the **>** link on the right to go to the next image and continue tagging each object.
   - Once all images are tagged, close the Image Detail editor and navigate to the **Training Images** page.
   - Under **Tags**, select **Tagged** to see all the tagged images.

Before proceeding with the Custom Vision project setup, ensure you have the necessary environment variables configured.

### Set up Environment Variables

1. Create a `.env` file in the root directory of your project.
2. Add the following environment variables to the `.env` file:
   ```
   TrainingEndpoint=your_training_endpoint
   TrainingKey=your_training_key
   ProjectID=your_custom_vision_project_id
   ```
3. Replace `your_training_endpoint`, `your_training_key`, and `your_custom_vision_project_id` with the values you obtained from the Azure portal.


## Training and Testing the Object Detection Model

Once you've tagged the images in your project, you're ready to train and test your object detection model. Follow these steps to complete the training process and publish your model for use:

1. **Train the Model**:
   - In the Custom Vision project, click on **Train** to initiate training of the object detection model using the tagged images.
   - Select the **Quick Training** option and wait for the training process to complete. This may take around ten minutes.
   - After training, review the Precision, Recall, and mAP performance metrics. These metrics measure the prediction accuracy of the classification model and should ideally be high.

- Run the script:

```bash
python3 train-detector.py
```

2. **Test the Model**:
   - At the top right of the page, click on **Quick Test**.
   - In the Image URL box, enter [https://aka.ms/apple-orange](https://aka.ms/apple-orange) and view the prediction generated for the image.
   - Close the Quick Test window after reviewing the prediction.

3. **Publish the Model**:
   - In the Custom Vision portal, navigate to the **Performance** page.
   - Click on the checkmark icon (✓) labeled **Publish** to publish the trained model.
   - Specify the following settings for publishing:
     - **Model name:** fruit-detector
     - **Prediction Resource:** Select the prediction resource you created previously, which ends with "-Prediction" (not the training resource).
   - Once published, click on the **Projects Gallery** icon (👁) at the top left of the Project Settings page to return to the Custom Vision portal home page, where your project is now listed.

4. **Retrieve Key and Endpoint Values**:
   - On the Custom Vision portal home page, click on the settings icon (⚙) at the top right to view the settings for your Custom Vision service.
   - Under **Resources**, find your prediction resource, which ends with "-Prediction" (not the training resource), to determine its **Key** and **Endpoint** values. You can also obtain this information by viewing the resource in the Azure portal.

### Create an .env file to store credentials

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

```bash
python3 test-detector.py
```

## Example Output
Example output is in the Example Output folder.

## Learning Outcomes
- Gained experience in using Azure AI

 services for advanced object detection.
- Developed skills in creating visualizations for AI model outputs.
- Enhanced understanding of integrating Azure Cognitive Services with Python visualization libraries.

## Acknowledgments
This project is a practical application inspired by the [Azure Cognitive Services Custom Vision documentation](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/).

This project is inspired by exercises in the [Microsoft AI MS Learn series](https://learn.microsoft.com/en-us/training/).

## Contact

If you have any questions or feedback, feel free to [open an issue](https://github.com/b8234/Azure-AI-Projects/issues/new). I welcome your input and suggestions to improve this repository further.
