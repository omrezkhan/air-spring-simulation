pipeline {
    agent { label 'linux-agent' }

    environment {
        PROJECT_DIR = "/home/omrez/Downloads/MAt_working/python_jenkins"
        MATLAB_SCRIPT = "Air_pressure.m"
        PYTHON_SCRIPT = "python_automation.py"
    }

    stages {
        stage('Clean Workspace') {
            steps {
                echo 'Cleaning workspace...'
                deleteDir()
            }
        }

        stage('Checkout Code') {
            steps {
                echo 'Checking out project from GitHub...'
                git branch: 'main', url: 'git@github.com:omrezkhan/air-spring-simulation.git'
            }
        }

        stage('Run MATLAB Simulation') {
            steps {
                echo 'Running MATLAB simulation...'
                sh "matlab -batch \"run('${PROJECT_DIR}/${MATLAB_SCRIPT}')\""
            }
        }

        stage('Run Python Automation') {
            steps {
                echo 'Running Python plotting script...'
                sh "python3 ${PROJECT_DIR}/${PYTHON_SCRIPT}"
            }
        }

        stage('Archive Results') {
            steps {
                echo 'Archiving outputs...'
                archiveArtifacts artifacts: 'plots/**, air_spring_output.csv', allowEmptyArchive: true
            }
        }
    }

    post {
        always {
            script {
                // Write 1=SUCCESS, 0=FAILURE for plotting
                def statusValue = currentBuild.currentResult == 'SUCCESS' ? 1 : 0
                writeFile file: 'build_status.txt', text: statusValue.toString()
            }

            // Archive build_status.txt for Plot Plugin
            archiveArtifacts artifacts: 'build_status.txt', allowEmptyArchive: true

            // Generate plot using XML config
            plot csvFileName: 'build_status.txt', 
                 group: 'PassFailTrend', 
                 style: 'line', 
                 title: 'Pass/Fail Trend', 
                 file: 'build_status.txt', 
                 numBuilds: 20
        }

        success {
            echo 'Pipeline completed successfully! ✅'
        }

        failure {
            echo 'Pipeline failed! ❌'
        }
    }
}
