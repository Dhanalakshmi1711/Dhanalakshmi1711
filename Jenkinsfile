pipeline {
    agent any

    stages {
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
        stage('Run Flask Application') {
            steps {
                script {
                    // Run Flask application
                    sh '''
                        source venv/bin/activate
                        python app.py &
                    '''
                }
            }
        }
        stage('Check Application') {
            steps {
                // Example of a check or test, adjust based on your needs
                sh '''
                    sleep 5
                    curl -s http://127.0.0.1:5000/
                '''
            }
        }
    }
}
