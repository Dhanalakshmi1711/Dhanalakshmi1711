pipeline {
    agent any
    stage('Setup Environment') {
            steps {
                script {
                    // Set up virtual environment
                    sh '''
                        python3 -m venv venv
                        source venv/bin/activate
                        pip install flask
                    '''
                }
            }
        }
    stages {
        stage('running flask') {
            steps {
                echo("::::::::::::::::::::::::")
                sh("python3 app.py")
                
            }
        }
    }
}
