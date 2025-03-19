pipeline {
    agent any
    stages {
        stage('Docker ready') {
            steps {
             sh 'echo HELLO'               
            }
        }
        stage('Run Regression Test') {
            agent {
                docker {
                    image 'python:3.9'
                    reuseNode true
                }
            }
            steps {
                sh 'python Regression_test.py'
            }
        }
    }
}
