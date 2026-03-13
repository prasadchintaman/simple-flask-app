@Library('my-shared-lib') _

pipeline {

    agent any

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('SonarQube Code Quality') {
            steps {
                sonarScan("flask-app")
            }
        }

        stage('Build Docker Image') {
            steps {
                buildDocker("flask-app")
            }
        }

        stage('Deploy Container') {
            steps {
                deployContainer("flask-container","flask-app")
            }
        }

    }
}
