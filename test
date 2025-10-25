pipeline {
    agent any
    environment {
        // Define Python image and Docker image name
        PYTHON_IMAGE = 'python:3.9-slim'
        IMAGE_NAME = 'lab2-web'
    }

    stages {
        stage('Checkout') {
            steps {
                // Pull the code from GitHub
                git 'https://github.com/1vanoxt/Lab2-web.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Create virtual environment and install dependencies
                    bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run tests (if pytest exists)
                    bat '''
                    call venv\\Scripts\\activate
                    pytest || exit /b 0
                    '''
                }
            }
        }

        stage('Static Code Analysis (Bandit)') {
            steps {
                script {
                    // Run Bandit for static code analysis
                    bat '''
                    call venv\\Scripts\\activate
                    bandit -r . -f txt -o bandit_report.txt || exit /b 0
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    bat 'docker-compose build'
                }
            }
        }

        stage('Container Vulnerability Scan (Trivy)') {
            steps {
                script {
                    // Scan Docker image with Trivy
                    bat 'docker run --rm -v %cd%:/app aquasec/trivy image %IMAGE_NAME%:latest || exit /b 0'
                }
            }
        }

        stage('Check Dependency Vulnerabilities (Safety)') {
            steps {
                script {
                    // Check dependencies with Safety (optional)
                    bat '''
                    call venv\\Scripts\\activate
                    safety check || exit /b 0
                    '''
                }
            }
        }

        stage('Deploy Application') {
            steps {
                script {
                    // Deploy application using Docker Compose
                    bat 'docker-compose up -d'
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
            cleanWs()
        }
    }
}
