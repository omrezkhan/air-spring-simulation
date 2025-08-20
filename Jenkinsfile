pipeline {
    agent any

    parameters {
        string(name: 'MASS', defaultValue: '300', description: 'Sprung mass [kg]')
        string(name: 'DAMPING', defaultValue: '1200', description: 'Damping coefficient [Ns/m]')
        string(name: 'PRESSURE', defaultValue: '2e5', description: 'Initial pressure [Pa]')
        string(name: 'AREA', defaultValue: '0.015', description: 'Effective diaphragm area [m^2]')
        string(name: 'VOLUME', defaultValue: '0.01', description: 'Chamber volume [m^3]')
        string(name: 'GAMMA', defaultValue: '1.4', description: 'Polytropic index [-]')
        string(name: 'SIM_TIME', defaultValue: '10', description: 'Simulation time [s]')
        string(name: 'MATLAB_SCRIPT', defaultValue: 'AirSpringModelScript.m', description: 'MATLAB script to run')
    }

    environment {
        PROJECT_DIR = "${WORKSPACE}"
    }

    stages {

        stage('Clean Plots Folder') {
            steps {
                echo 'Cleaning plots folder...'
                sh 'mkdir -p plots && rm -rf plots/* || true'
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
                sh """
                    matlab -batch "MASS=${params.MASS}; DAMPING=${params.DAMPING}; PRESSURE=${params.PRESSURE}; AREA=${params.AREA}; VOLUME=${params.VOLUME}; GAMMA=${params.GAMMA}; SIM_TIME=${params.SIM_TIME}; run('${PROJECT_DIR}/${params.MATLAB_SCRIPT}')"
                """
            }
        }

        stage('Run Python Automation') {
            steps {
                echo 'Running Python automation script...'
                sh 'python3 automation.py'
            }
        }

        stage('Archive Results') {
            steps {
                echo 'Archiving CSV and plot files...'
                archiveArtifacts artifacts: 'plots/*, air_spring_output.csv', fingerprint: true
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded! ✅'
        }
        failure {
            echo 'Pipeline failed! ❌'
        }
    }
}
