# hypermarket-mlops-pipeline

Project Architecture

Data Versioning → DVC manages datasets (sales.csv + CCTV images).

Pipeline Orchestration → Defined in dvc.yaml (preprocessing → training → evaluation → deployment).

Experiment Tracking → MLflow tracks model performance & parameters.

Model Deployment → FastAPI serves trained models as REST APIs.

Containerization → Docker for portability.

CI/CD → GitHub Actions automates retraining & redeployment.

 Repo Structure
hypermarket-mlops-pipeline/
├── data/
│   ├── sales.csv
│   └── images/
├── notebooks/
│   └── eda.ipynb
├── src/
│   ├── data_preprocess.py
│   ├── train.py
│   └── predict.py
├── dvc.yaml
├── app.py
├── Dockerfile
├── requirements.txt
└── .github/workflows/ci-cd.yml

⚙️ Tech Stack

Languages: Python

ML Frameworks: scikit-learn, PyTorch (optional)

MLOps Tools: DVC, MLflow

Deployment: FastAPI, Docker, GitHub Actions (CI/CD)

Cloud Ready: AWS/GCP/Azure (can be plugged in)

▶️ How to Run

Clone repo:

git clone https://github.com/yourusername/hypermarket-mlops-pipeline.git
cd hypermarket-mlops-pipeline


Install dependencies:

pip install -r requirements.txt


Run DVC pipeline:

dvc repro


Serve API locally:

uvicorn app:app --reload


Test endpoint:

curl "http://127.0.0.1:8000/predict?day=10"

Results 

Sales Forecasting Model → MSE = 150.3

Theft Detection Model → Placeholder (YOLOv8 can be integrated).

Author

Mian Yahya – MLOps Engineer
