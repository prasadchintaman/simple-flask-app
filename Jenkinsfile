@Library('my-shared-lib') _

pipeline {

agent any

stages {

stage('Checkout') {
steps {
git 'https://github.com/your-username/flask-app.git'
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
