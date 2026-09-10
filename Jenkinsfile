pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'pip install -r app/requirements.txt'
            }
        }

        stage('Syntax Check') {
            steps {
                // your command
            }
        }

        stage('Unit Tests') {
            steps {
                sh 'pytest app/test_app.py'
            }
        }

    }
}