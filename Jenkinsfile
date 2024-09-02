pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                script {
                    // Set up virtual environment
                    sh 'pip install -r requirements.txt'
                    sh 'python3 app.py'
                }
            }
        }
    }
}
