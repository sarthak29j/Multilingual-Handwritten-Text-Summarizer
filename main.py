import io
import json
import time
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes, VisualFeatureTypes
import requests
from PIL import Image, ImageDraw, ImageFont
import os

import nltk
#nltk.download('stopwords')
#nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

credential = json.load(open('credential1.json'))
API_KEY = credential['API_KEY']
ENDPOINT = credential['ENDPOINT']

cv_client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(API_KEY))

image = 'images/sample.jpg'
response = cv_client.read_in_stream( open(image, 'rb'), language = 'en', raw = True)
operationlocation = response.headers['Operation-Location']
operation_id = operationlocation.split('/')[-1]
time.sleep(5)
result = cv_client.get_read_result(operation_id)

text = ''
if result.status == OperationStatusCodes.succeeded:
    read_result = result.analyze_result.read_results
    for analyzed_result in read_result:
        for line in analyzed_result.lines:
            text = text + line.text + ' ' 
      
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import (
    TextAnalyticsClient,
    ExtractSummaryAction
)

endpoint = "AZURE_TEXT_ANALYTICS_ENDPOINT"
key = "AZURE_TEXT_ANALYTICS_KEY"

text_analytics_client = TextAnalyticsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key),
)

document = [
    text
]

poller = text_analytics_client.begin_analyze_actions(
    document,
    actions=[
        ExtractSummaryAction(),
    ],
)

document_results = poller.result()
for result in document_results:
    extract_summary_result = result[0]  # first document, first result
    if extract_summary_result.is_error:
        print("...Is an error with code '{}' and message '{}'".format(
            extract_summary_result.code, extract_summary_result.message
        ))
    else:
        print('\033[1m' + 'Summary extracted:' + '\033[0m' + "\n{}".format(
            " ".join([sentence.text for sentence in extract_summary_result.sentences]))
        )
summary = " ".join([sentence.text for sentence in extract_summary_result.sentences])


def selector(langCode):
	import requests, uuid, json

	credential2 = json.load(open('credential2.json'))
	subscription_key = credential2['API_KEY']
	endpoint = credential2['ENDPOINT']

	location = credential2['LOCATION']

	path = '/translate'
	constructed_url = endpoint + path

	params = {
		'api-version': '3.0',
		'from': 'en',
		'to': [langCode]
	}

	headers = {
		'Ocp-Apim-Subscription-Key': subscription_key,
		'Ocp-Apim-Subscription-Region': location,
		'Content-type': 'application/json',
		'X-ClientTraceId': str(uuid.uuid4())
	}

	body = [{
		'text': summary
	}]

	request = requests.post(constructed_url, params=params, headers=headers, json=body)
	response = request.json()
	print("\033[1m" + "Transated Summary:" + "\033[0m")
	print(response[0]['translations'][0]['text'])

	
selection = input("Do you want your summary to be translated? (Y/N)\n*Note: Input is case sensitive\n")
if selection == 'Y':
	language_select = input("Select your language:\nC for Chinese Simplified\nE for English\nF for French\nG for German\nH for Hindi\nS for Spanish\n")
	if language_select == 'C':
		selector('zh-Hans')  
	elif language_select == 'E':
		print(summary)
	elif language_select == 'F':
		selector('fr')	
	elif language_select == 'G':
		selector('de')	
	elif language_select == 'H':
		selector('hi')	
	elif language_select == 'S':
		selector('es')
	else: 
		print("Invalid Input")				
