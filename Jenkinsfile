
pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                dir('D:/SubtractionMLOps') {
                    bat 'venv\\Scripts\\python.exe -m pip install -r requirements.txt'
                }
            }
        }

        stage('Run Pytest') {
            steps {
                dir('D:/SubtractionMLOps') {
                    bat 'venv\\Scripts\\python.exe -m pytest -v'
                }
            }
        }

        stage('Generate Pytest HTML Report') {
            steps {
                dir('D:/SubtractionMLOps') {
                    bat 'if not exist reports mkdir reports'
                    bat 'venv\\Scripts\\python.exe -m pytest -v --html=reports/pytest_report.html --self-contained-html'
                }
            }
        }

        stage('Generate Evidently Report') {
            steps {
                dir('D:/SubtractionMLOps') {
                    bat 'venv\\Scripts\\python.exe generate_report.py'
                }
            }
        }
    }

    post {
        always {
            dir('D:/SubtractionMLOps') {
                archiveArtifacts artifacts: 'reports/*.html',
                                 allowEmptyArchive: true
            }
        }

        success {
            echo 'Subtraction MLOps Pipeline Completed Successfully!'
        }

        failure {
            echo 'Pipeline Failed. Please Check Console Output.'
        }
    }
}
