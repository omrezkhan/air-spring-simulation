pipeline {
    agent { label 'linux-agent' }  // Run this pipeline on the agent labeled 'linux-agent'

    environment {
        PROJECT_DIR = "/home/omrez/Downloads/MAt_working/python_jenkins"
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
                sh "matlab -batch \"run('${PROJECT_DIR}/${MATLAB_SCRIPT}')\""
            }
        }

        stage('Run Python Automation') {
            steps {
                echo 'Running Python script to plot CSV data...'
                sh "python3 ${PROJECT_DIR}/${PYTHON_SCRIPT}"
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
