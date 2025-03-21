// pipeline {
//     agent any
//     stages {
//         stage('Start Test') {
//             steps {
//                 sh 'echo HELLO'
//             }
//         }
//         stage('Run Regression Test') {
//             agent {
//                 docker {
//                     image 'akroneason123/strategy_test:2.0'
//                     args '-v /var/jenkins_home/workspace/Eason_Regression_test:/var/jenkins_home/workspace/Eason_Regression_test'
//                     reuseNode false
//                 }
//             }
//             steps {
//                     sh 'python /var/jenkins_home/workspace/Eason_Regression_test/Regression_test.py'
//             }
//         }
//     }
//         post{
//             always{
//                 cleanWs()
//             }
//         }
// }
pipeline {
    agent any
    environment {
        DOCKER_CLIENT_TIMEOUT = '300'
        COMPOSE_HTTP_TIMEOUT = '300'
    }
    stages {
        stage('Start Test') {
            steps {
                sh 'echo HELLO'
            }
        }
        stage('Run Regression Test') {
            steps {
                script {
                    // Define the Docker command
                    def dockerCommand = "docker run --rm -i akroneason123/strategy_test:2.0"

                    // Read the input JSON
                    def inputJson = readFile file: 'input_file/testcase_001.json'

                    // Run the Docker command and capture the output
                    def dockerOutput = sh(script: "${dockerCommand} <<EOF\n${inputJson}\nEOF", returnStdout: true).trim()

                    // Write the Docker output to a file
                    writeFile file: 'docker_output.json', text: dockerOutput

                    // Run the Python script to process the Docker output
                    // sh 'python /var/jenkins_home/workspace/Eason_Regression_test/Regression_test.py'
                    sh 'docker run --rm -v $(pwd):/workspace -w /workspace python:3.9 python /workspace/Regression_test.py'
                }
            }
        }
    }
        post{
            always{
                cleanWs()
            }
        }
}
