pipeline {
    agent {
        docker {
            image 'node:22.14.0-alpine3.21'
        }
    }
    
    stages {
        stage('Build') {
            steps {
                echo 'Running inside Docker container'
                sh 'node --version'
            }
        }
    }
}
