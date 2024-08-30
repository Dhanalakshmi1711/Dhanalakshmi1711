pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                script {
                    // Set up virtual environment
                    sh 'python3 app.py'
                    sh '''
                    sleep 5
                    curl -s http://127.0.0.1:5000/
                '''
                }
            }
        }
    }
}
