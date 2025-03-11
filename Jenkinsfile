pipeline {
    agent any
    stages {
        stage('Install Node.js and npm') {
            steps {
                script {
                    // Install Node.js and npm
                    sh 'curl -sL https://deb.nodesource.com/setup_16.x | bash -'
                    sh 'apt-get install -y nodejs'  // For Linux-based agents, adjust for macOS if necessary
                }
            }
        }
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    sh 'npm install'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    def nodePath = "/usr/local/bin/node" // Update with actual path if necessary
                    if (isUnix()) {
                        sh "${nodePath} --eval 'console.log(process.arch, process.platform)'"
                        sh "npm test -- --reporter mocha-junit-reporter"  // Adjust for your test runner
                    } else {
                        bat "${nodePath} --eval 'console.log(process.arch, process.platform)'"
                        bat "npm test -- --reporter mocha-junit-reporter"  // Adjust for your test runner
                    }
                }
            }
        }
        stage('Record Test Results') {
            steps {
                junit '**/test-results/*.xml'  // Adjust the path to match your test report location
            }
        }
        stage('Store Artifacts') {
            steps {
                archiveArtifacts allowEmptyArchive: true, artifacts: '**/test-results/*.xml, **/logs/*.log', fingerprint: true
            }
        }
    }
    post {
        always {
            echo "Pipeline completed"
        }
        success {
            echo "Tests passed successfully!"
        }
        failure {
            echo "Tests failed. Please check the logs."
        }
    }
}
