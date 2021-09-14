% -- inputs for this script -- %
clc
clear
numTrials                           = 1;
trialTime                           = 10; %in sec
interTrialInterval                  = 2; %in sec

totalTrialTime                      = trialTime + interTrialInterval;
totalTime                           = totalTrialTime*numTrials + 3; %in sec
daqType                             = 'ni';
deviceName                          = 'Dev4'; %changed from Dev1
channels                            = 0:15; %changed to add odor AIs
channelNames                        = {'PID',... %ai0
                                        'motion sensor',... %ai1
                                        'camera trigger',... %ai2
                                        'laser',... %ai3
                                        'touch',... %ai4
                                        'start-odor-end',... %ai5
                                        'camera analog',... %ai6
                                        'water',... %ai7
                                        'final_valve',... %ai8
                                        'blue-odor',... %ai9
                                        'red-odor',... %ai10
                                        'green-odor',... %ai11
                                        'brown-odor',... %ai12
                                        'orange-odor',... %ai13 (pink)
                                        'yellow-odor',... %ai14
                                        'odorless-oil'}; %ai15
                                    
camChannelName                      = strcat(deviceName,'_ai2'); % camera real analog
fauxCamChannelName                  = strcat(deviceName,'_ai6'); % camera trigger analog
fauxCamChannelOnThreshold           = 4;

startStopTrialChannelName           = strcat(deviceName,'_ai5');
analogStartSignalChannelThreshold   = 2; 
maxSamplingFrequency                = 160000;   %<----------change based on number of channels (16 channels = 16000 ; 5 channels = 5000)  
pathName                            = uigetdir;
hash                                = '\';
fileNameExtension                   = '_analogData';

% -- main script --
dq = daq(daqType); 
ch = addinput(dq, deviceName, channels, 'Voltage');

for iChannel                        = 1:length(channels)
    ch(iChannel).TerminalConfig     = 'Differential'; %changed from SingleEnded
end

samplingFrequencyPerChannel         = floor(maxSamplingFrequency/length(channels));
disp(samplingFrequencyPerChannel);
dq.Rate                             = samplingFrequencyPerChannel;
dq.ScansAvailableFcn                = @(src,evt) plotDataAvailable(src,evt);
dq.ScansAvailableFcnCount           = samplingFrequencyPerChannel;


fprintf('Waiting for start analog signal...\n')
while read(dq).(startStopTrialChannelName) < analogStartSignalChannelThreshold
    %fprintf('Waiting for start analog signal...\n')
end

tic

trial_tracker = 0 ;
trial_counter = 0 ;
time_index = 0;
while trial_counter < numTrials 
    if read(dq).(startStopTrialChannelName) > analogStartSignalChannelThreshold
        dateTimeString = char(datetime('now','Format','yyyyMMdd''_''HH''_''mm''_''ss'));
        fprintf('Starting acquisition...\n')
        data = read(dq, samplingFrequencyPerChannel*totalTrialTime); %instead of total time -> trial time then plot figure then loop
        toc
        figure
        for iChannel = 1:length(channels)
            subplot(length(channels),1,iChannel)
            fprintf('line 75')
            plot(data.Time(seconds([time_index time_index+samplingFrequencyPerChannel])), data.(ch(iChannel).Name)(1:samplingFrequencyPerChannel*totalTrialTime))
            xlim(seconds([trial_tracker trial_tracker+trialTime]))
            title(strcat(ch(iChannel).Name,': ',channelNames{iChannel}), 'Interpreter','None')
            fprintf('line 79')
            %xlabel('sec')
            ylabel('voltage')
        end
        set(gcf,'units','normalized','outerposition',[0 0 1 1])

    end
    fileName = strcat(pathName,hash,dateTimeString);
    fprintf('line87')
    format = '.png';
    s = strcat(fileName,fileNameExtension,string(trial_counter),format);
    saveas(gcf,s)
    fprintf('line89')

    trial_tracker = trial_tracker + trialTime;
    fprintf('line92')
    trial_counter = trial_counter + 1; 
    fprintf('line94')
    time_index = time_index + samplingFrequencyPerChannel;
    fprintf('line96')
end

%figure

%comment out the lines below if you do not want trial by trial graphs
%(highlight whole chunk and ctrl+r)

% trial_tracker = 0 ;
% trial_counter = 0 ;
% while trial_counter < numTrials 
% %     figure
% %     for iChannel = 1:length(channels)
% %         subplot(length(channels),1,iChannel)
% %         plot(data.Time, data.(ch(iChannel).Name)(1:samplingFrequencyPerChannel*totalTime))
% %         xlim(seconds([trial_tracker trial_tracker+trialTime]))
% %         title(strcat(ch(iChannel).Name,': ',channelNames{iChannel}), 'Interpreter','None')
% %         %xlabel('sec')
% %         ylabel('voltage')
% %     end
% %     set(gcf,'units','normalized','outerposition',[0 0 1 1])
% 
% % -- save figure
% fileName = strcat(pathName,hash,dateTimeString);
% saveas(gcf,strcat(fileName,fileNameExtension,string(trial_counter),'.png')) 
% 
% trial_tracker = trial_tracker + trialTime;
% trial_counter = trial_counter + 1; 
% end

% until here 
fprintf('line123')
toc

figure
for iChannel = 1:length(channels)
    subplot(length(channels),1,iChannel)
    plot(data.Time, data.(ch(iChannel).Name)(1:samplingFrequencyPerChannel*totalTime))
    title(strcat(ch(iChannel).Name,': ',channelNames{iChannel}), 'Interpreter','None')
    %xlabel('sec')
    ylabel('voltage')
end
set(gcf,'units','normalized','outerposition',[0 0 1 1])

% -- save figure
fileName = strcat(pathName,hash,dateTimeString);
saveas(gcf,strcat(fileName,fileNameExtension,'.png')) 
save(strcat(fileName,fileNameExtension,'.mat')) % saving this for safety - slows down code a bit
writetimetable(data,strcat(fileName,fileNameExtension,'.csv')) % saving this for safety - slows down code a bit

