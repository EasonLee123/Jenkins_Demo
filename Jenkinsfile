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
                    args '-v /var/jenkins_home/workspace/Eason_Regression_test:/var/jenkins_home/workspace/Eason_Regression_test'
                    reuseNode true
                }
            }
            steps {
                    sh 'python /var/jenkins_home/workspace/Eason_Regression_test/Regression_test.py'
            }
        }
    }
    post
    always{
        cleanWs()
    }
}
