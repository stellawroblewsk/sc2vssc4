# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 17:10:05 2021

@author: rajya
"""
import time
import random
import time
import random
import glob
import ctypes
import numpy as np
import scipy as sp
from scipy import stats
from PyDAQmx import *
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
import mainGUI
from mainGUI import Ui_mousebehaviorstartwindow
import sys
import pickle
from collections import defaultdict
import datetime
import pyautogui
import daqClasses
from daqClasses import stimTrialTimer, stimAnalogTrialTimer, odorAnalogSigStartStop, odorAnalogSigStartStopDisc, sequenceGenerator
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import threading
import os
import sys

class startwindow(QtWidgets.QDialog,Ui_mousebehaviorstartwindow):
    def __init__(self, mousebehaviorstartwindow,parent=None):
        
        super(startwindow, self).__init__(parent)
                
        # odor signature, start, end signaling LED details. Every time a trial starts and stops - an LED can be set to blink for a certain duration. The same LED will blink at a given voltage depending on the specific odor. 
        ## analog port details
        self.startEndStimOdorPortName           = 'ao0'
        self.startEndStimOdorPortAnalogMinVal   = 0
        self.startEndStimOdorPortAnalogMaxVal   = 5
        
        ## odor LED details
        self.odorSigAnalogVoltageKey = {
            'Limonene' : 2,
            'Pinene' : 2.5,
            'Hexenol' : 3,
            'Octanol' : 3.5
            }
        
        self.odorSigAnalogVoltage           = 3 # default voltage for odors - just in case
        
        ## session start LED details
        self.sessionStartStimAnalogVoltage  = 3.75
        self.sessionStartStimDuration       = 1
        self.sessionStartStimTimeToTrial    = 3
        
        ## trial start LED details
        self.startStimDuration              = 1
        self.trialStartAnalogVoltageSig     = 5 # keep this fixed and don't use this value for any odor signature - we use it in our code to break session into individual trials
        
        ## trial stop LED details
        self.endStimDuration                = 1
        self.trialStopAnalogVoltageSig      = 1 # keep this fixed and don't use this value for any odor signature - we use it in our code to break session into individual trials

        ## final solenoids voltage details
        #self.finalSolenoidsAnalogVoltage    = 4
       
        # record 2P and camera during ITI?
        self.recordDuringITI = True # (set to False if not recording 2P and camera during ITI)
    
        # DAQ info
        self.digitalPortsDeviceName     = 'Dev9'
        self.moreThanOneMegaPortsBinary = True # set to True if using 2 ports in the DAQ (eg : port0/lines0:7 and port1/lines0:3 total = 12 ports) - the GUI accepts a line number from 0-11 but I convert lines 8-11 to 'port1/lines0:3') - note I refer to the NI-DAQ ports as 'megaports' and lines as 'ports' throughout my code
        self.portZeroMax                = 7 # highest line number for port 0
        self.portZeroInt                = 0 # integer name of port 0 in device
        self.portOneInt                 = 1 # integer name of port 1 in device
        
        # displays GUI
        self.setupUi(self)
        
        # date autofills
        self.date = datetime.datetime.now().strftime('%Y%m%d')
        self.dateTextbox.setText(self.date)
        self.dateTextbox.setAlignment(QtCore.Qt.AlignCenter)

        
        # list of all textbox variables - find a way to automatically get all textbox variables
        self.textboxVariables = [self.outputFolderTextbox,
                                 self.dateTextbox,
                                 self.mouseNumTextbox,
                                 self.numTrialsTextbox,
                                 self.trialDurationTextbox,
                                 self.laserBinaryTextbox,
                                 self.laserPortTextbox,
                                 self.laserTrialStructureTextbox,
                                 self.odorBinaryTextbox,
                                 self.mineralOilPortTextbox,
                                 #self.finalSolenoidsPortDeltaDelayDurationTextbox,
                                 self.odorTrialStructureTextbox,
                                 self.odorNamePretrainingTextbox,
                                 self.odorPortPretrainingTextbox,
                                 self.rewardedOdorNamesTextbox,
                                 self.rewardedOdorPortsTextbox,
                                 self.unrewardedOdorNamesTextbox,
                                 self.unrewardedOdorPortsTextbox,
                                 self.waterBinaryTextbox,
                                 self.waterPortTextbox,
                                 self.waterTrialStructureTextbox,
                                 self.cameraBinaryTextbox,
                                 self.cameraTriggerPortTextbox,
                                 self.cameraTrialStructureTextbox,
                                 self.twoPhotonTriggerBinaryTextbox,
                                 self.twoPhotonTriggerPortTextbox,
                                 self.twoPhotonTrialStructureTextbox,
                                 self.interTrialIntervalTextbox]
        
        # list of all variables from gather input function + some additional variables from other functions
        self.allVars = ['self.outputFolder',
                        'self.date',
                        'self.mouse',
                        'self.numTrials',
                        'self.trialDuration',
                        'self.laserBinary',
                        'self.laserPort',
                        'self.laserTrialStructurex',
                        'self.odorBinary',
                        'self.mineralOilPort'
                        #'self.finalSolenoidsPortDeltaDelay',
                        'self.odorTrialStructure',
                        'self.odorNamePretraining',
                        'self.odorPortPretraining',
                        'self.rewardedOdorNames',
                        'self.rewardedOdorPorts',
                        'self.unrewardedOdorNames',
                        'self.unrewardedOdorPorts',
                        'self.waterBinary',
                        'self.waterPort',
                        'self.waterTrialStructure',
                        'self.cameraBinary',
                        'self.cameraTriggerPort',
                        'self.cameraTrialStructure',
                        'self.twoPhotonTriggerBinary',
                        'self.twoPhotonTriggerPort',
                        'self.twoPhotonTrialStructure',
                        'self.interTrialInterval',
                        'self.laserDelay',
                        'self.laserDuration',
                        'self.laserFrequency',
                        'self.laserDutyCycle',                        
                        'self.odorDelay',   
                        'self.odorDuration',
                        #'self.finalSolenoidsPort',
                        #'self.finalSolenoidsDeltaDelay',                       
                        'self.waterDelay',    
                        'self.waterDuration',
                        'self.camerafps',
                        'self.cameraDutyCycle',
                        'self.twoPhotonFreq',
                        'self.twoPhotonDutyCycle',
                        'self.stimDictionary']
        
        # assignment of functions to button presses
        self.browseFileButton.clicked.connect(self.openFile)
        self.resetButton.clicked.connect(self.resetFields)
        self.defaultButton.clicked.connect(self.defaultFields)
        self.startTrialTrainingButton.clicked.connect(self.startPretraining)
        self.startTrialDiscriminationButton.clicked.connect(self.startDiscrimination)
        self.resetDAQButton.clicked.connect(self.resetDAQ)
     
    # function to clear all vars listed in self.allVars 
    def clearAllVars(self):
        try:
            del self.outputFolder
        except:
            pass        
        try:
            del self.mouse
        except:
            pass       
        try:
            del self.numTrials
        except:
            pass
        try:
            del self.trialDuration
        except:
            pass
        try:
            del self.laserBinary
        except:
            pass
        try:
            del self.laserPort
        except:
            pass
        try:
            del self.laserTrialStructure
        except:
            pass                
        try:
            del self.odorBinary
        except:
            pass
        try:
            del self.mineralOilPort
        except:
            pass
      #  try:
      #      del self.finalSolenoidsPortDeltaDelay
      #  except:
      #      pass
        try:
            del self.odorTrialStructur
        except:
            pass
        try:
            del self.odorNamePretraining
        except:
            pass
        try:
            del self.odorPortPretraining
        except:
            pass
        try:
            del self.rewardedOdorNames
        except:
            pass
        try:
            del self.rewardedOdorPorts
        except:
            pass
        try:
            del self.unrewardedOdorNames
        except:
            pass        
        try:
            del self.unrewardedOdorPorts
        except:
            pass        
        try:
            del self.waterBinary
        except:
            pass        
        try:
            del self.waterTrialStructure
        except:
            pass        
        try:
            del self.cameraBinary
        except:
            pass
        try:
            del self.cameraTriggerPort
        except:
            pass
        try:
            del self.cameraTrialStructure
        except:
            pass
        try:
            del self.twoPhotonTriggerBinary
        except:
            pass        
        try:
            del self.twoPhotonTriggerPort
        except:
            pass     
        try:
            del self.twoPhotonTrialStructure
        except:
            pass     
        try:
            del self.interTrialInterval
        except:
            pass     
        try:
            del self.laserDuration
        except:
            pass             
        try:
            del self.laserFrequency
        except:
            pass             
        try:
            del self.laserDutyCycle
        except:
            pass             
        try:
            del self.odorDelay
        except:
            pass             
        try:
            del self.odorDuration
        except:
            pass             
        #try:
          #  del self.finalSolenoidsPort
       # except:
         #   pass             
       # try:
        #    del self.finalSolenoidsDeltaDelay
        #except:
        #    pass             
        try:
            del self.waterDelay
        except:
            pass             
        try:
            del self.waterDuration
        except:
            pass             
        try:
            del self.camerafps
        except:
            pass             
        try:
            del self.cameraDutyCycle
        except:
            pass             
        try:
            del self.twoPhotonFreq
        except:
            pass      
        try:
            del self.twoPhotonDutyCycle
        except:
            pass    
        try:
            del self.stimDictionary
        except:
            pass    
        
        # for var in self.allVars:
        #     if var in globals():
        #         del globals()[var] 
   
    # function for choosing output folder
    def openFile(self):
        datafile = QtWidgets.QFileDialog.getExistingDirectory()
        self.outputFolderTextbox.setText(datafile)
        self.outputFolderTextbox.setAlignment(QtCore.Qt.AlignCenter)
     
    # function to reset all textboxes    
    def resetFields(self):
        eliminateList = [self.dateTextbox]
        resetVarList = [i for i in self.textboxVariables if i not in eliminateList] #generalize to any variable
        for iResetVariable in range(len(resetVarList)):
            resetVarList[iResetVariable].clear()
            resetVarList[iResetVariable].setAlignment(QtCore.Qt.AlignCenter)
    
    # function to set default values on textboxes
    def defaultFields(self): 
        self.mouseNumTextbox.setText('1')
        self.numTrialsTextbox.setText('3')
        self.trialDurationTextbox.setText('10')
        self.laserBinaryTextbox.setText('1')
        self.laserPortTextbox.setText('0')
        self.laserTrialStructureTextbox.setText('4.5,4,0,0')
        self.odorBinaryTextbox.setText('1')
        self.mineralOilPortTextbox.setText('5')
        #self.finalSolenoidsPortDeltaDelayDurationTextbox.setText('3,0.5,2')
        self.odorTrialStructureTextbox.setText('2,2')
        self.odorNamePretrainingTextbox.setText('Pinene')
        self.odorPortPretrainingTextbox.setText('6')
        self.rewardedOdorNamesTextbox.setText('Pinene,Limonene')
        self.rewardedOdorPortsTextbox.setText('6,7')
        self.unrewardedOdorNamesTextbox.setText('Hexenol,Octanol')
        self.unrewardedOdorPortsTextbox.setText('8,9')
        self.waterBinaryTextbox.setText('1')
        self.waterPortTextbox.setText('4')
        self.waterTrialStructureTextbox.setText('8,0.50')
        self.cameraBinaryTextbox.setText('0')
        self.cameraTriggerPortTextbox.setText('2')
        self.cameraTrialStructureTextbox.setText('0,0')
        self.twoPhotonTriggerBinaryTextbox.setText('1')
        self.twoPhotonTriggerPortTextbox.setText('1')
        self.twoPhotonTrialStructureTextbox.setText('0,0')
        self.interTrialIntervalTextbox.setText('3')

        for iTextbox in range(len(self.textboxVariables)):
            self.textboxVariables[iTextbox].setAlignment(QtCore.Qt.AlignCenter)

    # function for resetting all tasks on DAQ
    def resetDAQ(self):
        self.gatherInputs()
        self.clearAllVars()           
        try:
            ## Stop all tasks     
            for iTask in range(self.allTasks):
                self.allTasks[iTask].StopTask()   
            print('Terminated all tasks!')
        except:
            print('No tasks running!')
    
    # function to gather all input variables
    def gatherInputs(self):        
        self.sanityCheck = True
        while True:
            try:
                self.numTrials              = int(self.numTrialsTextbox.toPlainText())
                self.trialDuration          = int(self.trialDurationTextbox.toPlainText())
                self.laserBinary            = int(self.laserBinaryTextbox.toPlainText())
                self.waterBinary            = int(self.waterBinaryTextbox.toPlainText())
                self.odorBinary             = int(self.odorBinaryTextbox.toPlainText())
                self.cameraBinary           = int(self.cameraBinaryTextbox.toPlainText())
                self.twoPhotonTriggerBinary = int(self.twoPhotonTriggerBinaryTextbox.toPlainText())
            except:
                pyautogui.alert('Error in critical input(s).', "Achtung!")
                break
                
            if self.outputFolderTextbox.toPlainText() == '':            
                pyautogui.alert('Enter an output directory.', "Achtung!")
                break
            else:
                self.outputFolder                           = self.outputFolderTextbox.toPlainText()
                self.outputFolder                           = self.outputFolder.replace('/','//')
            
            try:
                self.mouse                                  = int(self.mouseNumTextbox.toPlainText())
            except:
                pass
            
            try:
                self.interTrialInterval                     = int(self.interTrialIntervalTextbox.toPlainText())
            except:
                pass
            
            try: 
                self.odorNamePretraining                    = self.odorNamePretrainingTextbox.toPlainText()
            except:
                pass
            
            try:
                self.odorPortPretraining                    = int(self.odorPortPretrainingTextbox.toPlainText())
            except:
                pass             
            
            try:
                self.rewardedOdorNames                      = self.rewardedOdorNamesTextbox.toPlainText().replace(' ','').split(',') # remove .replace(' ',''). if throwing errors
            except:
                pass
        
            try:
                self.rewardedOdorPorts                      = [int(i) for i in self.rewardedOdorPortsTextbox.toPlainText().split(',')]
            except:
                pass        
         
            try:
                self.unrewardedOdorNames                    = self.unrewardedOdorNamesTextbox.toPlainText().replace(' ','').split(',') # remove .replace(' ',''). if throwing errors
            except:
                pass            
           
            try:
                self.unrewardedOdorPorts                    = [int(i) for i in self.unrewardedOdorPortsTextbox.toPlainText().split(',')]
            except:
                pass               
            try:
                self.mineralOilPort                         = int(self.mineralOilPortTextbox.toPlainText())
            except:
                pass
           # try:
            #    self.finalSolenoidsPortDeltaDelayDuration   = [float(i) for i in self.finalSolenoidsPortDeltaDelayDurationTextbox.toPlainText().split(',')]
            #except:
            #    pass
            #try:
            #    self.finalSolenoidsPort                     = int(self.finalSolenoidsPortDeltaDelayDuration[0])
            #except:
            #    pass
            #try:
          #      self.finalSolenoidsDeltaDelay               = self.finalSolenoidsPortDeltaDelayDuration[1]
            #except:
            #    pass
           # try:
           #     self.finalSolenoidsDuration                 = self.finalSolenoidsPortDeltaDelayDuration[2]
           # except:
            #    pass
            
            if self.laserBinary == 1:
                try:
                    self.laserTrialStructure = [float(i) for i in self.laserTrialStructureTextbox.toPlainText().split(',')]
                    self.laserDelay         = self.laserTrialStructure[0]
                    self.laserDuration      = self.laserTrialStructure[1]
                    self.laserFrequency     = int(self.laserTrialStructure[2])
                    self.laserDutyCycle     = self.laserTrialStructure[3]
                    self.laserPort          = int(self.laserPortTextbox.toPlainText())
                    
                except:
                    pyautogui.alert('Enter trial structure for laser!', "Achtung!")
                    break
                    
                
            if self.waterBinary == 1:
                try:
                    self.waterTrialStructure = [float(i) for i in self.waterTrialStructureTextbox.toPlainText().split(',')]
                    self.waterDelay          = self.waterTrialStructure[0]
                    self.waterDuration       = self.waterTrialStructure[1]
                    self.waterPort           = int(self.waterPortTextbox.toPlainText())
                except:
                    pyautogui.alert('Enter trial structure for water!', "Achtung!")
                    break

                                
            if self.odorBinary == 1:
                try:
                    self.odorTrialStructure = [float(i) for i in self.odorTrialStructureTextbox.toPlainText().split(',')]
                    self.odorDelay          = self.odorTrialStructure[0]
                    self.odorDuration       = self.odorTrialStructure[1]
                    # - troubleshoot why this does not work when put here - 
                    # self.odorNamePretraining = self.odorNamePretrainingTextbox.toPlainText()
                    # self.odorPortPretraining = int(self.odorPortPretrainingTextbox.toPlainText())
                    # self.rewardedOdorNames = self.rewardedOdorNamesTextbox.toPlainText().split(',')
                    # self.rewardedOdorPorts = [int(i) for i in self.rewardedOdorPortsTextbox.toPlainText().split(',')]
                    # self.unrewardedOdorNames = self.unrewardedOdorNamesTextbox.toPlainText().split(',')
                    # self.unrewardedOdorPorts = [int(i) for i in self.unrewardedOdorPortsTextbox.toPlainText().split(',')]
                    # #self.mineralOilPort = int(self.mineralOilPortTextbox.toPlainText())
                    # self.finalSolenoidsPortDeltaDelayDuration = [float(i) for i in self.finalSolenoidsPortDeltaDelayDurationTextbox.toPlainText().split(',')]
                    # self.finalSolenoidsPort = int(self.finalSolenoidsPortDeltaDelayDuration[0])
                    # self.finalSolenoidsDeltaDelay = self.finalSolenoidsPortDeltaDelayDuration[1]
                    # self.finalSolenoidsDuration = self.finalSolenoidsPortDeltaDelayDuration[2]
                   
                except:
                    pyautogui.alert('Enter trial structure for odors!', "Achtung!")
                    break                   
                
            if self.cameraBinary == 1:
                try:
                    self.cameraTrialStructure   = [float(i) for i in self.cameraTrialStructureTextbox.toPlainText().split(',')]
                    self.camerafps              = int(self.cameraTrialStructure[0])
                    self.cameraDutyCycle        = self.cameraTrialStructure[1]
                    self.cameraTriggerPort      = int(self.cameraTriggerPortTextbox.toPlainText())
                except:
                    pyautogui.alert('Enter trial structure for water!', "Achtung!")
                    break
                
            if self.twoPhotonTriggerBinary == 1:
                try:
                    self.twoPhotonTriggerPort       = int(self.twoPhotonTriggerPortTextbox.toPlainText())
                    self.twoPhotonTrialStructure    = [float(i) for i in self.twoPhotonTrialStructureTextbox.toPlainText().split(',')]
                    self.twoPhotonFreq              = int(self.twoPhotonTrialStructure[0])
                    self.twoPhotonDutyCycle         = self.twoPhotonTrialStructure[1]
                except:
                    pyautogui.alert('Enter trial structure for water!', "Achtung!")
                    break                
            break
        
        
        try:
            self.numTrials
            self.trialDuration 
            self.laserBinary 
            self.waterBinary
            self.odorBinary
            self.cameraBinary
            self.twoPhotonTriggerBinary
            self.outputFolder
        except:
            self.sanityCheck = False
            
    # function for pretraining trials
    def startPretraining(self):
            
        # -- Part 1 --
        ## clear leftovers from previous session and determine trial duration (recording camera and 2P during ITI or not)
        self.clearAllVars()
        
        ## clear fields that are not relevant for pretraining
        self.rewardedOdorNamesTextbox.clear()
        self.rewardedOdorNamesTextbox.setAlignment(QtCore.Qt.AlignCenter)
        self.rewardedOdorPortsTextbox.clear()
        self.rewardedOdorPortsTextbox.setAlignment(QtCore.Qt.AlignCenter)
        self.unrewardedOdorNamesTextbox.clear()
        self.unrewardedOdorNamesTextbox.setAlignment(QtCore.Qt.AlignCenter)
        self.unrewardedOdorPortsTextbox.clear()
        self.unrewardedOdorPortsTextbox.setAlignment(QtCore.Qt.AlignCenter)

        ## gather all entries from GUI prompts and turn them into variables and start camera script if camera is used
        print('Starting Pretraining trials...')
        
        self.gatherInputs()
        
        if self.sanityCheck == True:         
                       
            ## determine 'real' trial duration (recording camera and 2P during ITI or not)
            if self.recordDuringITI == True:
                self.realTrialDuration = self.trialDuration + self.interTrialInterval
            else:
                self.realTrialDuration = self.trialDuration
                
            # -- Part 2 --
            ## compose a stimuli dictionary - we will call from this dictionary when threading        
            self.stimDictionary = {}
            
            ## add start trial, stop trial LED details (make sure each 'trigger' ie 'write' in digiproxyport are temporally non-overlapping because we use the same DOOut for each trigger)
            self.stimDictionary.update({                   
                'digiProxyPort' : {
                    'stimuli' : {
                        'startLED' : {
                            'stimName' : 'startLED',
                            'delay' : 0,
                            'duration' :  self.startStimDuration,
                            'trialDuration' : self.trialDuration,
                            'analogVoltage' : self.trialStartAnalogVoltageSig
                            },
                        
                        'endLED' : {
                            'stimName' : 'endLED',
                            'delay' : self.trialDuration - self.endStimDuration,
                            'duration' : self.endStimDuration,
                            'trialDuration' : self.trialDuration,
                            'analogVoltage' : self.trialStopAnalogVoltageSig
                            }
                        },
                      'portName' : self.startEndStimOdorPortName,
                      'analogMinVal' : self.startEndStimOdorPortAnalogMinVal,
                      'analogMaxVal' : self.startEndStimOdorPortAnalogMaxVal
                    }
                })
            
            ## add details of odor trial structure if it is an odor trial - same LED that signals start and stop trial
            if self.odorBinary == True:                                           
                try:
                    self.odorSigAnalogVoltage = self.odorSigAnalogVoltageKey[self.odorNamePretraining]
                except:
                    pass
                     

                self.stimDictionary.update({                   
                  'digiProxyPort' : {
                      'stimuli' : {
                          'startLED' : {
                              'stimName' : 'startLED',
                              'delay' : 0,
                              'duration' :  self.startStimDuration,
                              'trialDuration' : self.trialDuration,
                              'analogVoltage' : self.trialStartAnalogVoltageSig
                              },
                          
                          'endLED' : {
                              'stimName' : 'endLED',    
                              'delay' : self.trialDuration - self.endStimDuration,
                              'duration' : self.endStimDuration,
                              'trialDuration' : self.trialDuration,
                              'analogVoltage' : self.trialStopAnalogVoltageSig
                              },
                          
                          'odorSig' : {
                              'stimName' : 'odorSig',
                              'delay' : self.odorDelay,
                              'duration' :  self.odorDuration,
                              'trialDuration' : self.trialDuration,
                              'analogVoltage' : self.odorSigAnalogVoltage
                              },
                          
                          # 'finalSol' : {
                          #     'stimName' : 'finalSol',
                          #     'delay' : self.odorDelay + self.odorDuration + self.finalSolenoidsDeltaDelay,
                          #     'duration' : self.finalSolenoidsDuration,
                          #     'trialDuration' : self.trialDuration,
                          #     'analogVoltage' : self.finalSolenoidsAnalogVoltage
                          #     }
                          },
                      
                      'portName' : self.startEndStimOdorPortName,
                      'analogMinVal' : self.startEndStimOdorPortAnalogMinVal,
                      'analogMaxVal' : self.startEndStimOdorPortAnalogMaxVal
                      }
                  })
            
                
                self.stimDictionary.update({
                    'odor':{
                        'stimName':self.odorNamePretraining,
                        'delay': self.odorDelay,
                        'duration': self.odorDuration,
                        'frequency': [],
                        'dutyCycle':[],
                        'deviceName' : self.digitalPortsDeviceName,
                        'portName' : self.odorPortPretraining   
                            },
                    
                    'control1': {
                        'stimName': 'mineralOil',
                        'delay': self.odorDelay,
                        'duration': self.odorDuration,
                        'frequency': [],
                        'dutyCycle':[],
                        'deviceName' : self.digitalPortsDeviceName,
                        'portName' : self.mineralOilPort
                                },
                    
                    # 'finalSolenoidsPort':{
                    #     'stimName':'finalSolenoids',
                    #     'delay': self.odorDelay + self.odorDuration + self.finalSolenoidsDeltaDelay,
                    #     'duration':  self.finalSolenoidsDuration,
                    #     'frequency': [],
                    #     'dutyCycle':[],
                    #     'deviceName' : self.digitalPortsDeviceName,
                    #     'portName' : self.finalSolenoidsPort  
                    #         }
                    })
           
            else:
                self.stimDictionary.update({                   
                  'digiProxyPort' : {
                      'stimuli' : {
                          'startLED' : {
                              'stimName' : 'startLED',
                              'delay' : 0,
                              'duration' :  self.startStimDuration,
                              'frequency' : [],
                              'dutyCycle' : [],
                              'trialDuration' : self.trialDuration,
                              'analogVoltage' : self.trialStartAnalogVoltageSig
                              },
                          
                          'endLED' : {
                              'stimName' : 'endLED',
                              'delay' : self.trialDuration - self.endStimDuration,
                              'duration' : self.endStimDuration,
                              'frequency' : [],
                              'dutyCycle' : [],
                              'trialDuration' : self.trialDuration,
                              'analogVoltage' : self.trialStopAnalogVoltageSig
                              },
                          },
                      
                      'portName' : self.startEndStimOdorPortName
                      }
                  })

            ## add details of water trial structure if it is a trial where water is delivered                
            if self.waterBinary == True: 
                self.stimDictionary.update({
                    'water':{
                        'stimName':'water',
                        'delay': self.waterDelay,
                        'duration':self.waterDuration,
                        'frequency': [],
                        'dutyCycle':[],
                        'deviceName' : self.digitalPortsDeviceName,
                        'portName' : self.waterPort,        
                            }
                    })
            else:
                pass

            ## add details of laser trial structure if it is a laser trial            
            if self.laserBinary == True: 
                self.stimDictionary.update({
                    'laser':{
                        'stimName':'laser',
                        'delay': self.laserDelay,
                        'duration': self.laserDuration,
                        'frequency' : self.laserFrequency,
                        'dutyCycle' : self.laserDutyCycle,
                        'deviceName' : self.digitalPortsDeviceName,
                        'portName' : self.laserPort
                            }
                    })
            else:
                pass
            
            ## add camera aquisition details if camera is used
            if self.cameraBinary == True:                    
                self.stimDictionary.update({
                    'camera':{
                        'stimName':'camera',
                        'delay':0,
                        'duration': self.realTrialDuration,
                        'frequency': self.camerafps,
                        'dutyCycle' : self.cameraDutyCycle,
                        'deviceName' : self.digitalPortsDeviceName,
                        'portName' : self.cameraTriggerPort        
                            }
                    })
            else:
                pass       

            ## add 2P aquisition details if imaging
            if self.twoPhotonTriggerBinary == True: 
                self.stimDictionary.update({
                    'twoPhoton':{
                        'stimName':'2P',
                        'delay':0,
                        'duration': self.realTrialDuration,
                        'frequency': self.twoPhotonFreq,
                        'dutyCycle' : self.twoPhotonDutyCycle,
                        'deviceName' : self.digitalPortsDeviceName,
                        'portName' : self.twoPhotonTriggerPort        
                            }
                    })
            else:
                pass       
            
        ## convert portname to megaportname/portname format
            if self.moreThanOneMegaPortsBinary == True:
                for iStim in range(len(self.stimDictionary)):
                    if not list(self.stimDictionary)[iStim] == 'digiProxyPort':
                        if self.stimDictionary[list(self.stimDictionary)[iStim]]['portName'] > self.portZeroMax:
                            self.stimDictionary[list(self.stimDictionary)[iStim]]['portName'] = self.stimDictionary[list(self.stimDictionary)[iStim]]['portName'] - self.portZeroMax - 1
                            self.stimDictionary[list(self.stimDictionary)[iStim]]['megaPortName'] = self.portOneInt
                        else:
                            self.stimDictionary[list(self.stimDictionary)[iStim]]['megaPortName'] = self.portZeroInt
                    else:
                        pass
                    
           # save stimDictionary in a pickle file before tasks are assigned
            outputPickleFileDict = self.stimDictionary            
            if not os.path.exists('{}//{}'.format(self.outputFolder, self.date)): 
                os.mkdir('{}//{}'.format(self.outputFolder, self.date))            
            
            timeNow        = datetime.datetime.now()
            dateTime       = timeNow.strftime("%Y%m%d_%H_%M_%S")
            try:           
                fileName   = 'mouse{}_{}'.format(str(self.mouse),dateTime)
            except:
                fileName   = '{}'.format(dateTime)
            outputPickleFile = '{}//{}//{}'.format(self.outputFolder, self.date, fileName) 

                
            f = open('{}_stimDict.pkl'.format(outputPickleFile),"wb") 
            pickle.dump(outputPickleFileDict,f)
            f.close()        
            
            # -- Part 3 -- 
            ## make individual tasks for each digital port
            self.allTasks = []
            for iTask in range(len(self.stimDictionary)):
                if not list(self.stimDictionary)[iTask] == 'digiProxyPort':
                    DOOut = Task()
                    megaPortName = self.stimDictionary[list(self.stimDictionary)[iTask]]['megaPortName']
                    portName = self.stimDictionary[list(self.stimDictionary)[iTask]]['portName']
                    DOOut.CreateDOChan('{}/port{}/line{}'.format(self.digitalPortsDeviceName, megaPortName, portName), "", DAQmx_Val_ChanForAllLines)
                    # print('{}/port{}/line{}'.format(deviceName, megaPortName, portName))
                    self.stimDictionary[list(self.stimDictionary)[iTask]]['task'] = DOOut
                    self.allTasks.append(DOOut)
                    DOOut = []
                else:
                    AOOut = Task()
                    AOOut.CreateAOVoltageChan("{}/{}".format(self.digitalPortsDeviceName, self.startEndStimOdorPortName),"",self.startEndStimOdorPortAnalogMinVal,self.startEndStimOdorPortAnalogMaxVal, DAQmx_Val_Volts, None)
                    self.stimDictionary['digiProxyPort']['task'] = AOOut
                    self.allTasks.append(AOOut)

            # start all tasks
            for iTask in range(len(self.allTasks)):
                self.allTasks[iTask].StartTask()            
            DOOutwrit = int32()
            
            # -- Part4 --
            ## start session with an analog signal that signals other computer to start reading analog ports
            stimAnalogTrialTimer('startSession', 0, self.sessionStartStimDuration, self.sessionStartStimTimeToTrial, self.stimDictionary['digiProxyPort']['task'], self.sessionStartStimAnalogVoltage)
            
            ## define individual threads                 
            for iTrials in range(self.numTrials):
                print('Starting trial {}...'.format(str(iTrials+1)))
                threads = []
                for iTask in range(len(self.stimDictionary)):  
                    if not list(self.stimDictionary)[iTask] == 'digiProxyPort':
                        threads.append(threading.Thread(target=stimTrialTimer, 
                                                        args=(self.stimDictionary[list(self.stimDictionary)[iTask]]['stimName'],
                                                              self.stimDictionary[list(self.stimDictionary)[iTask]]['delay'],
                                                              self.stimDictionary[list(self.stimDictionary)[iTask]]['duration'],
                                                              self.stimDictionary[list(self.stimDictionary)[iTask]]['frequency'],
                                                              self.stimDictionary[list(self.stimDictionary)[iTask]]['dutyCycle'],
                                                              self.realTrialDuration,
                                                              self.stimDictionary[list(self.stimDictionary)[iTask]]['portName'], 
                                                              self.stimDictionary[list(self.stimDictionary)[iTask]]['task'], 
                                                              DOOutwrit)))
                    else: 
                        pass
                threads.append(threading.Thread(target = odorAnalogSigStartStop, args=(self.stimDictionary['digiProxyPort'],'stimuli'))) # not sure why this is buggy i.e. why I need a second argument            
                                                
                
            # -- Part6 --
                ## Start and join individual threads            
                for iThread in range(len(threads)):
                    threads[iThread].start()
                        
                for iThread in range(len(threads)):
                    threads[iThread].join()
             
                if self.recordDuringITI == False:
                    time.sleep(self.interTrialInterval)
                else:
                    pass
                             
            ## Stop all tasks     
            for iTask in range(len(self.allTasks)):
                self.allTasks[iTask].StopTask()
            
            if self.odorBinary == True:
                outputPickleFileDict.update({
                    'odorSeq' : self.odorNamePretraining
                    })
        
                x = open('{}_odorSeq.pkl'.format(outputPickleFile),"wb") 
                pickle.dump([self.odorNamePretraining],x)
                x.close()
            
            print('Session ended!')
            
        else:
            pyautogui.alert('Critical inputs missing - try again!', "Achtung!")
            
    # function for discrimination trials
    def startDiscrimination(self):
        self.clearAllVars()           
        self.odorNamePretrainingTextbox.clear()
        self.odorNamePretrainingTextbox.setAlignment(QtCore.Qt.AlignCenter)
        self.odorPortPretrainingTextbox.clear()
        self.odorPortPretrainingTextbox.setAlignment(QtCore.Qt.AlignCenter)
        self.gatherInputs()
                
        if self.sanityCheck == True:                              
            ## determine 'real' trial duration (recording camera and 2P during ITI or not)
            if self.recordDuringITI == True:
                self.realTrialDuration = self.trialDuration + self.interTrialInterval
            else:
                self.realTrialDuration = self.trialDuration
                
            # -- Part 2 --
            ## compose a stimuli dictionary - we will call from this dictionary when threading        
            print('Starting Discrimination trials...')
            self.stimDictionary = {}
    
            ## add start trial, stop trial LED details (make sure each 'trigger' ie 'write' in digiproxyport are temporally non-overlapping because we use the same DOOut for each trigger)
            self.stimDictionary.update({                   
                'digiProxyPort' : {
                    'stimuli' : {
                        'LEDSig': {                
                            'startLED' : {
                                'stimName' : 'startLED',
                                'delay' : 0,
                                'duration' : self.startStimDuration,
                                'trialDuration' : self.trialDuration,
                                'analogVoltage' : self.trialStartAnalogVoltageSig
                                },
                            
                            'endLED' : {
                                'stimName' : 'endLED',
                                'delay' : self.trialDuration - self.endStimDuration,
                                'duration' : self.endStimDuration,
                                'trialDuration' : self.trialDuration,
                                'analogVoltage' : self.trialStopAnalogVoltageSig
                                }
                            }
                        },
                      'portName' : self.startEndStimOdorPortName,
                      'analogMinVal' : self.startEndStimOdorPortAnalogMinVal,
                      'analogMaxVal' : self.startEndStimOdorPortAnalogMaxVal
                    }
                })
                    
    
            ## add details of water trial structure if it is a trial where water is delivered                
            if self.waterBinary == True: 
                self.stimDictionary.update({
                    'water':{
                        'stimName':'water',
                        'delay': self.waterDelay,
                        'duration': self.waterDuration,
                        'frequency': [],
                        'dutyCycle': [],
                        'deviceName': self.digitalPortsDeviceName,
                        'portName': self.waterPort,        
                            }
                    })
            else:
                pass
    
            ## add details of laser trial structure if it is a laser trial            
            if self.laserBinary == True: 
                self.stimDictionary.update({
                    'laser':{
                        'stimName':'laser',
                        'delay': self.laserDelay,
                        'duration': self.laserDuration,
                        'frequency': self.laserFrequency,
                        'dutyCycle': self.laserDutyCycle,
                        'deviceName': self.digitalPortsDeviceName,
                        'portName': self.laserPort
                            }
                    })
            else:
                pass
            
            ## add camera aquisition details if camera is used
            if self.cameraBinary == True:                    
                self.stimDictionary.update({
                    'camera':{
                        'stimName':'camera',
                        'delay': 0,
                        'duration': self.realTrialDuration,
                        'frequency': self.camerafps,
                        'dutyCycle': self.cameraDutyCycle,
                        'deviceName': self.digitalPortsDeviceName,
                        'portName': self.cameraTriggerPort        
                            }
                    })
            else:
                pass       
    
            ## add 2P aquisition details if imaging
            if self.twoPhotonTriggerBinary == True: 
                self.stimDictionary.update({
                    'twoPhoton':{
                        'stimName':'2P',
                        'delay':0,
                        'duration': self.realTrialDuration,
                        'frequency': self.twoPhotonFreq,
                        'dutyCycle': self.twoPhotonDutyCycle,
                        'deviceName': self.digitalPortsDeviceName,
                        'portName': self.twoPhotonTriggerPort        
                            }
                    })
            else:
                pass          
            
            ## add odor details if odor trial
            if self.odorBinary == True:                 
                
                ### add details of mineral oil and final solenoids
                self.stimDictionary.update({                    
                    'control1': {
                        'stimName': 'mineralOil',
                        'delay': self.odorDelay,
                        'duration': self.odorDuration,
                        'frequency': [],
                        'dutyCycle':[],
                        'deviceName': self.digitalPortsDeviceName,
                        'portName': self.mineralOilPort
                                },
                    
                    # 'finalSolenoidsPort':{
                    #     'stimName':'finalSolenoids',
                    #     'delay': self.odorDelay + self.odorDuration + self.finalSolenoidsDeltaDelay,
                    #     'duration':  self.finalSolenoidsDuration,
                    #     'frequency': [],
                    #     'dutyCycle':[],
                    #     'deviceName': self.digitalPortsDeviceName,
                    #     'portName': self.finalSolenoidsPort  
                    #         }
                    })
    
                ### add details of odors and final solenoids to digiProxyPort dictionary
                # self.stimDictionary['digiProxyPort']['stimuli']['LEDSig'].update({
                #      'finalSolenoidsPort': {
                #          'stimName':'finalSolenoids',
                #          'delay': self.odorDelay + self.odorDuration + self.finalSolenoidsDeltaDelay,
                #          'duration':  self.finalSolenoidsDuration,
                #          'trialDuration': self.trialDuration,
                #          'analogVoltage' : self.finalSolenoidsAnalogVoltage
                #          }
                #      })
    
                self.stimDictionary['digiProxyPort']['stimuli'].update({
                     'odorSig' : {}
                     })       
                
                ### add details of odors 
                self.stimDictionary.update({
                     'odors' : {}
                     })    
                
                for iRewardedOdorName in range(len(self.rewardedOdorNames)):
                    self.stimDictionary['odors'].update({
                        self.rewardedOdorNames[iRewardedOdorName] : {
                            'stimName' : self.rewardedOdorNames[iRewardedOdorName],
                            'delay' : self.odorDelay,
                            'duration': self.odorDuration,
                            'trialDuration' : self.trialDuration,                    
                            'frequency': [],
                            'dutyCycle':[],
                            'deviceName': self.digitalPortsDeviceName,
                            'portName':  self.rewardedOdorPorts[iRewardedOdorName],
                            'rewardedBinary': True
                            }
                        })
        
                    self.stimDictionary['digiProxyPort']['stimuli']['odorSig'].update({
                        self.rewardedOdorNames[iRewardedOdorName] : {
                            'stimName' : self.rewardedOdorNames[iRewardedOdorName],
                            'delay' : self.odorDelay,
                            'duration': self.odorDuration,
                            'trialDuration' : self.trialDuration,
                            'analogVoltage' : self.odorSigAnalogVoltageKey[self.rewardedOdorNames[iRewardedOdorName]],
                            'rewardedBinary': True
                            }
                        })
        
                for iUnrewardedOdorName in range(len(self.unrewardedOdorNames)):
                    self.stimDictionary['odors'].update({
                        self.unrewardedOdorNames[iUnrewardedOdorName] : {
                            'stimName' : self.unrewardedOdorNames[iUnrewardedOdorName],
                            'delay' : self.odorDelay,
                            'duration': self.odorDuration,
                            'trialDuration' : self.trialDuration,                    
                            'frequency': [],
                            'dutyCycle':[],
                            'deviceName': self.digitalPortsDeviceName,
                            'portName': self.unrewardedOdorPorts[iUnrewardedOdorName],
                            'rewardedBinary': False
                            }
                        })
                    
                    self.stimDictionary['digiProxyPort']['stimuli']['odorSig'].update({
                        self.unrewardedOdorNames[iUnrewardedOdorName] : {
                            'stimName' : self.unrewardedOdorNames[iUnrewardedOdorName],
                            'delay' : self.odorDelay,
                            'duration': self.odorDuration,
                            'trialDuration' : self.trialDuration,
                            'analogVoltage' : self.odorSigAnalogVoltageKey[self.unrewardedOdorNames[iUnrewardedOdorName]],
                            'rewardedBinary': False
                            }
                        })    
            
            ## convert portName to megaPortName/portName wherever necessary
            if self.moreThanOneMegaPortsBinary == True:
                for iStim in range(len(self.stimDictionary)):
                    try:
                        if self.stimDictionary[list(self.stimDictionary)[iStim]]['portName'] > self.portZeroMax:
                            self.stimDictionary[list(self.stimDictionary)[iStim]]['portName'] = self.stimDictionary[list(self.stimDictionary)[iStim]]['portName'] - self.portZeroMax - 1
                            self.stimDictionary[list(self.stimDictionary)[iStim]]['megaPortName'] = self.portOneInt
                        else:
                            self.stimDictionary[list(self.stimDictionary)[iStim]]['megaPortName'] = self.portZeroInt
                    except:
                        pass
                
                if self.odorBinary == True:                
                    for iStim in range(len(self.stimDictionary['odors'])):
                        try:
                            if self.stimDictionary['odors'][list(self.stimDictionary['odors'])[iStim]]['portName'] > self.portZeroMax:
                                self.stimDictionary['odors'][list(self.stimDictionary['odors'])[iStim]]['portName'] = self.stimDictionary['odors'][list(self.stimDictionary['odors'])[iStim]]['portName'] - self.portZeroMax - 1
                                self.stimDictionary['odors'][list(self.stimDictionary['odors'])[iStim]]['megaPortName'] = self.portOneInt
                            else:
                                self.stimDictionary['odors'][list(self.stimDictionary['odors'])[iStim]]['megaPortName'] = self.portZeroInt
                        except:
                            pass 
                        
           
            # save stimDictionary in a pickle file before tasks are assigned                        
            outputPickleFileDict = self.stimDictionary            
            if not os.path.exists('{}//{}'.format(self.outputFolder, self.date)): 
                os.mkdir('{}//{}'.format(self.outputFolder, self.date))            
            
            timeNow        = datetime.datetime.now()
            dateTime       = timeNow.strftime("%Y%m%d_%H_%M_%S")
            try:           
                fileName   = 'mouse{}_{}'.format(str(self.mouse),dateTime)
            except:
                fileName   = '{}'.format(dateTime)
            outputPickleFile = '{}//{}//{}'.format(self.outputFolder, self.date, fileName) 
              
            f = open('{}_stimDict.pkl'.format(outputPickleFile),"wb") 
            pickle.dump(outputPickleFileDict,f)
            f.close()
            
            ## create tasks and save task numbers in stimDictionary
            self.allTasks = []
            DOOutwrit = int32()
            for iTask in range(len(self.stimDictionary)):
                if list(self.stimDictionary)[iTask] == 'digiProxyPort':
                    try:
                        AOOut = Task()
                        AOOut.CreateAOVoltageChan("{}/{}".format(self.digitalPortsDeviceName, self.stimDictionary[list(self.stimDictionary)[iTask]]['portName']),"",self.startEndStimOdorPortAnalogMinVal,self.startEndStimOdorPortAnalogMaxVal, DAQmx_Val_Volts, None)
                        self.stimDictionary[list(self.stimDictionary)[iTask]]['task'] = AOOut
                        # self.stimDictionary[list(self.stimDictionary)[iTask]]['task'].StartTask()
                        self.allTasks.append(AOOut)
                        AOOut = []
                    except:
                        pass
                else:
                    pass            
        
            for iTask in range(len(self.stimDictionary)):
                if not list(self.stimDictionary)[iTask] == 'digiProxyPort':
                    try:
                        DOOut = Task()
                        megaPortName = self.stimDictionary[list(self.stimDictionary)[iTask]]['megaPortName']
                        portName = self.stimDictionary[list(self.stimDictionary)[iTask]]['portName']
                        DOOut.CreateDOChan('{}/port{}/line{}'.format(self.digitalPortsDeviceName, megaPortName, portName), "", DAQmx_Val_ChanForAllLines)
                        self.stimDictionary[list(self.stimDictionary)[iTask]]['task'] = DOOut
                        # self.stimDictionary[list(self.stimDictionary)[iTask]]['task'].StartTask()
                        self.allTasks.append(DOOut)
                        DOOut = []         
                    except:
                        pass
                else:
                    pass
            
            if self.odorBinary == True:
                 for iOdorTask in range(len(self.stimDictionary['odors'])):
                     try:
                         DOOut = Task() 
                         megaPortName = self.stimDictionary['odors'][list(self.stimDictionary['odors'])[iOdorTask]]['megaPortName'] 
                         portName = self.stimDictionary['odors'][list(self.stimDictionary['odors'])[iOdorTask]]['portName'] 
                         DOOut.CreateDOChan('{}/port{}/line{}'.format(self.digitalPortsDeviceName, megaPortName, portName), "", DAQmx_Val_ChanForAllLines) 
                         self.stimDictionary['odors'][list(self.stimDictionary['odors'])[iOdorTask]]['task'] = DOOut 
                         # self.stimDictionary['odors'][list(self.stimDictionary['odors'])[iOdorTask]]['task'].StartTask() 
                         self.allTasks.append(DOOut)
                         DOOut = []
                     except:
                         pass
            else:
                pass
            
            
            # start all tasks
            for iTask in range(len(self.allTasks)):
                self.allTasks[iTask].StartTask()    
            
            # start session with an analog signal that signals other computer to start reading analog ports
            stimAnalogTrialTimer('startSession', 0, self.sessionStartStimDuration, self.sessionStartStimTimeToTrial, self.stimDictionary['digiProxyPort']['task'], self.sessionStartStimAnalogVoltage)
            
            if self.odorBinary == True:
            ## randomize trials
                trialSeq = sequenceGenerator(self.numTrials, self.odorSigAnalogVoltageKey)
                # print(trialSeq)
                # trialSeq = ['Limonene', 'Pinene', 'Octanol', 'Hexenol', 'Hexenol', 'Pinene', 'Octanol', 'Limonene']
                
                ## loop through randomized trials
                for iTrial in range(len(trialSeq)):   
                    print('Starting trial {}...'.format(str(iTrial+1)))
                    threads = []
                    threads.append(threading.Thread(target = odorAnalogSigStartStopDisc, args=(self.stimDictionary['digiProxyPort'],
                                                                                                trialSeq[iTrial],
                                                                                                'stimuli',
                                                                                                'LEDSig',
                                                                                                'odorSig')))
                    threads.append(threading.Thread(target=stimTrialTimer, 
                                    args=(self.stimDictionary['odors'][trialSeq[iTrial]]['stimName'],
                                          self.stimDictionary['odors'][trialSeq[iTrial]]['delay'],
                                          self.stimDictionary['odors'][trialSeq[iTrial]]['duration'],
                                          self.stimDictionary['odors'][trialSeq[iTrial]]['frequency'],
                                          self.stimDictionary['odors'][trialSeq[iTrial]]['dutyCycle'],
                                          self.realTrialDuration,
                                          self.stimDictionary['odors'][trialSeq[iTrial]]['portName'], 
                                          self.stimDictionary['odors'][trialSeq[iTrial]]['task'], 
                                          DOOutwrit)))
                    
                    if self.stimDictionary['odors'][trialSeq[iTrial]]['rewardedBinary']:
                        threads.append(threading.Thread(target=stimTrialTimer, 
                                        args=(self.stimDictionary['water']['stimName'],
                                              self.stimDictionary['water']['delay'],
                                              self.stimDictionary['water']['duration'],
                                              self.stimDictionary['water']['frequency'],
                                              self.stimDictionary['water']['dutyCycle'],
                                              self.realTrialDuration,
                                              self.stimDictionary['water']['portName'], 
                                              self.stimDictionary['water']['task'], 
                                              DOOutwrit)))
                    else:
                        pass
                    
                    for iTask in range(len(self.stimDictionary)):  
                        if not list(self.stimDictionary)[iTask] == 'digiProxyPort' and not list(self.stimDictionary)[iTask] == 'odors' and not list(self.stimDictionary)[iTask] == 'water':
                            threads.append(threading.Thread(target=stimTrialTimer, 
                                                            args=(self.stimDictionary[list(self.stimDictionary)[iTask]]['stimName'],
                                                                  self.stimDictionary[list(self.stimDictionary)[iTask]]['delay'],
                                                                  self.stimDictionary[list(self.stimDictionary)[iTask]]['duration'],
                                                                  self.stimDictionary[list(self.stimDictionary)[iTask]]['frequency'],
                                                                  self.stimDictionary[list(self.stimDictionary)[iTask]]['dutyCycle'],
                                                                  self.realTrialDuration,
                                                                  self.stimDictionary[list(self.stimDictionary)[iTask]]['portName'], 
                                                                  self.stimDictionary[list(self.stimDictionary)[iTask]]['task'], 
                                                                  DOOutwrit)))
                    # -- Part6 --
                    ## Start and join individual threads            
                    for iThread in range(len(threads)):
                        threads[iThread].start()
                            
                    for iThread in range(len(threads)):
                        threads[iThread].join()
                 
                    if self.recordDuringITI == False:
                        time.sleep(self.interTrialInterval)
                    else:
                        pass
                             
                            
            else:
                for iTrial in range(self.numTrials):
                    print('Starting trial {}...'.format(str(iTrial+1)))
                    threads = []
                    threads.append(threading.Thread(target = odorAnalogSigStartStopDisc, args=(self.stimDictionary['digiProxyPort'],
                                                                                                [],
                                                                                                'stimuli',
                                                                                                'LEDSig',
                                                                                                [])))
                    for iTask in range(len(self.stimDictionary)):
                        try:
                            threads.append(threading.Thread(target=stimTrialTimer, 
                                                            args=(self.stimDictionary[list(self.stimDictionary)[iTask]]['stimName'],
                                                                  self.stimDictionary[list(self.stimDictionary)[iTask]]['delay'],
                                                                  self.stimDictionary[list(self.stimDictionary)[iTask]]['duration'],
                                                                  self.stimDictionary[list(self.stimDictionary)[iTask]]['frequency'],
                                                                  self.stimDictionary[list(self.stimDictionary)[iTask]]['dutyCycle'],
                                                                  self.realTrialDuration,
                                                                  self.stimDictionary[list(self.stimDictionary)[iTask]]['portName'], 
                                                                  self.stimDictionary[list(self.stimDictionary)[iTask]]['task'], 
                                                                  DOOutwrit)))
                        except: 
                            pass
                                                        
                    
                    # -- Part6 --
                    ## Start and join individual threads            
                    for iThread in range(len(threads)):
                        threads[iThread].start()
                            
                    for iThread in range(len(threads)):
                        threads[iThread].join()
                    
                    if self.recordDuringITI == False:
                        time.sleep(self.interTrialInterval)
                    else:
                        pass
                             
            ## stop all tasks     
            for iTask in range(len(self.allTasks)):
                self.allTasks[iTask].StopTask()       
          
            
            if self.odorBinary == True:
                outputPickleFileDict.update({
                    'odorSeq' : trialSeq
                    })
        
                x = open('{}_odorSeq.pkl'.format(outputPickleFile),"wb") 
                pickle.dump(trialSeq, x)
                x.close()
                
            print('Session ended!')
        else:
            pyautogui.alert('Critical inputs missing - try again!', "Achtung!")
            
# run the main GUI    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainwin = QtWidgets.QDialog()
    w = startwindow(mainwin, parent=None)
    w.show()
    app.exec_()