# simple-flask-app
# Simple Flask Application

## Project Overview

This project is a simple Python Flask application created for learning and practicing DevOps workflows.

The project includes:
- Python Flask application
- Docker containerization
- Jenkins CI/CD pipeline integration
- Git version control workflow


## Applsimple-flask-app/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
├── README.md└── .gitignorei


## Prerequisites
Install required tools:
- Python 3
- Git
- Docker
- Jenkins


## Run Application Locally

Install dependencies:

```bash
pip install -r requirements.txt
Run Flask application:

python3 app.py

Application will start on:

http://localhost:80

Build Docker File
docker build -t simple-flask-app .
