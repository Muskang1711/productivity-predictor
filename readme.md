# 🧠 Productivity Predictor

This is a machine learning-powered web application that predicts your productivity level based on lifestyle inputs like sleep hours, screen time, breaks, etc.

---

## 🚀 Tech Stack

- Python
- Scikit-learn
- FastAPI
- Docker
- AWS EC2
- DockerHub

---

## 📦 Features

- ML model (RandomForest) trained on realistic data
- FastAPI-based backend with auto-generated docs (`/docs`)
- Dockerized for easy deployment
- Hosted on AWS EC2 using DockerHub image

---

## 📁 Project Structure

.
├── app
│ ├── main.py
│ └── predict.py
├── models/
│ └── RandomForest_model/model.pkl
├── Dockerfile
├── requirements.txt
└── README.md

yaml
Copy code

---

## 🛠️ How to Run

### 🔧 Local

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
🐳 Docker
bash
Copy code
docker build -t productivity-app .
docker run -d -p 8000:8000 productivity-app
Then open: http://localhost:8000/docs

☁️ AWS EC2 Deployment
bash
Copy code
docker pull muskang1711/productivity-app
docker run -d -p 8000:8000 muskang1711/productivity-app
Visit: http://<your-ec2-ip>:8000/docs

📊 Input Features
Sleep hours

Screen time (daily)

Number of breaks

Exercise level

Stress level (1–10)

Focus time (hours/day)

📈 Output
Productivity Label: Low, Medium, or High

🙋‍♀️ Author
Muskan Goyal
DockerHub: muskang1711

yaml
Copy code

---
