pipeline {
    agent { label 'docker-agent' }

    stages {
        stage('Build') {
            steps {
                echo 'Running on a Docker-supported agent'
                sh 'node --version'
            }
        }
    }
}

