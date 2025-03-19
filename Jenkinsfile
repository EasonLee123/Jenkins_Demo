pipeline {
    agent {
        docker { image 'python:3.8' }
    }
    stages {
        stage('Run Regression Test') {
            steps {
                sh 'python Regression_test.py'
            }
        }
    }
}
