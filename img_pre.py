import streamlit as st
from PIL import Image
from ultralytics import YOLO
import io
import json

# Set Streamlit page configuration
st.set_page_config(page_title="YOLOv8 Object Detection App", layout="wide")

st.title("YOLOv8 Object Detection with Streamlit")
st.write("Upload an image to perform object detection using a YOLOv8 nano model.")

# Load a pre-trained YOLOv8 nano model
@st.cache_resource
def load_model():
    model = YOLO('yolov8n.pt')  # You can choose other YOLOv8 models like 'yolov8s.pt', 'yolov8m.pt', etc.
    return model

model = load_model()

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("Running object detection...")

    # Perform inference
    results = model(image)

    # Plot results on the image
    for r in results:
        im_array = r.plot()  # plot a BGR numpy array of predictions
        # Convert BGR to RGB for PIL and Streamlit
        im_array = im_array[..., ::-1] 
        res_image = Image.fromarray(im_array)
        
    st.image(res_image, caption='Image with Detections', use_column_width=True)
    st.success("Detection complete!")

    # Optionally, display raw results
    with st.expander("View Raw Detection Results"):
        for r in results:
            st.code(r.to_json(), language="json")
else:
    st.info("Please upload an image to start detection.")
