from flask import *
import os
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
from dotenv import load_dotenv
from app import app
load_dotenv()


prediction_key = os.getenv('KEY')
ENDPOINT = os.getenv('ENDPOINT')
projectId = os.getenv('PROJECT_ID')
publish_iteration_name = os.getenv('PUBLISHED_ITERATION_NAME')
