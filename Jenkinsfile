pipeline {
    agent { label 'linux-agent' }

    environment {
        PROJECT_DIR = "/home/omrez/Downloads/MAt_working/python_jenkins"
        MATLAB_SCRIPT = "Air_pressure.m"
        PYTHON_SCRIPT = "python_automation.py"
        PASS_FAIL_SCRIPT = "plot_pass_fail.py"
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
                // Convert SUCCESS/FAILURE to 1/0 for trend plotting
                def statusValue = currentBuild.currentResult == 'SUCCESS' ? 1 : 0
                writeFile file: "${PROJECT_DIR}/build_status.txt", text: statusValue.toString()
                
                // Update pass/fail trend plot
                sh "python3 ${PROJECT_DIR}/${PASS_FAIL_SCRIPT}"
            }
            
            // Archive the trend plot and status file
            archiveArtifacts artifacts: 'plots/pass_fail_trend.png, build_status.txt', allowEmptyArchive: true
        }

        success {
            echo 'Pipeline completed successfully! ✅'
        }
        failure {
            echo 'Pipeline failed! ❌'
        }
    }
}
