# Project Name: Story Generator

## Motivation
As a parent, I want to provide my kid with a fun and engaging activity during the holidays, So that they can stay motivated to draw and be occupied.

This project is a Python application that allows users to upload a drawing, which is then processed to generate a story based on the image. The story is then converted into an audio file, and a new image is generated using AI. The application utilizes:

1. Streamlit for creating the web interface.
2. Azure Vision API for image captioning.
3. gTTs for text to audio.
4. OpenAI for generating the story.
5. DeepAI for generating a new image.

## Installation

1. Clone the repository: `git clone https://github.com/harmeetsokhi/story-generator.git`
2. `cd story-generator`
3. Install the required dependencies `Poetry install`
4. Set up the necessary credentials and API keys for Azure Vision API 4.0 , OpenAI, and DeepAI.  
6. Run the application: `poetry run streamlit run story_app.py`

## Configuration
Before running the application, make sure to set up the necessary configurations:

1. Setup following environment variables 

- `export VISION_ENDPOINT='YOUR_AZURE_VISION_API_END_PONIT with https'`

- `export VISION_ENDPOINT_2='YOUR_AZURE_VISION_API_END_PONIT without https and any /'`

- `export VISION_KEY='"YOUR_AZURE_VISION_API_KEY"'`

- `export OPEN_API_KEY='YOUR OPEN API KEY'`

## Usage

1. Once the application is running, you we  web browser will open with the app 
2. The web interface will be displayed, providing a file upload option.
3. Click on the "Upload File" button and select the kids drawing you want to process.
4. The application will send the image to Azure Vision API for image captioning, and retrieve the generated caption.
5. The caption is then used as a prompt for the OpenAI model to generate a story based on the image.
6. The generated story is converted into an audio file.
7. The DeepAI model is then utilized to create a new image based on the story.
8. The resulting story and image are displayed on the web interface.
9. Repeat the process to generate stories and images from different drawings.

## Acknowledgements

This project utilizes the following technologies:

- [Streamlit](https://www.streamlit.io/) - For creating the web application.
- [Azure Vision API](https://learn.microsoft.com/en-us/azure/cognitive-services/computer-vision/how-to/call-analyze-image-40?tabs=rest#select-the-image-to-analyze) - For image captioning.
- [OpenAI](https://platform.openai.com/account/api-keys/) - For generating the story.
- [DeepAI](https://deepai.org/) - For generating a new image.

## Contact

If you have any questions, suggestions, or feedback, please feel free to contact :
- Name: Harmeet Sokhi 
