# 🧠 Productivity Predictor

This is a machine learning-powered web application that predicts productivity level based on lifestyle inputs like sleep hours, screen time, breaks, and more.

---

## 🚀 Tech Stack
- **Python**
- **Scikit-learn**
- **FastAPI**
- **Docker**
- **AWS EC2**
- **DockerHub**

---

## 📦 Features
- ML model (RandomForest) trained on realistic synthetic data  
- FastAPI backend with auto-generated docs at `/docs`  
- Dockerized for easy local and cloud deployment  
- Hosted on AWS EC2 using a DockerHub image

---

## 📁 Project Structure
.
├── app/
│ ├── main.py
│ └── predict.py
├── models/
│ └── RandomForest_model/model.pkl
├── Dockerfile
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## 🛠️ How to Run

### 🔧 Local
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
Open the API docs: http://127.0.0.1:8000/docs

🐳 Docker
bash
Copy
Edit
docker build -t productivity-app .
docker run -d -p 8000:8000 productivity-app
Open: http://localhost:8000/docs

☁️ AWS EC2 Deployment
bash
Copy
Edit
# Pull prebuilt image from DockerHub
docker pull muskang1711/productivity-app

# Run on EC2
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
GitHub: https://github.com/Muskang1711/productivity-predictor

📜 License
This project is licensed under the MIT License
