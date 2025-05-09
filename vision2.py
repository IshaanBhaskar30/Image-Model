import streamlit as st
import google.generativeai as genai
from PIL import Image

# Streamlit app config
st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini Image Application")

# Sidebar input for API Key
api_key = st.sidebar.text_input("Enter your Google API Key", type="password")

# Input prompt
input_prompt = st.text_input("Input Prompt:", key="input")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

# Submit button
submit = st.button("Tell me about the image")

# Function to get Gemini response
def get_gemini_response(api_key, input_text, image_obj):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    if input_text:
        response = model.generate_content([input_text, image_obj])
    else:
        response = model.generate_content(image_obj)
    return response.text

# Handle submit
if submit:
    if not api_key:
        st.error("Please enter your Google API key in the sidebar.")
    elif not image:
        st.warning("Please upload an image.")
    else:
        response = get_gemini_response(api_key, input_prompt, image)
        st.subheader("The Response is")
        st.write(response)
