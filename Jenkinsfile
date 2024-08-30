pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                script {
                    // Set up virtual environment
                    sh 'sudo apt install python3-flask -y'
                }
            }
        }
    }
}
