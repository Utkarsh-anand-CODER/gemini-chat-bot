from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input_prompt, image):
    if input_prompt != "" and image:
        response = model.generate_content([input_prompt, image])
    elif image:
        response = model.generate_content(image)
    else:
        response = "Please upload an image or provide an input prompt."
    return response.text


st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Application")
input_prompt = st.text_input("Input Prompt:", key="input")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Tell me something")
if submit:
    response = get_gemini_response(input_prompt, image)
    st.subheader("The prompt is here")
    st.write(response)
