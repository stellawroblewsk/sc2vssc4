function postProcessSessionCsv(inputMatFilePath, deltaWinStartStopVoltageThreshold,...
    cameraMinimumHighThreshold, cameraAnalogThreshold, determineStartStopTrialVolThreshold,...
    trialStartVoltageThreshold, trialStopVoltageThreshold)

    % -- determine frame numbers --
    load(inputMatFilePath)
    camChannelDataStream        = data.(camChannelName);
    if max(camChannelDataStream) > cameraMinimumHighThreshold
        r                       = analogToDigital(camChannelDataStream,cameraAnalogThreshold);
        frames                  = digitalToFrameNumber(r);
        numInstancesLastFrame   = length(frames(frames == frames(end)));
        numFrames               = [];
        for iFrame              = 1:frames(end)-1
            numFrames(iFrame)   = length(frames(frames == iFrame));
        end
        actualLastFrames        = median(numFrames);

        if numInstancesLastFrame > actualLastFrames 
           data.frame           = vertcat(frames(1:(end-numInstancesLastFrame)+actualLastFrames),nan((numInstancesLastFrame - actualLastFrames),1));
        else
           data.frame           = frames;
        end
    end

    % -- determine trial numbers --
    if determineStartStopTrialVolThreshold == true && max(camChannelDataStream) > cameraMinimumHighThreshold
        cameraFrameOne              = find(data.(fauxCamChannelName)>=4);
        firstCameraFrame            = cameraFrameOne(5); %taking the 5th frame just to be safe
        firstTrialLastCameraFrame   = firstCameraFrame + trialTime*samplingFrequencyPerChannel-1-4;
        startTrialSignal            = data.(startStopTrialChannelName)(firstCameraFrame);
        stopTrialSignal             = data.(startStopTrialChannelName)(firstTrialLastCameraFrame);
        trialStartVoltageThreshold  = [round(startTrialSignal-deltaWinStartStopVoltageThreshold,2), round(startTrialSignal+deltaWinStartStopVoltageThreshold,2)];
        trialStopVoltageThreshold   = [round(stopTrialSignal-deltaWinStartStopVoltageThreshold,2), round(stopTrialSignal+deltaWinStartStopVoltageThreshold,2)];
    end

    startTrialDataStream            = [0; data.(startStopTrialChannelName)>trialStartVoltageThreshold(1)...
                                        & data.(startStopTrialChannelName)<trialStartVoltageThreshold(2)];
    stopTrialDataStream             = [0; data.(startStopTrialChannelName)>trialStopVoltageThreshold(1)...
                                        & data.(startStopTrialChannelName)<trialStopVoltageThreshold(2)];

    diffStartTrialDataStream        = diff(startTrialDataStream);
    diffStopTrialDataStream         = diff(stopTrialDataStream);
    trialStartStopFrames            = [find(diffStartTrialDataStream==1), find(diffStopTrialDataStream==-1)-1];
    trialNumber                     = nan(size(data,1),1);

    for iTrial = 1:size(trialStartStopFrames,1)
        trialNumber(trialStartStopFrames(iTrial,1):trialStartStopFrames(iTrial,2)) = iTrial;
    end
    data.trial = trialNumber;

    % -- save timetable along with date and time of when the whole session
    % ended --
    writetimetable(data,strcat(fileName,fileNameExtension,'.csv')) 
    save(strcat(fileName,fileNameExtension,'.mat'))
end
