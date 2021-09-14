# -*- coding: utf-8 -*-
"""
Created on Tue May 25 18:55:12 2021

@author: rajya
"""

# imports
import pandas as pd
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt
import pickle
import os
import textwrap

def generateList(inputPath,inputFileFormat):
    fileNames = []
    for root, dirs, files in os.walk(inputPath):
        for file in files:
            if file.endswith(inputFileFormat):
                 fileNames.append(os.path.join(root, file))
    return fileNames

def openPickleFile(fileName):
    pickle_in = open(fileName,"rb")
    example_dict = pickle.load(pickle_in)
    return pickle_in, example_dict

def converttostr(input_seq, seperator):
    # join all strings in sequence
    final_str = seperator.join(input_seq)
    return final_str

def append_new_line(file_name, text_to_append):
    """Append given text as a new line at the end of file"""
    # Open the file in append & read mode ('a+')
    with open(file_name, "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(text_to_append)

# -- main script -- 
def perTrialPlots(fileName, pickleFilesInputPath, pickleFileIdentifier, csvFileIdentifier, deviceName, overlayAnalogPorts, overlayAnalogPortNames, overlayAnalogPortColors, nonOverlayAnalogPorts, nonOverlayAnalogPortNames, 
                  touchThreshold, touchFramesNumberThreshold, touchChannel,figWidth, plotHeight):   
    
    df                           = pd.read_csv(fileName)
    frameColumn                  = 'frame'
    trialColumn                  = 'trial'
    overlayAnalogPorts           = [deviceName+'_'+i for i in overlayAnalogPorts]
    yLimitOverlayAnalogPorts     = max([round(max(df[i]),3) for i in overlayAnalogPorts])
    nonOverlayAnalogPorts        = [deviceName+'_'+i for i in nonOverlayAnalogPorts]
    yLimMaxNonOverlayAnalogPorts = [round(max(df[i]),3)+df[i].std() for i in nonOverlayAnalogPorts]
    yLimMinNonOverlayAnalogPorts = [round(min(df[i]),3)-df[i].std() for i in nonOverlayAnalogPorts]
    uniqueValuesTrialCol         = np.unique(df['trial'])
    trials                       = [int(i) for i in uniqueValuesTrialCol if not np.isnan(i)]
    totalNumSubPlots             = 1 + len(nonOverlayAnalogPorts)
    figHeight                    = totalNumSubPlots*plotHeight + 6
    totalSessionTime             = float(df['Time'][len(df)-1].split(' ')[0])
    samplingFrequency            = (len(df)-1)/totalSessionTime
    dateTime                     = fileName.split('\\')[-1].split(csvFileIdentifier)[0].split('_')
    pickleFilesList              = generateList(pickleFilesInputPath,pickleFileIdentifier)
    text_file                    = '{}_touchBouts.txt'.format(fileName.split('.')[0])
    
    if os.path.exists(text_file):
        os.remove(text_file)
    
    try:
        r                           = fileName.split(csvFileIdentifier)[0].split('\\')[-1].split('_')
        dateTimeString              = '{}_{}_{}'.format(r[0],r[1],r[2])
        fileNameOdorSeq             = [i for i in pickleFilesList if dateTimeString in i][0]
        pickle_in_odorSeq, odorSeq  = openPickleFile(fileNameOdorSeq)
        mouseNum                    = fileNameOdorSeq.split('\\')[-1].split('_')[0]
    except:
        odorSeq                     = []
        
    # -- per trial plots --
    sns.set()
    
    
    for iTrial in range(len(trials)):
        newDf        = df[df[trialColumn]==iTrial+1]
        
        if not odorSeq == []:
            if len(odorSeq) == 1:
                odorName = odorSeq[0]
            else:
                odorName = odorSeq[iTrial]
        else:
            odorName = 'X'
        
        time         = np.arange(0,len(newDf))*1/samplingFrequency
        fig, axes    = plt.subplots(totalNumSubPlots,1, sharex=True, figsize=(figWidth,figHeight))
        if len(dateTime) == 4:
            try:
                fig.suptitle('Trial-{} ({})\nDate: {}\nSession: {}:{}:{}\nOdor:{}'.format(iTrial+1, mouseNum, dateTime[0], dateTime[1], dateTime[2],  dateTime[3], odorName))
            except:
                fig.suptitle('Trial-{}\nDate: {}\nSession: {}:{}:{}\nOdor:{}'.format(iTrial+1, dateTime[0], dateTime[1], dateTime[2], dateTime[3], odorName))
        else:
            fig.suptitle('Trial-{} ({})\nDate: {}\nSession: {}:{}:{}\nOdor:{}'.format(iTrial+1, dateTime[-5], dateTime[-4], dateTime[-3], dateTime[-2], dateTime[-1], odorName))
        
        ## plot overlay plots
        axes[0].set_title('Analog "signature" for trial structure')    
        axes[0].set_ylim(0, yLimitOverlayAnalogPorts) 
        axes[0].set_ylabel('voltage')
        
        
        for iOverlayAnalogPort in range(len(overlayAnalogPorts)):
            sns.lineplot(data=newDf, x= time, y= overlayAnalogPorts[iOverlayAnalogPort],  ax=axes[0], color=overlayAnalogPortColors[iOverlayAnalogPort], alpha = 0.3, linewidth = 1, label= overlayAnalogPortNames[iOverlayAnalogPort])
            l1      = axes[0].lines[iOverlayAnalogPort]
            x1      = l1.get_xydata()[:,0]
            y1      = l1.get_xydata()[:,1]
            axes[0].fill_between(x1,y1, color=overlayAnalogPortColors[iOverlayAnalogPort], alpha=0.2)
        axes[0].legend(labels=overlayAnalogPortNames, bbox_to_anchor=(1.01,1), loc=2,  borderaxespad=0.)
            
        ## plot non-overlay plots
        for iNonOverlayAnalogPort in range(len(nonOverlayAnalogPorts)):
            axes[iNonOverlayAnalogPort + 1].set_title(nonOverlayAnalogPortNames[iNonOverlayAnalogPort])
            axes[iNonOverlayAnalogPort + 1].set_ylim(yLimMinNonOverlayAnalogPorts[iNonOverlayAnalogPort], yLimMaxNonOverlayAnalogPorts[iNonOverlayAnalogPort])
            sns.lineplot(data=newDf, x= time, y= nonOverlayAnalogPorts[iNonOverlayAnalogPort],  ax=axes[iNonOverlayAnalogPort + 1])
            axes[iNonOverlayAnalogPort + 1].set_ylabel('voltage')           
        axes[iNonOverlayAnalogPort + 1].set_xlabel('time (s)')
        
        ## calculate touch bouts
        frames              = newDf[frameColumn]
        touchTrueFalse      = list(newDf[touchChannel]>touchThreshold)
        touchBinary         = [1 if i else 0 for i in touchTrueFalse]
        touchBinaryMod      = [0] + touchBinary
        touchBinaryMod[-1]  = 0
        diffTouchBinaryMod  = np.diff(touchBinaryMod)
        touchStart          = list(frames[diffTouchBinaryMod == 1])
        touchStop           = list(frames[diffTouchBinaryMod == -1])
        touchStopStart      = [str(i) for i in zip(touchStart,touchStop)]
        
        if len(touchStopStart) > touchFramesNumberThreshold:
            touchStr                = 'too many frames'
        elif len(touchStopStart)    == 0:
            touchStr                = 'none'
        else:
            touchStr                = converttostr(touchStopStart, ',')
        figTouchStr = 'Touch frames \n(start, stop): {} | threshold > {}'.format(touchStr, touchThreshold)
        figTouchStrWrapped = textwrap.fill(figTouchStr, width = 20)
        
        ## add legends to figure
        fig.text(1, 0.2, figTouchStrWrapped, ha='center', wrap = True)
        fig.text(0.5, .04, 'pklFilePath: {}'.format(fileNameOdorSeq), ha='center')
        fig.text(0.5, .02, 'csvFilePath: {}'.format(fileName), ha='center')
        
        plt.show(block=False)
        outputFigFileName = '{}_trial{}.png'.format(fileName.split('.')[0],iTrial+1)  
        outputTxtFileName = '{}_trial{}.txt'.format(fileName.split('.')[0],iTrial+1)        
        fig.savefig(outputFigFileName, bbox_inches="tight")
        
        if not len(touchStopStart) == 0:
            append_new_line(text_file, 'Trial {} | Touch frames \n(start, stop): {} | threshold > {}'.format(str(iTrial+1),converttostr(touchStopStart,','), touchThreshold))
        else:
            append_new_line(text_file, 'Trial {} | Touch frames \n(start, stop): {} | threshold > {}'.format(str(iTrial+1),'none', touchThreshold))
        

    text_file.close()
        
    # return df, touchStart, touchStop, touchStopStart

if __name__ == "__main__":        
    # -- inputs --
    inputPath                    = "Z:\\Behavior\\Cristian\\20210602"
    pickleFilesInputPath         = "Z:\\Behavior\\Cristian\\20210602"
    
    csvFileIdentifier            = '_analogData.csv'
    sessionCsvFileNames          = generateList(inputPath, csvFileIdentifier)
    
    pickleFileIdentifier         = '_odorSeq.pkl'
    deviceName                   = 'Dev1'
    overlayAnalogPorts           = ['ai3','ai5', 'ai7']
    overlayAnalogPortNames       = ['laser', 'start>odor>finalSol>stop', 'water']
    overlayAnalogPortColors      = ['red','green','blue']
    # nonOverlayAnalogPorts        = ['ai1', 'ai4']
    # nonOverlayAnalogPortNames    = ['motion sensor', 'touch sensor']
    nonOverlayAnalogPorts        = ['ai0', 'ai1', 'ai4']
    nonOverlayAnalogPortNames    = ['PID', 'motion sensor', 'touch sensor']
    touchThreshold               = 2
    touchFramesNumberThreshold   = 103 # if more than this number of touch bouts then does not print - see text file for info on touch bouts in this case
    touchChannel                 = 'Dev1_ai4'
    figWidth                     = 10
    plotHeight                   = 2
    
    for iSessionCsvFile in range(len(sessionCsvFileNames)):
        fileName = sessionCsvFileNames[iSessionCsvFile]       
        try:
           perTrialPlots(fileName, pickleFilesInputPath, pickleFileIdentifier, csvFileIdentifier, deviceName, overlayAnalogPorts, overlayAnalogPortNames, overlayAnalogPortColors, nonOverlayAnalogPorts, nonOverlayAnalogPortNames, 
                                touchThreshold,  touchFramesNumberThreshold, touchChannel, figWidth, plotHeight)
        except:
            pass

