pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                // checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Dhanalakshmi1711/Dhanalakshmi1711']])
                echo("::::::::::::::::::::::::")
                sh("apt install python3-flask")
                sh("python3 app.py")
                
            }
        }
    }
}
