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
                sh 'python -m py_compile *.py'
            }
        }

        stage('Unit Tests') {
            steps {
                 sh 'python3 -m pytest app/test_app.py'
            }
        }

    }
}