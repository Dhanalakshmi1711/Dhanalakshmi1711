pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                script {
                    // Set up virtual environment
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate'
                    
                    // Install dependencies
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        
        stage('Run Flask Application') {
            steps {
                script {
                    // Run the Flask app
                    sh '. venv/bin/activate && python app.py &'
                }
            }
        }
    }
}
