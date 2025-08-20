%% Air Spring Suspension Simulation Script
% This script initializes parameters in the MATLAB workspace,
% runs the Simulink model, and exports results to CSV.

clc; clear; close all;

%% Ensure MATLAB is in the folder with this script (and the .slx file)
scriptDir = fileparts(mfilename('fullpath'));
cd(scriptDir);

%% Parameters (feel free to change values)
m = 350;          % Sprung mass [kg]
c = 1200;         % Damping coefficient [Ns/m]
P0 = 2e5;         % Initial pressure [Pa]
A = 0.015;        % Effective diaphragm area [m^2]
V0 = 0.01;        % Chamber volume [m^3]
gamma = 1.4;      % Polytropic index [-]

t_end = 10;       % Simulation time [s]

%% Load and run Simulink model
modelName = 'AirSpringModel';
load_system(modelName);                 % Load the model
set_param(modelName,'StopTime',num2str(t_end));
out = sim(modelName);                   % Run simulation
close_system(modelName, 0);             % Close without saving changes

%% Extract signals from logsout (Simulink -> To Workspace or logging signals)
time = out.tout;
displacement = out.logsout.getElement('displacement').Values.Data;
velocity     = out.logsout.getElement('velocity').Values.Data;
force        = out.logsout.getElement('force').Values.Data;

%% Save to CSV
T = table(time, displacement, velocity, force);
writetable(T, 'air_spring_output.csv');

disp("✅ Simulation complete. Results saved to air_spring_output.csv");
