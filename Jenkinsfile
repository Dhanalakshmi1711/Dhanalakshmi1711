pipeline {
    agent any
    stages {
        stage('running flask') {
            steps {
                echo("::::::::::::::::::::::::")
                sh '''
                        python3 -m venv venv
                        source venv/bin/activate
                        pip install flask
                    '''
                sh("python3 app.py")
                
            }
        }
    }
}
