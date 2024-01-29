from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from dotenv import load_dotenv
import os
from PIL import Image
import sys
import time

# Load configuration from .env file
load_dotenv()

# Authenticate
subscription_key = os.getenv("VISION_KEY")
endpoint = os.getenv("VISION_ENDPOINT")

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

# Path to the local image file
local_image_path = "images/Rome.pdf"  # Replace with the path to your local image file

'''
OCR: Read File using the Read API, extract text - local
This example will extract text in a local image, then print results, line by line.
This API call can also extract handwriting style text (not shown).
'''
print("===== Read File - local =====")

# Open the local image file
with open(local_image_path, "rb") as local_image_file:
    # Call API with local image and raw response (allows you to get the operation location)
    read_response = computervision_client.read_in_stream(local_image_file, raw=True)

# Get the operation location (URL with an ID at the end) from the response
read_operation_location = read_response.headers["Operation-Location"]
# Grab the ID from the URL
operation_id = read_operation_location.split("/")[-1]

# Call the "GET" API and wait for it to retrieve the results
while True:
    read_result = computervision_client.get_read_result(operation_id)
    if read_result.status not in ['notStarted', 'running']:
        break
    time.sleep(1)

# Print the detected text, line by line
if read_result.status == OperationStatusCodes.succeeded:
    for text_result in read_result.analyze_result.read_results:
        for line in text_result.lines:
            print(line.text)
            print(line.bounding_box)
print()
'''
END - Read File - local
'''

print("End of Computer Vision quickstart.")
