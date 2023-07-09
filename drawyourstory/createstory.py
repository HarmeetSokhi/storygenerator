
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

import subprocess
from array import array
import os
from PIL import Image
import openai  
from gtts import gTTS
import requests
from io import BytesIO
import http.client, urllib.request, urllib.parse, urllib.error, base64
import ast

# this is old version (3.2) 
def caption_image(image_path,st):
    subscription_key = os.environ["VISION_KEY"]
    endpoint = os.environ["VISION_ENDPOINT"]  
    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
    image_file=open(image_path,"rb")
    caption_results = computervision_client.describe_image_in_stream(image_file) 
    captions=[]
    print("Caption in the remote image: ")
    if (len(caption_results.captions[0].text) == 0):
        st.write("Unable to caption this")
    else:
        for tag in caption_results.captions:
            captions.append(tag.text)
            print("'{}' with confidence {:.2f}%".format(tag.text, tag.confidence * 100))
    return captions

#This is to use azure vision api preview.This gives better caption than the 3.2 viersion
def caption_image_curl(image_path,st):
    subscription_key = os.environ["VISION_KEY"]
    endpoint = os.environ["VISION_ENDPOINT"] 
    with open(image_path, 'rb') as f:
        body = f.read()
    headers = {
        # Request headers
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': f'{subscription_key}',
    }
    

    params = urllib.parse.urlencode({
        # Request parameters
        'features': 'caption',
        #'model-name': '{string}',
        'language': 'en',
        #'smartcrops-aspect-ratios': '{string}',
        'gender-neutral-caption': 'False',
    })

    try:
        conn = http.client.HTTPSConnection(os.environ["VISION_ENDPOINT_2"] )
        conn.request("POST", "/computervision/imageanalysis:analyze?api-version=2023-02-01-preview&%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close() 
        captions =[]
        if response.status  == 200 or response.status ==201:
            print(data)
            dict_str = data.decode("UTF-8")
            mydata = ast.literal_eval(dict_str)
            captions.append(mydata['captionResult']['text'])
            return captions
    except Exception as e:
        print(e)

def format_caption(caption,st,col1):
    formatted_captions=[]
    for text in caption:
        trimmed_text = text.replace("a drawing of", "", 1)  # Replace the phrase with an empty string, limiting it to one occurrence
        trimmed_text = trimmed_text.replace("drawing of", "", 1)  # Replace the phrase with an empty string, limiting it to one occurrence
        trimmed_text = trimmed_text.strip()  # Remove any leading or trailing whitespace
        formatted_captions.append(trimmed_text)
    return formatted_captions

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

#OpenAI
def generate_story(text,st,col2):
    api_key = os.environ["OPEN_API_KEY"] 
    openai.api_key  = api_key 
    prompt= f""" Write a very short moral story with the following characters:"
    {text} """ 
    response = get_completion(prompt)
    with col2:
        st.header(text[0].title())
        st.write(response)
        story_file_name = f'{text[0].title()}.txt'
        with open(story_file_name, 'w') as f:
            f.write(response) 
    return response,story_file_name

def convert_text_to_speech(text,caption,st,col3):
    language = 'en' #english
    speech = gTTS(text = text, lang = language, slow = False)
    story_audio = f'{caption}.wav'
    speech.save(story_audio) # this will save the format 
    with col3:
        st.header("Play the story") 
        st.audio(story_audio) 

#https://deepai.org/machine-learning-model/text2img
def generate_another_image(caption,st,col3):
    r = requests.post(
        "https://api.deepai.org/api/text2img",
        data={
            'text': f'{caption[0]}',
        },
        headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
    )
    print(r.json())
    
    image_url =  r.json()['output_url'] 
    
    if image_url:
        response = requests.get(image_url)
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            with col3:
                st.image(image)
        else:
            st.error("Error loading image from the provided URL")

def create_story_from_image(image_path,st,col1,col2,col3): 
    try:
        #captions=caption_image(image_path,st )
        captions=caption_image_curl(image_path,st )
        formatted_caption_list=format_caption(captions,st,col1)
        story,story_file_name =generate_story(formatted_caption_list,st,col2)
        convert_text_to_speech(story,story_file_name,st,col3)
        generate_another_image(formatted_caption_list,st,col3)
    except Exception as e:
        print (e)
