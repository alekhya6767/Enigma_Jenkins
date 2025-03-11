pipeline {
    agent any  // Use any available agent instead of Docker
    stages {
        stage('Test') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'node --eval "console.log(process.arch, process.platform)"'
                    } else {
                        bat 'node --eval "console.log(process.arch, process.platform)"'
                    }
                }
            }
        }
    }
}
