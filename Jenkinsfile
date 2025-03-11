pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                script {
                    def nodePath = "/usr/local/bin/node" // Update with actual path
                    if (isUnix()) {
                        sh "${nodePath} --eval 'console.log(process.arch, process.platform)'"
                    } else {
                        bat "${nodePath} --eval 'console.log(process.arch, process.platform)'"
                    }
                }
            }
        }
    }
}
