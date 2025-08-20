pipeline {
    agent { label 'linux-agent' }

    environment {
        MASS = "300"
        DAMPING = "1200"
        PRESSURE = "2e5"
        AREA = "0.015"
        VOLUME = "0.01"
        GAMMA = "1.4"
        SIM_TIME = "10"
        MATLAB_PATH = "/usr/local/MATLAB/R2025a/bin/matlab"  // adjust as needed
        WORKSPACE_DIR = "/var/jenkins_home/workspace/AirSpringSimulation"
    }

    stages {

        stage('Clean Plots Folder') {
            steps {
                echo 'Cleaning plots folder...'
                sh """
                    mkdir -p ${WORKSPACE_DIR}/plots
                    rm -rf ${WORKSPACE_DIR}/plots/*
                """
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
                dir("${WORKSPACE_DIR}") {
                    sh """
                        ${MATLAB_PATH} -batch \\
                        "MASS=${MASS}; DAMPING=${DAMPING}; PRESSURE=${PRESSURE}; AREA=${AREA}; VOLUME=${VOLUME}; GAMMA=${GAMMA}; SIM_TIME=${SIM_TIME}; run('Air_pressure.m')"
                    """
                }
            }
        }

        stage('Run Python Automation') {
            steps {
                echo 'Running Python automation script...'
                dir("${WORKSPACE_DIR}") {
                    sh 'python3 python_automation.py'
                }
            }
        }

        stage('Generate Pass/Fail Trend Graph') {
            steps {
                echo 'Generating pass/fail trend graph...'
                dir("${WORKSPACE_DIR}") {
                    sh 'python3 plot_pass_fail.py'
                }
            }
        }

        stage('Archive Results') {
            steps {
                echo 'Archiving results...'
                archiveArtifacts artifacts: 'air_spring_output.csv, plots/**', allowEmptyArchive: true
            }
        }

    }

    post {
        always { echo 'Pipeline finished.' }
        success { echo '✅ Build succeeded!' }
        failure { echo '❌ Build failed!' }
    }
}
