pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                script {
                    sh 'nohup python3 app.py > flask.log 2>&1 &'
                    // sh 'python3 app.py'
                }
            }
        }
    }
}
