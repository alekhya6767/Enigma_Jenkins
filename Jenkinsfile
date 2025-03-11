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
                sh 'pip install -r requirements.txt' // If you have a requirements.txt file
                // Or use the pip install command for `unittest-xml-reporting` explicitly
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python test_sum.py'
            }
        }

        stage('Record Test Results') {
            steps {
                junit '**/test-reports/test_results.xml' // Point to the location of the generated JUnit XML
            }
        }

        stage('Store Artifacts') {
            steps {
                archiveArtifacts artifacts: '**/test-reports/test_results.xml', allowEmptyArchive: true
            }
        }
    }
    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed. Check logs and test results.'
        }
    }
}
