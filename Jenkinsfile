pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Mengambil source code...'
                checkout scm
            }
        }

        stage('Test') {
            steps {
                echo 'Menjalankan test...'

                sh '''
                    python3 -m venv .venv
                    .venv/bin/pip install -r requirements.txt
                    .venv/bin/pytest
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Build Docker image...'

                sh '''
                    docker build \
                        -t jenkins-demo:${BUILD_NUMBER} .
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Menjalankan container...'

                sh '''
                    docker rm -f jenkins-demo || true

                    docker run -d \
                        --name jenkins-demo \
                        -p 5000:5000 \
                        -e BUILD_NUMBER=${BUILD_NUMBER} \
                        jenkins-demo:${BUILD_NUMBER}
                '''
            }
        }
    }
}