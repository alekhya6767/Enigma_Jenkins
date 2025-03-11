pipeline {
    agent any
    
    environment {
        ARTIFACTS_DIR = "artifacts" // Directory to store the artifacts
        TEST_RESULTS = "test-results" // Directory to store test results
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the source code from your Git repository
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install dependencies if needed
                // For example, using npm for a Node.js project
                sh 'npm install'
            }
        }

        stage('Run Tests') {
            steps {
                // Run the tests using a test framework (e.g., npm test, pytest)
                // Adjust this command based on your project
                sh 'npm test'
            }
        }

        stage('Record Test Results') {
            steps {
                // Archive the test results (assuming the test framework generates results in a file)
                // For example, if you are using a framework like Mocha with a reporter generating results in "test-results/*.xml"
                junit '**/test-results/*.xml' // Adjust the path as needed
            }
        }

        stage('Store Artifacts') {
            steps {
                // Archive the artifacts (e.g., logs, reports, or any files you want to preserve)
                // Example: storing log files or generated reports
                archiveArtifacts artifacts: '**/build/*.log, **/test-reports/**/*.html', allowEmptyArchive: true
            }
        }
        
        stage('Deploy') {
            steps {
                // Example deploy step, you can customize it for your project
                echo 'Deploying application...'
            }
        }
    }

    post {
        always {
            // Clean up any temporary resources or steps to be executed after the pipeline
            echo 'Cleaning up...'
        }
        success {
            // Actions to take on successful execution of the pipeline
            echo 'Pipeline succeeded!'
        }
        failure {
            // Actions to take if the pipeline fails
            echo 'Pipeline failed. Check logs and test results.'
        }
    }
}
