pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                script {
                    sh 'python3 app.py'
                }
            }
        }
    }
}
