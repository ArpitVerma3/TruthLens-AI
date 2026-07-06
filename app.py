import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import preprocess_input

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="TruthLens AI",
    page_icon="🤖",
    layout="centered"
)

# ----------------  CSS Attached ----------------

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.markdown("""
<div class="title">
🤖 TruthLens AI
</div>

<div class="subtitle">
Real vs AI Generated Image Detection
</div>
""", unsafe_allow_html=True)

# ---------------- STATS ----------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🧠 Model", "ResNet-50")

with col2:
    st.metric("📊 Accuracy", "80%")

with col3:
    st.metric("⚡ Framework", "TensorFlow")

# ---------------- PROJECT DESCRIPTION ----------------

with st.expander("📖 About Project"):
    st.write("""
This project uses a ResNet-50 based Convolutional Neural Network,
fine-tuned via transfer learning, to classify images as either
Real or AI Generated.
    """)

    st.markdown("""
| Features               | Technologies Used                  |
|------------------------|------------------------------------|
| Image Upload           | TensorFlow & Keras                 |
| Confidence Score       | ResNet-50 (Pretrained on ImageNet) |
| Deep Learning Class.   | Streamlit                          |
| Interactive UI         | Python                             |
    """)

# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.title("📌 Project Information")

    st.success("Deep Learning Project")

    st.write("🧠 ResNet-50 Model")
    st.write("📁 Upload Image Support")
    st.write("📊 Confidence Score")
    st.write("⚡ TensorFlow + Streamlit")

    st.markdown("---")

    st.info("""
    Detect whether an image is:

    ✅ Real Image

    🤖 AI Generated Image
    """)

# ---------------- LOAD MODEL ----------------

model = tf.keras.models.load_model("project.keras")

# ---------------- IMAGE UPLOAD ----------------

image = None

uploaded_file = st.file_uploader(
    "📁 Upload an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

# ---------------- PREDICTION ----------------

if image is not None:

    st.markdown(
        "<h3 class='preview-title'>🖼️ Image Preview</h3>",
        unsafe_allow_html=True
    )

    st.image(
        image,
        width=500
    )

    img = image.resize((200, 200))
    img_array = preprocess_input(np.array(img, dtype="float32"))
    img_array = np.expand_dims(img_array, axis=0)

    # Prediction
    prediction = model.predict(img_array)

    confidence = float(prediction[0][0])

    st.markdown("---")

    if confidence > 0.5:

        st.markdown(f"""
        <div class='result-box result-real'>
        <h2>✅ REAL IMAGE DETECTED</h2>
        <h4>Confidence: {confidence*100:.2f}%</h4>
        </div>
        """, unsafe_allow_html=True)

        st.progress(int(confidence * 100))

    else:

        ai_conf = 1 - confidence

        st.markdown(f"""
        <div class='result-box result-ai'>
        <h2>🤖 AI GENERATED IMAGE DETECTED</h2>
        <h4>Confidence: {ai_conf*100:.2f}%</h4>
        </div>
        """, unsafe_allow_html=True)

        st.progress(int(ai_conf * 100))

# ---------------- FOOTER ----------------

st.markdown("---")

st.markdown("""
<div class="footer">
🚀 Developed by Group 3<br>
Galgotias College of Engineering and Technology <br>
Deep Learning Project 2026
</div>
""", unsafe_allow_html=True)
