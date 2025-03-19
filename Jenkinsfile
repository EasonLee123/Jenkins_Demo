pipeline {
    agent any
    stages {
        stage('Install Python') {
            steps {
                sh 'apt-get update && sudo apt-get install -y python3'
            }
        }
        stage('Run Regression Test') {
            steps {
                sh 'python3 Regression_test.py'
            }
        }
    }
}
