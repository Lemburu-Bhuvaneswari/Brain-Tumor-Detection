# Brain-Tumor-Detection
A deep learning-based Brain Tumor Detection web application built using TensorFlow, Keras, CNN, Flask, and OpenCV to classify MRI brain scans into four categories: Glioma, Meningioma, Pituitary Tumor, and No Tumor.

🧠 Brain Tumor Detection Using Deep Learning (CNN)

A deep learning-based web application that detects and classifies brain tumors from MRI images using Convolutional Neural Networks (CNN). The application is built with **TensorFlow**, **Keras**, and **Flask**, providing an easy-to-use interface for uploading MRI scans and receiving real-time predictions.

📌 Features

- Upload MRI brain scan images
- Detect brain tumors using a trained CNN model
- Classifies MRI images into four categories:
  - Glioma
  - Meningioma
  - Pituitary Tumor
  - No Tumor
- Simple and responsive web interface
- Real-time prediction results



🛠️ Technologies Used

- Python
- TensorFlow
- Keras
- Flask
- OpenCV
- NumPy
- Matplotlib
- HTML
- CSS



📂 Project Structure


BrainTumorDetection/
│
├── app.py
├── train.py
├── predict.py
├── utils.py
├── requirements.txt
├── labels.txt
├── README.md
├── .gitignore
│
├── dataset/
│   ├── Training/
│   └── Testing/
│
├── models/
│   └── brain_tumor_model.h5
│
├── static/
├── templates/
└── uploads/


🧠 Model

The model is developed using a Convolutional Neural Network (CNN) trained on MRI brain scan images.

Classes

- Glioma
- Meningioma
- Pituitary
- No Tumor


📸 Sample Workflow

1. Open the application.
2. Upload an MRI image.
3. Click **Predict**.
4. View the predicted tumor type.

📈 Future Improvements

- Prediction confidence percentage
- Improved CNN architecture
- Transfer Learning (EfficientNet/MobileNet)
- Confusion Matrix
- Classification Report
- Model performance visualization
- Cloud Deployment
- Docker Support

👩‍💻 Author

Lemburu Bhuvaneswari

📄 License

This project is intended for educational and research purposes only.


