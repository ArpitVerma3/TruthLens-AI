# 🤖 TruthLens AI — Real vs AI Generated Image Detection

A Deep Learning project that classifies images as **Real** or **AI Generated** using a **ResNet-50** based Convolutional Neural Network with transfer learning. This project includes an interactive **Streamlit** web application that allows users to upload an image for real-time prediction with a confidence score.

---

# 📌 Project Overview

The rapid advancement of Artificial Intelligence has made it easier to generate realistic images. This project aims to identify whether an image is **Real** or **AI Generated** using Deep Learning techniques.

A **ResNet-50** model, pretrained on ImageNet and fine-tuned via transfer learning, is trained on a dataset containing both Real and AI Generated images. The trained model is then integrated into a Streamlit web application for fast, accurate, and user-friendly predictions.

---

# ✨ Features

- 📁 Image Upload Support
- 🤖 ResNet-50 Based Image Classification (Transfer Learning)
- ⚡ Real-Time Prediction
- 📊 Confidence Score Display
- 🎨 User-Friendly Streamlit Interface

---

# 🛠 Technologies Used

- Python
- TensorFlow
- Keras
- ResNet-50 (Pretrained on ImageNet)
- Streamlit
- NumPy
- Pillow

---

# 📂 Project Structure

```text
Real_vs_AI_Generated_Image_Detection/
│
├── app.py
├── Implimentation.ipynb
├── project.keras
├── requirements.txt
├── README.md
├── styles.css
├── sample.png
└── dataset/
```

---

# ⚙️ How the Project Works

### Step 1: Dataset Collection
Collect a dataset containing both **Real** and **AI Generated** images, organized into two class folders.

### Step 2: Data Preprocessing
Resize all images to **150 × 150 pixels** and apply ResNet-50's preprocessing (with augmentation such as rotation, zoom, and horizontal flip) for efficient model training.

### Step 3: Model Development
Load **ResNet-50** pretrained on ImageNet (excluding its original classifier head), freeze its base layers, and attach a custom classification head (Global Average Pooling, Dense, Dropout, Dense) for binary classification.

### Step 4: Model Training
Train the custom classification head on the prepared dataset to learn the visual features that distinguish Real from AI Generated images.

### Step 5: Model Evaluation
Evaluate the trained model using validation data to measure its accuracy and performance.

### Step 6: Model Saving
Save the trained model as:

```text
project.keras
```

### Step 7: Streamlit Web Application
Develop an interactive web application using **Streamlit**.

### Step 8: Image Input
Users can upload an image (JPG or PNG) through the web interface.

### Step 9: Image Prediction
The trained ResNet-50 model analyzes the input image and predicts whether it is:

- ✅ Real Image
- 🤖 AI Generated Image

### Step 10: Result Display
Display the prediction along with the confidence score using an attractive and user-friendly interface.

---

# 🚀 Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

# 📊 Applications

- Fake Image Detection
- AI Image Verification
- Media Authentication
- Cyber Security
- Social Media Content Verification
- Educational Projects

---

# ✅ Advantages

- Transfer Learning for Higher Accuracy with Less Data
- Fast and Real-Time Detection
- Simple Image Upload Interface
- Deep Learning-Based Solution

---

# 🔮 Future Improvements

- Improve Model Accuracy Through Fine-Tuning ResNet-50 Layers
- Camera-Based Image Capture Support
- Mobile Application Development
- Cloud Deployment
- Multi-Class Image Classification

---

# 👨‍💻 Developers

Arpit Verma,
Anurag Yadav,
Ajeet Singh,
Arslaan

Galgotias College of Engineering and Technology

---

# ⭐ Support

If you found this project useful, please **⭐ Star this repository** and share your feedback.