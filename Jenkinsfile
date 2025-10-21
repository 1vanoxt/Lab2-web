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
                sh 'docker-compose build'
            }
        }

        stage('Run Bandit Scan') {
            steps {
                sh 'bandit -r . || true'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest || true'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t lab2-web .'
            }
        }

        stage('Run Trivy Scan') {
            steps {
                sh 'trivy image lab2-web || true'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}
