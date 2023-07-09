# Project Name: Story Generator

This project is a Python application that allows users to upload a drawing, which is then processed to generate a story based on the image. The story is then converted into an audio file, and a new image is generated using AI. The application utilizes 
    1. Poetry for package mangement.
    2. Streamlit for creating the web interface, 
    3. Azure Vision API for image captioning, 
    4. gTTs for text to audio
    5. OpenAI for generating the story, and 
    6. DreamAI for generating a new image.

## Installation

1. Clone the repository: git clone https://github.com/your-username/story-generator.git
2. cd story-generator:Install the required dependencies: 
3. Set up the necessary credentials and API keys for Azure Vision API, OpenAI, and DreamAI. Instructions for obtaining the keys can be found in the respective documentation.
4. Poetry install
5. Run the application: streamlit run story_app.py


## Usage

1. Once the application is running, you we  web browser will open with the app 

2. The web interface will be displayed, providing a file upload option.

3. Click on the "Upload File" button and select the kids drawing you want to process.

4. The application will send the image to Azure Vision API for image captioning, and retrieve the generated caption.

5. The caption is then used as a prompt for the OpenAI model to generate a story based on the image.

6. The generated story is converted into an audio file.

7. The DreamAI model is then utilized to create a new image based on the story.

8. The resulting story and image are displayed on the web interface.

9. Repeat the process to generate stories and images from different drawings.

## Configuration

Before running the application, make sure to set up the necessary configurations:

1. setup following environment variables 

azure_vision_api_key = "YOUR_AZURE_VISION_API_KEY"
openai_api_key = "YOUR_OPENAI_API_KEY"
dreamai_api_key = "YOUR_DREAMAI_API_KEY"
`export VISION_ENDPOINT='"YOUR_AZURE_VISION_API_END_PONIT with https"'
`export VISION_ENDPOINT_2='YOUR_AZURE_VISION_API_END_PONIT without https and any /'
`export VISION_KEY='"YOUR_AZURE_VISION_API_KEY"'
`export OPEN_API_KEY='YOUR OPEN API KEY'
 
## Acknowledgements

This project utilizes the following technologies:

- [Streamlit](https://www.streamlit.io/) - For creating the web application.
- [Azure Vision API](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/) - For image captioning.
- [OpenAI](https://openai.com/) - For generating the story.
- [DreamAI](https://dream-ai.io/) - For generating a new image.

## Contact

If you have any questions, suggestions, or feedback, please feel free to contact :
- Name: Harmeet Sokhi 

 


