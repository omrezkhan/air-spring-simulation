pipeline {
    agent { label 'linux-agent' }  // Run this pipeline on the agent labeled 'linux-agent'

    environment {
        MATLAB_SCRIPT = "Air_pressure.m"
        PYTHON_SCRIPT = "python_automation.py"
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Checking out the project from GitHub...'
                git branch: 'main', url: 'git@github.com:omrezkhan/air-spring-simulation.git'
            }
        }

        stage('Run MATLAB Simulation') {
            steps {
                echo 'Running MATLAB simulation script...'
                dir("${env.WORKSPACE}") {
                    sh "matlab -batch \"run('${MATLAB_SCRIPT}')\""
                }
            }
        }

        stage('Run Python Automation') {
            steps {
                echo 'Running Python script to plot CSV data...'
                dir("${env.WORKSPACE}") {
                    sh "python3 ${PYTHON_SCRIPT}"
                }
            }
        }

        stage('Archive Results') {
            steps {
                echo 'Archiving simulation outputs...'
                archiveArtifacts artifacts: 'plots/**, air_spring_output.csv', allowEmptyArchive: true
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully! ✅'
        }
        failure {
            echo 'Pipeline failed! ❌'
        }
    }
}
