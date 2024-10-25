pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[credentialsId: '59415612', url: 'https://github.com/Sujeethrk07/devops_pipeline.git']])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', credentialsId: '59415612', url: 'https://github.com/Sujeethrk07/devops_pipeline.git'
                bat 'python sout.py'
                
            }
        }
        stage('Test') {
            steps {
                echo "Testing is done"
            }
        }
    }
}
