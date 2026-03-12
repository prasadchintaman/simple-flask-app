@Library('my-shared-lib') _

pipeline {

    agent any

    stages {

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
