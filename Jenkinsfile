#!groovy
pipeline {
    agent {
        label "MyRunner"
    }

    stages {
        stage('Build') {
            steps {
                script {
                    sh "docker rm --force container"
                    echo "----------------------- Build Started -----------------------"
                    sh "docker build -t app -f python/Dockerfile ."
                    echo "----------------------------------------------"
                    echo "Build Number: ${env.BUILD_NUMBER}"
                    echo "----------------------- Build Finished -----------------------"
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo "----------------------- Test Started -----------------------"

                    def result = sh(script: 'grep "Hello" python/app.py | wc -l', returnStdout: true).trim()
                    echo result
                    if (result == "1") {
                        echo "Test Passed"
                    }
                    else {
                        echo "Test Failed"
                        exit 1
                    }
                    echo "----------------------- Test Finished -----------------------"
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    echo "----------------------- Deploy Started -----------------------"
                    sh 'docker run -d -p 8888:80 --name container app'
                    sh 'docker logs container'
                    echo "----------------------- Deploy Finished -----------------------"
                }
            }
        }
    }
}
