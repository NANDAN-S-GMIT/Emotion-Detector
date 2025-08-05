# 😄 Emotion Detector Web App 

A powerful, web-based **Emotion Detection** application built using **Flask** (Python) for the backend and **HTML/CSS/JavaScript** for the frontend. This project analyzes text input and predicts the underlying emotion using natural language processing (NLP) techniques or API-based models.

---

## 🔍 Overview

The Emotion Detector enables users to input text and get instant feedback about the emotional sentiment behind it. It can identify emotions like:

- 😀 Happy
- 😠 Angry
- 😨 Fear
- 🤢 Disgust
- 😢 Sad
- 😍 Love
- 😂 Amusement
- 😕 Confusion
- 😐 Neutral
- 
- [![View Live](https://img.shields.io/badge/View-Live%20App-blue?style=for-the-badge)](https://emotion-detector-mo89.onrender.com)



---

## 🎯 Features

- 🧠 Emotion analysis from user-provided text
- 🎨 Clean, responsive frontend UI with emoji-based buttons
- ⚙️ Backend powered by Flask and Python
- 🔁 JavaScript-powered asynchronous API interaction
- 🧪 Unit tested for reliability and robustness
- 🧰 Proper error handling and status code management
- 🧱 Structured packaging with `__init__.py`
- 🧼 Static code analysis with 10/10 Pylint score
- 🖥️ Fully responsive and mobile-friendly layout
- 🚀 Deployment-ready for platforms like Render or Heroku

---

## 🛠️ Tech Stack

| Layer      | Technology                  |
|------------|-----------------------------|
| Frontend   | HTML, CSS, JavaScript       |
| Backend    | Python, Flask, Gunicorn     |
| APIs/NLP   | Flask logic / Watson NLP    |
| Hosting    | GitHub, Render-ready        |


---

## 📁 Project Structure

```
Emotion-Detector/
├── app.py
├── server.py
├── emotion_detector/
│   ├── __init__.py
│   └── emotion_detection.py
├── tests/
│   └── test_emotion_detection.py
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── templates/
│   └── index.html
└── README.md
```

---

## 📸 Screenshots

> *(Below are visuals from the application in action. Each demonstrates functionality, design, and user interaction.)*

<br>

![Home Page](https://github.com/NANDAN-S-GMIT/Emotion-Detector/blob/main/EmotionDetector1.png?raw=true)

<br>

![Analyzing Page](https://github.com/NANDAN-S-GMIT/Emotion-Detector/blob/main/EmotionDetector2.png?raw=true)

<br>

![Detection Result](https://github.com/NANDAN-S-GMIT/Emotion-Detector/blob/main/EmotionDetector3.png?raw=true)

---

## 💻 Getting Started Locally

### 1. Clone the repository

```bash
git clone https://github.com/NANDAN-S-GMIT/Emotion-Detector.git
cd Emotion-Detector
```

### 2. Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

### 5. Visit in browser

```
http://localhost:5000
```

---

## 🌐 Deployment (Render Recommended)

To deploy this project on **Render**:

- Push the project to GitHub.
- Create a new Web Service on [Render](https://render.com/).
- Use the following settings:

| Field          | Value                          |
|----------------|-------------------------------|
| Build Command  | `pip install -r requirements.txt` |
| Start Command  | `Python Server.py`             |
| Runtime        | Python                         |

---

## 📦 Requirements

```
Flask
flask-cors
pylint
```
Add more packages as needed (e.g., `textblob`, `ibm-watson`, `unittest`, etc.)

---

## 📌 Sample Buttons in UI

```html
<button class="sample-btn" onclick="setEmotionTextAndAnalyze('I am very happy today!')">😀 Happy</button>
<button class="sample-btn" onclick="setEmotionTextAndAnalyze('This makes me angry.')">😠 Angry</button>
<button class="sample-btn" onclick="setEmotionTextAndAnalyze('It scares me a lot.')">😨 Fear</button>
<button class="sample-btn" onclick="setEmotionTextAndAnalyze('I feel so disgusted.')">🤢 Disgust</button>
<button class="sample-btn" onclick="setEmotionTextAndAnalyze('I am deeply sad.')">😢 Sad</button>
<button class="sample-btn" onclick="setEmotionTextAndAnalyze('I love this!')">😍 Love</button>
<button class="sample-btn" onclick="setEmotionTextAndAnalyze('It was hilarious!')">😂 Amusement</button>
<button class="sample-btn" onclick="setEmotionTextAndAnalyze('I am totally confused.')">😕 Confusion</button>
<button class="sample-btn" onclick="setEmotionTextAndAnalyze('I am just feeling okay.')">😐 Neutral</button>
```

---

## 🙋‍♂️ Author

**Nandan S**  
🔗 [LinkedIn](https://www.linkedin.com/in/nandans-devloper/)  
💻 Full Stack Developer | Python | AI Enthusiast  
📍 India

---

## ⭐️ Show Your Support

If you found this project useful or interesting:

- Give it a ⭐ on GitHub  
- Share it with others  
- Connect with me for collaboration

---


