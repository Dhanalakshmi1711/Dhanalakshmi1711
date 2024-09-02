pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                script {
                    // Set up virtual environment
                    sh 'python3 test.py'
                }
            }
        }
    }
}
