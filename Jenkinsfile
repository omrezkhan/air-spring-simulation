pipeline {
    agent { label 'linux-agent' }

    parameters {
        string(name: 'MASS', defaultValue: '300', description: 'Sprung mass [kg]')
        string(name: 'DAMPING', defaultValue: '1200', description: 'Damping coefficient [Ns/m]')
        string(name: 'PRESSURE', defaultValue: '2e5', description: 'Initial pressure [Pa]')
        string(name: 'AREA', defaultValue: '0.015', description: 'Diaphragm area [m^2]')
        string(name: 'VOLUME', defaultValue: '0.01', description: 'Chamber volume [m^3]')
        string(name: 'GAMMA', defaultValue: '1.4', description: 'Polytropic index [-]')
        string(name: 'SIM_TIME', defaultValue: '10', description: 'Simulation time [s]')
    }

    environment {
        MATLAB_PATH = "/usr/local/MATLAB/R2025a/bin/matlab"
        LOCAL_PROJECT_DIR = "/home/omrez/Downloads/MAt_working/python_jenkins"
    }

    stages {

        stage('Clean Plots Folder') {
            steps {
                echo 'Cleaning plots folder...'
                dir("${LOCAL_PROJECT_DIR}") {
                    sh """
                        mkdir -p plots
                        rm -rf plots/*
                    """
                }
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
                dir("${LOCAL_PROJECT_DIR}") {
                    sh """
                        ${MATLAB_PATH} -batch \\
                        "MASS=${params.MASS}; DAMPING=${params.DAMPING}; PRESSURE=${params.PRESSURE}; AREA=${params.AREA}; VOLUME=${params.VOLUME}; GAMMA=${params.GAMMA}; SIM_TIME=${params.SIM_TIME}; run('Air_pressure.m')"
                    """
                }
            }
        }

        stage('Run Python Automation') {
            steps {
                echo 'Running Python automation script to generate plots...'
                dir("${LOCAL_PROJECT_DIR}") {
                    sh 'python3 python_automation.py'
                }
            }
        }

        stage('Generate Pass/Fail Trend Graph') {
            steps {
                echo 'Generating pass/fail trend graph...'
                dir("${LOCAL_PROJECT_DIR}") {
                    sh 'python3 plot_pass_fail.py'
                }
            }
        }

        stage('Archive CSV and Plots') {
            steps {
                echo 'Archiving CSV and plots...'
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
