pipeline {
    agent any  // Runs on any available agent

    stages {
        stage('Build') {
            steps {
                echo 'Starting the build process...'
                sh 'echo "Compiling source code..."'
                sh 'echo "Build completed successfully!"'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'echo "Executing unit tests..."'
                sh 'echo "All tests passed!"'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh 'echo "Deploying to staging environment..."'
                sh 'echo "Deployment successful!"'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up workspace...'
            sh 'echo "Performing cleanup tasks..."'
        }
        success {
            echo 'Pipeline execution completed successfully!'
        }
        failure {
            echo 'Pipeline failed! Check the logs for more details.'
        }
    }
}
