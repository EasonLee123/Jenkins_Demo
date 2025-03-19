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
                    docker.image('strategy_test:1.0').inside {
                        sh 'python Regression_test.py'
                    }
                }
            }
        }
    }
}
