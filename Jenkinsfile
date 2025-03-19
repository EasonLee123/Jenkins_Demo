pipeline {
    agent any

    stages {
        stage('Run Regression Test') {
            steps {
                script {
                    sh 'python --version'
                    sh 'python Regression_test.py'
                }
            }
        }
    }
}
