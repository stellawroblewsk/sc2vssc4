clc;
clear;

% -- inputs --
masterFolderPath                    = uigetdir;
fileIdentifier                      = '_analogData.mat';
hash                                = '\';
inputMatFilePaths                   = dir(strcat(masterFolderPath,'\**\*',fileIdentifier));
deltaWinStartStopVoltageThreshold   = 0.05;
cameraMinimumHighThreshold          = 1;
cameraAnalogThreshold               = 0.2;
determineStartStopTrialVolThreshold = true;
trialStartVoltageThreshold          = [4.58, 4.78]; % to determine thresholds rather than hardcoding, set determineStartStopTrialVolThreshold to True 
trialStopVoltageThreshold           = [0.9, 1.1]; % to determine thresholds rather than hardcoding, set determineStartStopTrialVolThreshold to True 


% -- actual script --
for iMatFile            = 1:size(inputMatFilePaths,1)
   
    inputMatFilePath    = strcat(inputMatFilePaths(iMatFile).folder, hash,...
        inputMatFilePaths(iMatFile).name);   
    
%     try
    postProcessSessionCsv(inputMatFilePath, deltaWinStartStopVoltageThreshold,...
    cameraMinimumHighThreshold, cameraAnalogThreshold, determineStartStopTrialVolThreshold,...
    trialStartVoltageThreshold, trialStopVoltageThreshold)
%     catch
%         warning('Problem using function!')
%     end
    
end
