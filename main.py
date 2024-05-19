import os
import re
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from gradio_client import Client
from contextlib import asynccontextmanager

from Preprocess import preprocess_image
from Format import remove_nextlines

from google.cloud import vision
from PIL import Image
import cv2
import numpy as np

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'google-credentials.json'
class Message(BaseModel):
    content: str

class Param(BaseModel):
    file_path: str

client = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    global client
    client = Client("https://osanseviero-mistral-super-fast.hf.space/")
    with open("systemprompt.txt") as file:
        prompt = Message(content=file.read())

    result = client.predict(
        prompt.content,  # use the content attribute of the Message model
        0.9,  # int | float (numeric value between 0.0 and 1.0)
              # in 'Temperature' Slider component
        500,  # int | float (numeric value between 0 and 1048)
              # in 'Max new tokens' Slider component
        0.9,  # int | float (numeric value between 0.0 and 1)
              # in 'Top-p (nucleus sampling)' Slider component
        1.2,  # int | float (numeric value between 1.0 and 2.0)
              # in 'Repetition penalty' Slider component
        api_name="/chat"
    )
    print(result)
    
    yield
    client.clear()
    # Clean up the ML models and release the resources


app = FastAPI(lifespan=lifespan)

def detect_document(img_path):
    """Detects document features in an image."""

    client = vision.ImageAnnotatorClient()

    # Preprocess the image
    # img = Image.open(img_path)
    # preprocessed_img = preprocess_image(img)

    # # OCR using Google Cloud Vision API
    # client = vision.ImageAnnotatorClient()
    # content = cv2.imencode(".jpg", np.array(preprocessed_img))[1].tostring()
    # image = vision.Image(content=content)
    # response = client.document_text_detection(image=image)
    # detections = response.full_text_annotation
    # converted_text = detections.text

    with open(img_path, "rb") as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.document_text_detection(image=image)
    detections = response.full_text_annotation
    converted_text = detections.text

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )
    
    return converted_text

# for file path parameters
@app.post("/convert")
async def process_image(message: Param):
    image_filepath = message.file_path
    # Save the uploaded image
    image_path = f"{image_filepath}"
    # with open(image_path, "wb") as f:
    #     f.write(file.file.read())

    # Preprocess and OCR the image
    ocr_text = detect_document(image_path)

    # Format the text
    formatted_text = remove_nextlines(ocr_text)
    return {"text": formatted_text}

# for file upload paramater
# @app.post("/convert")
# async def process_image(file: UploadFile = File(...)):
#     # Save the uploaded image
#     image_path = f"essays/{file.filename}"
#     with open(image_path, "wb") as f:
#         f.write(file.file.read())

#     # Preprocess and OCR the image
#     ocr_text = detect_document(image_path)

#     # Format the text
#     formatted_text = remove_nextlines(ocr_text)
#     return {"text": formatted_text}

# @app.post("/evaluate")
# async def process_image(file: UploadFile = File(...)):
#     # Save the uploaded image
#     image_path = f"essays/{file.filename}"
#     with open(image_path, "wb") as f:
#         f.write(file.file.read())

#     # Preprocess and OCR the image
#     ocr_text = detect_document(image_path)

#     # Format the text
#     formatted_text = remove_nextlines(ocr_text)
#     # Use the formatted text as a prompt for NLP
#     result = client.predict(
#         formatted_text,
#         0.9,
#         500,
#         0.9,
#         1.2,
#         api_name="/chat"
#     )

#     return {"result": result[:-4], "text": ocr_text}

# @app.post("/convert")
# async def process_image(file: UploadFile = File(...)):
#     # Save the uploaded image
#     image_path = f"essays/{file.filename}"
#     with open(image_path, "wb") as f:
#         f.write(file.file.read())

#     # Preprocess and OCR the image
#     ocr_text = detect_document(image_path)

#     # Format the text
#     formatted_text = remove_nextlines(ocr_text)
#     return {"text": formatted_text}

# async def process_image(file_path: str = ""):
#     # Save the uploaded image
#     # Check if file path is provided
#     # if not file_path:
#     #     return {"error": "Missing file path"}

#     # Open the file and read its content
#     try:
#         with open(file_path, "rb") as f:
#             image_data = f.read()
#     except FileNotFoundError:
#         return {"error": "File not found"}

#     # Preprocess and OCR the image
#     ocr_text = detect_document(image_data)

#     # Format the text
#     formatted_text = remove_nextlines(ocr_text)
#     return {"text": formatted_text}

# @app.post("/chat")
# async def chat_endpoint(message: Message):
#     # Use the global client instance
#     result = client.predict(
#         message.content,  # use the content attribute of the Message model
#         0.9,  # int | float (numeric value between 0.0 and 1.0)
#               # in 'Temperature' Slider component
#         500,  # int | float (numeric value between 0 and 1048)
#               # in 'Max new tokens' Slider component
#         0.9,  # int | float (numeric value between 0.0 and 1)
#               # in 'Top-p (nucleus sampling)' Slider component
#         1.2,  # int | float (numeric value between 1.0 and 2.0)
#               # in 'Repetition penalty' Slider component
#         api_name="/chat"
#     )
#     return {"result": result[:-4]}
