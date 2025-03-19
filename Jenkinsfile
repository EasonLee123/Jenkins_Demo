pipeline {
    agent any
    stages {
        stage('Docker ready') {
            steps {
                sh 'echo HELLO'
            }
        }
        stage('Run Regression Test') {
            steps {
                script {
                    docker.image('python:3.9').inside {
                        sh 'python Regression_test.py'
                    }
                }
            }
        }
    }
}
