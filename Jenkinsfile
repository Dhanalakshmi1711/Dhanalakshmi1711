pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo("::::::::::::::::::::::::")
                sh("pip install flask")
                sh("python3 app.py")
                
            }
        }
    }
}
