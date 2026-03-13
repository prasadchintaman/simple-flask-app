@Library('my-shared-lib') _

pipeline {

    agent any

    environment {
        IMAGE_NAME = "flask-app"
        IMAGE_TAG  = "${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('SonarQube Code Quality') {
            steps {
                sonarScan("${IMAGE_NAME}")
            }
        }

        stage('Build & Push Docker Image') {
            steps {
                buildDocker("${IMAGE_NAME}:${IMAGE_TAG}")
            }
        }

        stage('Deploy Container') {
            steps {
                deployContainer("flask-container","${IMAGE_NAME}:${IMAGE_TAG}")
            }
        }

    }
}
