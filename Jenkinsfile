pipeline {
    agent {
        docker { image 'python:3.9' }
    }

    stages {
        stage('Run Regression Test') {
            steps {
                script {
                    sh 'python Regression_test.py'
                }
            }
        }
    }
}
