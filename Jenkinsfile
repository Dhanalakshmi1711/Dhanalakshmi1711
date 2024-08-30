pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                // checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Dhanalakshmi1711/Dhanalakshmi1711']])
                echo("::::::::::::::::::::::::")
                sh("pip install flask")
                sh("python3 app.py")
                
            }
        }
    }
}
