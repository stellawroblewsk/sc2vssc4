inputFolderPath                     = uigetdir('','Select input folder');
outputFolderPath                    = uigetdir('','Select output folder');
fileIdentifier                      = '_analogData.csv';
hash                                = '\';
inputCsvFilePaths                   = dir(strcat(inputFolderPath,'\**\*',fileIdentifier));

for iCsvFile            = 1:size(inputCsvFilePaths,1)
   inputCsvFilePath     = strcat(inputCsvFilePaths(iCsvFile).folder, hash,...
        inputCsvFilePaths(iCsvFile).name); 
   copyfile(inputCsvFilePath, outputFolderPath)
end
