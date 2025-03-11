node {
    stage('Build') {
        checkout scm
        docker.image('node:22.14.0-alpine3.21').inside {
            sh 'node --version'
        }
    }
}
