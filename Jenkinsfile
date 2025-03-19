pipeline {
    agent any
    environment {
        docker-credentials-id = 'c9d32ed1-8ccc-4cff-9c36-057e632825e4'
        DOCKER_USERNAME = 'akroneason123'
        DOCKER_PASSWORD = 'EasonLee123!'
    }
    stages {
        stage('Docker ready') {
            steps {
             sh 'echo HELLO'               
            }
        }
        stage('Run Regression Test') {
            agent {
                docker {
                    image 'strategy_test:1.0'
                    reuseNode true
                }
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-credentials-id', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                }
                sh 'python Regression_test.py'
            }
        }
    }
}
