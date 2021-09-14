inputFolderPath = uigetdir('','Select input folder');
numSessions     = 3;
date            = char(datetime('now','Format','yyyyMMdd'));
hash            = '\';

for iSession = 1:numSessions
    mkdir(strcat(inputFolderPath,hash,date,hash,'session',string(iSession),hash,'camImages'))
end