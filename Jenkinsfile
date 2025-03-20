pipeline {
    agent any
    stages {
        stage('Start Test') {
            steps {
                sh 'echo HELLO'
            }
        }
        stage('Run Regression Test') {
            agent {
                docker {
                    image 'akroneason123/strategy_test:2.0'
                    args '-v /var/jenkins_home/workspace:/var/jenkins_home/workspace'
                    reuseNode true
                }
            }
            steps {
                script {
                    docker.image('akroneason123/strategy_test:2.0').inside('-v /var/jenkins_home/workspace') {
                        sh 'python Regression_test.py'
                    }
                }
            }
        }
    }
}
