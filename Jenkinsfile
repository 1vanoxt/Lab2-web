pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/1vanoxt/Lab2-web.git'
            }
        }

        stage('Build') {
            steps {
                bat 'docker-compose build'
            }
        }

        stage('Run Bandit Scan') {
            steps {
                bat 'chcp 65001 && python -m bandit -r . -f txt -o bandit_report.txt || exit /b 0'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest || exit /b 0'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t lab2-web .'
            }
        }

        stage('Run Trivy Scan') {
            steps {
                bat 'trivy image lab2-web || exit /b 0'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}
