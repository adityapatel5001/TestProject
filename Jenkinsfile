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
                sh 'python3 -m venv venv'
                sh 'venv/bin/pip install -r app/requirements.txt'
            }
        }

        stage('Syntax Check') {
            steps {
                sh 'venv/bin/python -m py_compile app/app.py'
            }
        }

        stage('Unit Tests') {
            steps {
                sh 'venv/bin/python -m pytest app/test_app.py'
            }
        }

    }
}