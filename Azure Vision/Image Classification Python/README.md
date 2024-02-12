# Azure Custom Vision Model Training and Image Classification Projects

## Description

These projects are part of the Microsoft AI MS Learn series. They utilize Azure Cognitive Services Custom Vision for image classification. The Python scripts automate the process of uploading training images, tagging them, and training a classification model. Additionally, the trained model can be used to classify new images based on its learning.

## Objectives

- Use Azure Custom Vision to train a custom image classification model.
- Automate the uploading and tagging of training images using the Custom Vision Training Client.
- Demonstrate the process of training and iterating over an image classification model.
- Utilize a pre-trained model to predict image labels.
- Automate the process of image classification using Azure Cognitive Services.

## Technologies Used

- Azure Cognitive Services Custom Vision for model training and image classification.
- Python for scripting and interacting with Azure services.
- Custom Vision Training Client for programmatically managing the training process.
- ApiKeyCredentials for authentication.

## Setup and Installation

To set up and run these projects:

```bash
git clone https://github.com/b8234/Azure-AI-Projects.git
cd Azure-AI-Projects/Azure\ Vision/Image\ Classification\ Python
```

Run command to install packages in respective folders:

```bash
pip3 install azure-cognitiveservices-vision-customvision msrest python-dotenv
```

Or install the required dependencies via requirements in respective folders, run the following command:

```bash
pip3 install -r requirements.txt
```

## Configuration

### Create Custom Vision resources

Before you can train a model, you will need Azure resources for training and prediction. You can create Custom Vision resources for each of these tasks, or you can create a single Azure AI Services resource and use it for either (or both).

1. In a new browser tab, open the Azure portal at [https://portal.azure.com](https://portal.azure.com), and sign in using the Microsoft account associated with your Azure subscription.
2. Select the **＋Create a resource** button, search for "custom vision," and create a Custom Vision resource with the following settings:
   - **Create options:** Both
   - **Subscription:** Your Azure subscription
   - **Resource group:** Choose or create a resource group (if you are using a restricted subscription, you may not have permission to create a new resource group - use the one provided)
   - **Region:** Choose any available region
   - **Name:** Enter a unique name
   - **Training pricing tier:** F0
   - **Prediction pricing tier:** F0
   *Note: If you already have an F0 custom vision service in your subscription, select S0 for this one.*
3. Wait for the resources to be created, and then view the deployment details and note that two Custom Vision resources are provisioned; one for training, and another for prediction (evident by the -Prediction suffix). You can view these by navigating to the resource group where you created them.

### Create a Custom Vision project

To train an image classification model, you need to create a Custom Vision project based on your training resource. To do this, you’ll use the Custom Vision portal.

1. In Visual Studio Code, view the training images in the `more-training-images`. This folder contains subfolders of apple, banana, and orange images.
2. In a new browser tab, open the Custom Vision portal at [https://customvision.ai](https://customvision.ai). If prompted, sign in using the Microsoft account associated with your Azure subscription and agree to the terms of service.
3. In the Custom Vision portal, create a new project with the following settings:
   - **Name:** Classify Fruit
   - **Description:** Image classification for fruit
   - **Resource:** The Custom Vision resource you created previously
   - **Project Types:** Classification
   - **Classification Types:** Multiclass (single tag per image)
   - **Domains:** Food
4. In the new project, click [+] Add images, and select all of the files in the `more-training-images/apple` folder you viewed previously. Then upload the image files, specifying the tag apple.
5. Repeat the previous step to upload the images in the banana folder with the tag banana, and the images in the orange folder with the tag orange.
6. Explore the images you have uploaded in the Custom Vision project.
7. In the Custom Vision project, above the images, click Train to train a classification model using the tagged images. Select the Quick Training option, and then wait for the training iteration to complete.
8. When the model iteration has been trained, review the Precision, Recall, and AP performance metrics - these measure the prediction accuracy of the classification model, and should all be high.

### Test the model

Now that you’ve trained the model, you can test it.

1. Above the performance metrics, click Quick Test.
2. In the Image URL box, type `https://aka.ms/apple-image` and click ➔
3. View the predictions returned by your model - the probability score for apple should be the highest.

### View the project settings

The project you have created has been assigned a unique identifier, which you will need to specify in any code that interacts with it.

1. Click the settings (⚙) icon at the top right of the Performance page to view the project settings.
2. Under General (on the left), note the Project Id that uniquely identifies this project.
3. On the right, under Resources note that the key and endpoint are shown. These are the details for the training resource (you can also obtain this information by viewing the resource in the Azure portal).

## Publish the Image Classification Model

Now you’re ready to publish your trained model so that it can be used from a client application.

1. In the Custom Vision portal, on the Performance page, click 🗸 Publish to publish the trained model with the following settings:
   - **Model name:** fruit-classifier
   - **Prediction Resource:** The prediction resource you created previously which ends with “-Prediction” (not the training resource).
   
2. At the top left of the Project Settings page, click the Projects Gallery (👁) icon to return to the Custom Vision portal home page, where your project is now listed.

3. On the Custom Vision portal home page, at the top right, click the settings (⚙) icon to view the settings for your Custom Vision service. Then, under Resources, find your prediction resource which ends with “-Prediction” (not the training resource) to determine its Key and Endpoint values (you can also obtain this information by viewing the resource in the Azure portal).

### Create an .env file to store credentials

- Set up the necessary environment variables in a `.env` file for training:
  ```
  TrainingEndpoint=your_training_endpoint
  TrainingKey=your_training_key
  ProjectID=your_custom_vision_project_id
  ```

- Set up the necessary environment variables in a `.env` file for the prediction:
  ```
  PredictionEndpoint=your_prediction_endpoint
  PredictionKey=your_prediction_key
  ProjectID=your_project_id
  ModelName=your_model_name
  ```

## How to Use

- Place the training images in the 'more-training-images' directory, organized by tags.
- Place the images you want to classify in the 'test-images' directory.
- Run the respective scripts:
  
  For training:
  ```

bash
  python3 train-classifier.py
  ```

  For testing:
  ```bash
  python3 test-classifier.py
  ```

## Example Output

Example output is in the Example Output folder.

## Learning Outcomes

- Gained experience in using Azure Cognitive Services for custom model training and image classification.
- Developed skills in automating the training process of an image classifier and classifying images.
- Enhanced understanding of practical AI applications in custom image classification.

## Acknowledgments

These projects are inspired by exercises in the [Microsoft AI MS Learn series](https://learn.microsoft.com/en-us/training/). The projects also draw on the [Azure Cognitive Services Custom Vision documentation](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/).

## Contact

If you have any questions or feedback, feel free to [open an issue](https://github.com/b8234/Azure-AI-Projects/issues/new). I welcome your input and suggestions to improve this repository further.
