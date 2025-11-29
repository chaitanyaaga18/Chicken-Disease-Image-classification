import streamlit as st
import numpy as np
from PIL import Image
from cnnClassifier.pipeline.predict import PredictionPipeline

st.set_page_config(page_title="Chicken Disease Classification", layout="wide")
st.set_option('client.showErrorDetails', True)

st.title("🐔 Chicken Disease Classification")
st.write("Upload an image of a chicken and the model will predict the disease.")

uploaded_file = st.file_uploader("Upload Chicken Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", width=300)

    # Save temp image
    image.save("inputImage.jpg")
    st.success("Image uploaded successfully!")

    if st.button("Predict Disease"):
        predictor = PredictionPipeline("inputImage.jpg")
        result = predictor.predict()

        st.subheader("🔍 Prediction Result")
        st.json(result)
