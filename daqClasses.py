# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 13:15:13 2021

@author: rajya
"""
import numpy as np
from PyDAQmx import *
from ctypes import byref
import ctypes
import time
import threading
import random 

def sequenceGenerator(numTrials, odorSigAnalogVoltageKey):  
    # print('Generating a random sequence of {} numbers...'.format(len(odorSigAnalogVoltageKey)))
    seq = [random.randint(0, len(odorSigAnalogVoltageKey) - 1) for i in range(numTrials)]
    odorSeq = [list(odorSigAnalogVoltageKey)[i] for i in seq]
    # print(odorSeq)
    return odorSeq

def stimTrialTimer(stimName, stimDelay, stimDuration, stimFrequency, stimDutyCycle, trialDuration, portName, DOOut, DOOutwrit):
    if (stimFrequency == [] or stimFrequency == 0) and (stimDutyCycle == [] or stimDutyCycle == 0):
        time.sleep(stimDelay)   
        DOOut.WriteDigitalU16(1,True,0,DAQmx_Val_GroupByChannel,np.array([2**portName],dtype='uint16'),ctypes.byref(DOOutwrit),None)
        time.sleep(stimDuration)
        DOOut.WriteDigitalU16(1,True,0,DAQmx_Val_GroupByChannel,np.array([0],dtype='uint16'),ctypes.byref(DOOutwrit),None)
        time.sleep(trialDuration - (stimDuration+stimDelay))
   
    else:
        numPulses = int(stimFrequency*stimDuration)
        pulsePeriod = 1/stimFrequency
        onSleep = stimDutyCycle*pulsePeriod
        offSleep = pulsePeriod - onSleep
        #offSleep = (1-stimDutyCycle)*pulsePeriod
        time.sleep(stimDelay)
        
        for i in range(numPulses):
            startTime = time.time()
            while onSleep >= time.time() - startTime:
                # print('{} (port {}) is On, time: {}.'.format(stimName, str(2**portName), time.ctime()))
                 DOOut.WriteDigitalU16(1,True,0,DAQmx_Val_GroupByChannel,np.array([2**portName],dtype='uint16'),ctypes.byref(DOOutwrit),None)
                # time.sleep(onSleep)
            while offSleep + onSleep >= time.time() - startTime > onSleep :
                # print('{} (port {}) is Off, time: {}.'.format(stimName, str(2**portName), time.ctime()))
                 DOOut.WriteDigitalU16(1,True,0,DAQmx_Val_GroupByChannel,np.array([0],dtype='uint16'),ctypes.byref(DOOutwrit),None)
        time.sleep(trialDuration -(stimDuration+stimDelay))
               
              
def stimAnalogTrialTimer(stimName, stimDelay, stimDuration, trialDuration, AOOut, analogVoltage):
     time.sleep(stimDelay)    
     AOOut.WriteAnalogScalarF64(1,10.0,analogVoltage,None)
     time.sleep(stimDuration)
     AOOut.WriteAnalogScalarF64(1,10.0,0,None)
     time.sleep(trialDuration - (stimDuration + stimDelay))
     

def odorAnalogSigStartStop(dictThreadDetails, a):
    threads = []
    for iStim in range(len(dictThreadDetails[a])):
        t = threading.Thread(target=stimAnalogTrialTimer, args=(dictThreadDetails[a][list(dictThreadDetails[a])[iStim]]['stimName'],
                                                          dictThreadDetails[a][list(dictThreadDetails[a])[iStim]]['delay'],
                                                          dictThreadDetails[a][list(dictThreadDetails[a])[iStim]]['duration'],
                                                          dictThreadDetails[a][list(dictThreadDetails[a])[iStim]]['trialDuration'], 
                                                          dictThreadDetails['task'], 
                                                          dictThreadDetails[a][list(dictThreadDetails[a])[iStim]]['analogVoltage']))
        threads.append(t)
    for iThread in range(len(threads)):
        threads[iThread].start()        
    for iThread in range(len(threads)):
        threads[iThread].join()
        
        
def odorAnalogSigStartStopDisc(dictThreadDetails, odorName, masterDict, loopDict, pickOneDict):
    threads = []
    for iStim in range(len(dictThreadDetails[masterDict][loopDict])):
        
        t = threading.Thread(target=stimAnalogTrialTimer, args=(dictThreadDetails[masterDict][loopDict][list(dictThreadDetails[masterDict][loopDict])[iStim]]['stimName'],
                                                          dictThreadDetails[masterDict][loopDict][list(dictThreadDetails[masterDict][loopDict])[iStim]]['delay'],
                                                          dictThreadDetails[masterDict][loopDict][list(dictThreadDetails[masterDict][loopDict])[iStim]]['duration'],
                                                          dictThreadDetails[masterDict][loopDict][list(dictThreadDetails[masterDict][loopDict])[iStim]]['trialDuration'], 
                                                          dictThreadDetails['task'], 
                                                          dictThreadDetails[masterDict][loopDict][list(dictThreadDetails[masterDict][loopDict])[iStim]]['analogVoltage']))
        threads.append(t)
    
    if not pickOneDict == [] and not odorName == []: 
        threads.append(threading.Thread(target=stimAnalogTrialTimer, args=(dictThreadDetails[masterDict][pickOneDict][odorName]['stimName'],
                                          dictThreadDetails[masterDict][pickOneDict][odorName]['delay'],
                                          dictThreadDetails[masterDict][pickOneDict][odorName]['duration'],
                                          dictThreadDetails[masterDict][pickOneDict][odorName]['trialDuration'], 
                                          dictThreadDetails['task'], 
                                          dictThreadDetails[masterDict][pickOneDict][odorName]['analogVoltage'])))

    for iThread in range(len(threads)):
        threads[iThread].start()        
    for iThread in range(len(threads)):
        threads[iThread].join()