% -- inputs for this script -- %
clc
clear
numTrials                           = 10;
trialTime                           = 10; %in sec
interTrialInterval                  = 3; %in sec

totalTrialTime                      = trialTime + interTrialInterval;
totalTime                           = totalTrialTime*numTrials + 3; %in sec
daqType                             = 'ni';
deviceName                          = 'Dev3'; %changed from Dev1
channels                            = 0:15; %changed to add odor AIs (also changed to 14 w/o final valve)
channelNames                        = {'PID',... %ai0
                                        'motion sensor',... %ai1
                                        'camera trigger',... %ai2
                                        'laser',... %ai3
                                        'touch',... %ai4
                                        'start-odor-end',... %ai5
                                        'camera analog',... %ai6
                                        'water',... %ai7
                                        'pseduo valve - ignore',... %ai8   
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
maxSamplingFrequency                = 160000;   % <----------change based on number of channels (16 channels = 16000 ; 5 channels = 5000)  
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
if read(dq).(startStopTrialChannelName) > analogStartSignalChannelThreshold
    dateTimeString = char(datetime('now','Format','yyyyMMdd''_''HH''_''mm''_''ss'));
    fprintf('Starting acquisition...\n')
    data = read(dq, samplingFrequencyPerChannel*totalTime); %instead of total time -> trial time then plot figure then loop
end
toc

%figure

%comment out the lines below if you do not want trial by trial graphs
%(highlight whole chunk and right click to comment/uncomment

% trial_tracker = 0 ;
% trial_counter = 0 ;
% while trial_counter < numTrials 
%     figure
%     for iChannel = 1:length(channels)
%         subplot(length(channels),1,iChannel)
%         plot(data.Time, data.(ch(iChannel).Name)(1:samplingFrequencyPerChannel*totalTime))
%         xlim(seconds([trial_tracker trial_tracker+trialTime]))
%         title(strcat(ch(iChannel).Name,': ',channelNames{iChannel}), 'Interpreter','None')
%         %xlabel('sec')
%         ylabel('voltage')
%     end
%     set(gcf,'units','normalized','outerposition',[0 0 1 1])
% 
% % -- save figure
% fileName = strcat(pathName,hash,dateTimeString);
% saveas(gcf,strcat(fileName,fileNameExtension,string(trial_counter),'.png')) 
% 
% trial_tracker = trial_tracker + trialTime;
% trial_counter = trial_counter + 1; 
% end

% until here 


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