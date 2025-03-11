pipeline {
    agent { 
        docker { 
            image 'node:22.14.0-alpine3.21' 
            args '--user root'  // Optional: Run as root inside the container
        } 
    }

    stages {
        stage('Build') {
            steps {
                echo 'Running inside a Docker container'
                sh 'node --version'
            }
        }
    }
}

