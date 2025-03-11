pipeline {
    agent {
        docker {
            image 'python:3.13.2-alpine3.21'
        }
    }
    stages {
        stage('Build') {
            steps {
                echo 'Running inside Docker!'
                sh 'python --version'
            }
        }
    }
}
