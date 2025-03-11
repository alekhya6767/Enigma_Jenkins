pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    // Install dependencies using npm (or yarn, if preferred)
                    sh 'npm install'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    def nodePath = "/usr/local/bin/node" // Update with actual path
                    if (isUnix()) {
                        // Run the test command and output results to a file
                        sh "${nodePath} --eval 'console.log(process.arch, process.platform)'"
                        sh "npm test -- --reporter mocha-junit-reporter"  // Adjust for your test runner (e.g., Mocha)
                    } else {
                        bat "${nodePath} --eval 'console.log(process.arch, process.platform)'"
                        bat "npm test -- --reporter mocha-junit-reporter"  // Adjust for your test runner
                    }
                }
            }
        }
        stage('Record Test Results') {
            steps {
                // Record JUnit test results (ensure this is the correct path to your test reports)
                junit '**/test-results/*.xml'  // Adjust the path to match your test report location
            }
        }
        stage('Store Artifacts') {
            steps {
                // Archive build artifacts like logs, test results, etc.
                archiveArtifacts allowEmptyArchive: true, artifacts: '**/test-results/*.xml, **/logs/*.log', fingerprint: true
            }
        }
    }
    post {
        always {
            // Archive any additional logs or artifacts if needed
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
