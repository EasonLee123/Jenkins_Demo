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
                    image 'strategy_test:1.0'
                    reuseNode true
                }
            }
            steps {
                sh 'python Regression_test.py'
            }
        }
    }
}
