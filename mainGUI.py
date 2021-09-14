# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maingui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mousebehaviorstartwindow(object):
    def setupUi(self, mousebehaviorstartwindow):
        mousebehaviorstartwindow.setObjectName("mousebehaviorstartwindow")
        mousebehaviorstartwindow.resize(988, 975)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(mousebehaviorstartwindow)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(9, 30, 271, 901))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.outputFolderLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.outputFolderLabel.setFont(font)
        self.outputFolderLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.outputFolderLabel.setObjectName("outputFolderLabel")
        self.verticalLayout_6.addWidget(self.outputFolderLabel)
        self.dateLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.dateLabel.setFont(font)
        self.dateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dateLabel.setObjectName("dateLabel")
        self.verticalLayout_6.addWidget(self.dateLabel)
        self.mouseNumLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.mouseNumLabel.setFont(font)
        self.mouseNumLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mouseNumLabel.setObjectName("mouseNumLabel")
        self.verticalLayout_6.addWidget(self.mouseNumLabel)
        self.numTrialsLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.numTrialsLabel.setFont(font)
        self.numTrialsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.numTrialsLabel.setObjectName("numTrialsLabel")
        self.verticalLayout_6.addWidget(self.numTrialsLabel)
        self.trialTimeLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.trialTimeLabel.setFont(font)
        self.trialTimeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.trialTimeLabel.setObjectName("trialTimeLabel")
        self.verticalLayout_6.addWidget(self.trialTimeLabel)
        self.laserBinaryLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.laserBinaryLabel.setFont(font)
        self.laserBinaryLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.laserBinaryLabel.setObjectName("laserBinaryLabel")
        self.verticalLayout_6.addWidget(self.laserBinaryLabel)
        self.laserPortLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.laserPortLabel.setFont(font)
        self.laserPortLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.laserPortLabel.setObjectName("laserPortLabel")
        self.verticalLayout_6.addWidget(self.laserPortLabel)
        self.laserTrialStructureLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.laserTrialStructureLabel.setFont(font)
        self.laserTrialStructureLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.laserTrialStructureLabel.setObjectName("laserTrialStructureLabel")
        self.verticalLayout_6.addWidget(self.laserTrialStructureLabel)
        self.odorBinaryLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.odorBinaryLabel.setFont(font)
        self.odorBinaryLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.odorBinaryLabel.setObjectName("odorBinaryLabel")
        self.verticalLayout_6.addWidget(self.odorBinaryLabel)
        self.mineralOilPortLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.mineralOilPortLabel.setFont(font)
        self.mineralOilPortLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mineralOilPortLabel.setObjectName("mineralOilPortLabel")
        self.verticalLayout_6.addWidget(self.mineralOilPortLabel)
        # self.finalSolenoidsPortDeltaDelayDurationLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        # font = QtGui.QFont()
        # font.setFamily("Gill Sans MT")
        # font.setPointSize(12)
        # font.setBold(False)
        # font.setWeight(50)
        # self.finalSolenoidsPortDeltaDelayDurationLabel.setFont(font)
        # self.finalSolenoidsPortDeltaDelayDurationLabel.setAlignment(QtCore.Qt.AlignCenter)
        # self.finalSolenoidsPortDeltaDelayDurationLabel.setObjectName("finalSolenoidsPortDeltaDelayDurationLabel")
        # self.verticalLayout_6.addWidget(self.finalSolenoidsPortDeltaDelayDurationLabel)
        self.odorTrialStructurePretrainingLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.odorTrialStructurePretrainingLabel.setFont(font)
        self.odorTrialStructurePretrainingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.odorTrialStructurePretrainingLabel.setObjectName("odorTrialStructurePretrainingLabel")
        self.verticalLayout_6.addWidget(self.odorTrialStructurePretrainingLabel)
        self.odorNamePretrainingLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.odorNamePretrainingLabel.setFont(font)
        self.odorNamePretrainingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.odorNamePretrainingLabel.setObjectName("odorNamePretrainingLabel")
        self.verticalLayout_6.addWidget(self.odorNamePretrainingLabel)
        self.odorPortPretrainingLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.odorPortPretrainingLabel.setFont(font)
        self.odorPortPretrainingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.odorPortPretrainingLabel.setObjectName("odorPortPretrainingLabel")
        self.verticalLayout_6.addWidget(self.odorPortPretrainingLabel)
        self.rewardedOdorNamesLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.rewardedOdorNamesLabel.setFont(font)
        self.rewardedOdorNamesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rewardedOdorNamesLabel.setWordWrap(True)
        self.rewardedOdorNamesLabel.setObjectName("rewardedOdorNamesLabel")
        self.verticalLayout_6.addWidget(self.rewardedOdorNamesLabel)
        self.rewardedOdorPortsLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.rewardedOdorPortsLabel.setFont(font)
        self.rewardedOdorPortsLabel.setScaledContents(False)
        self.rewardedOdorPortsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rewardedOdorPortsLabel.setWordWrap(True)
        self.rewardedOdorPortsLabel.setObjectName("rewardedOdorPortsLabel")
        self.verticalLayout_6.addWidget(self.rewardedOdorPortsLabel)
        self.unrewardedOdorNamesLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.unrewardedOdorNamesLabel.setFont(font)
        self.unrewardedOdorNamesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.unrewardedOdorNamesLabel.setWordWrap(True)
        self.unrewardedOdorNamesLabel.setObjectName("unrewardedOdorNamesLabel")
        self.verticalLayout_6.addWidget(self.unrewardedOdorNamesLabel)
        self.unrewardedOdorPortsLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.unrewardedOdorPortsLabel.setFont(font)
        self.unrewardedOdorPortsLabel.setScaledContents(False)
        self.unrewardedOdorPortsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.unrewardedOdorPortsLabel.setWordWrap(True)
        self.unrewardedOdorPortsLabel.setObjectName("unrewardedOdorPortsLabel")
        self.verticalLayout_6.addWidget(self.unrewardedOdorPortsLabel)
        self.waterBinaryLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.waterBinaryLabel.setFont(font)
        self.waterBinaryLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.waterBinaryLabel.setObjectName("waterBinaryLabel")
        self.verticalLayout_6.addWidget(self.waterBinaryLabel)
        self.waterPortLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.waterPortLabel.setFont(font)
        self.waterPortLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.waterPortLabel.setObjectName("waterPortLabel")
        self.verticalLayout_6.addWidget(self.waterPortLabel)
        self.waterTrialStructureLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.waterTrialStructureLabel.setFont(font)
        self.waterTrialStructureLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.waterTrialStructureLabel.setObjectName("waterTrialStructureLabel")
        self.verticalLayout_6.addWidget(self.waterTrialStructureLabel)
        self.cameraBinaryLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.cameraBinaryLabel.setFont(font)
        self.cameraBinaryLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.cameraBinaryLabel.setObjectName("cameraBinaryLabel")
        self.verticalLayout_6.addWidget(self.cameraBinaryLabel)
        self.cameraTriggerPortLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.cameraTriggerPortLabel.setFont(font)
        self.cameraTriggerPortLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.cameraTriggerPortLabel.setObjectName("cameraTriggerPortLabel")
        self.verticalLayout_6.addWidget(self.cameraTriggerPortLabel)
        self.cameraTrialStructureLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.cameraTrialStructureLabel.setFont(font)
        self.cameraTrialStructureLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.cameraTrialStructureLabel.setObjectName("cameraTrialStructureLabel")
        self.verticalLayout_6.addWidget(self.cameraTrialStructureLabel)
        self.twoPhotonTriggerBinaryLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.twoPhotonTriggerBinaryLabel.setFont(font)
        self.twoPhotonTriggerBinaryLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.twoPhotonTriggerBinaryLabel.setObjectName("twoPhotonTriggerBinaryLabel")
        self.verticalLayout_6.addWidget(self.twoPhotonTriggerBinaryLabel)
        self.twoPhotonTriggerPortLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.twoPhotonTriggerPortLabel.setFont(font)
        self.twoPhotonTriggerPortLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.twoPhotonTriggerPortLabel.setObjectName("twoPhotonTriggerPortLabel")
        self.verticalLayout_6.addWidget(self.twoPhotonTriggerPortLabel)
        self.twoPhotonTrialStructureLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.twoPhotonTrialStructureLabel.setFont(font)
        self.twoPhotonTrialStructureLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.twoPhotonTrialStructureLabel.setObjectName("twoPhotonTrialStructureLabel")
        self.verticalLayout_6.addWidget(self.twoPhotonTrialStructureLabel)
        self.interTrialIntervalLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.interTrialIntervalLabel.setFont(font)
        self.interTrialIntervalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.interTrialIntervalLabel.setObjectName("interTrialIntervalLabel")
        self.verticalLayout_6.addWidget(self.interTrialIntervalLabel)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(mousebehaviorstartwindow)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(300, 30, 281, 901))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.outputFolderTextbox = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.outputFolderTextbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.outputFolderTextbox.setObjectName("outputFolderTextbox")
        self.verticalLayout_7.addWidget(self.outputFolderTextbox)
        self.dateTextbox = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.dateTextbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dateTextbox.setObjectName("dateTextbox")
        self.verticalLayout_7.addWidget(self.dateTextbox)
        self.mouseNumTextbox = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.mouseNumTextbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mouseNumTextbox.setObjectName("mouseNumTextbox")
        self.verticalLayout_7.addWidget(self.mouseNumTextbox)
        self.numTrialsTextbox = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.numTrialsTextbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.numTrialsTextbox.setObjectName("numTrialsTextbox")
        self.verticalLayout_7.addWidget(self.numTrialsTextbox)
        self.trialDurationTextbox = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.trialDurationTextbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.trialDurationTextbox.setObjectName("trialDurationTextbox")
        self.verticalLayout_7.addWidget(self.trialDurationTextbox)
        self.laserBinaryTextbox = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.laserBinaryTextbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.laserBinaryTextbox.setObjectName("laserBinaryTextbox")
        self.verticalLayout_7.addWidget(self.laserBinaryTextbox)
        self.laserPortTextbox = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.laserPortTextbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.laserPortTextbox.setObjectName("laserPortTextbox")
        self.verticalLayout_7.addWidget(self.laserPortTextbox)
        self.laserTrialStructureTextbox = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.laserTrialStructureTextbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.laserTrialStructureTextbox.setObjectName("laserTrialStructureTextbox")
        self.verticalLayout_7.addWidget(self.laserTrialStructureTextbox)
        self.odorBinaryTextbox = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.odorBinaryTextbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.odorBinaryTextbox.setObjectName("odorBinaryTextbox")
        self.verticalLayout_7.addWidget(self.odorBinaryTextbox)
        self.mineralOilPortTextbox = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.mineralOilPortTextbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mineralOilPortTextbox.setObjectName("mineralOilPortTextbox")
        self.verticalLayout_7.addWidget(self.mineralOilPortTextbox)
        # self.finalSolenoidsPortDeltaDelayDurationTextbox = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        # self.finalSolenoidsPortDeltaDelayDurationTextbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        # self.finalSolenoidsPortDeltaDelayDurationTextbox.setObjectName("finalSolenoidsPortDeltaDelayDurationTextbox")
        # self.verticalLayout_7.addWidget(self.finalSolenoidsPortDeltaDelayDurationTextbox)
        self.odorTrialStructureTextbox = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.odorTrialStructureTextbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.odorTrialStructureTextbox.setObjectName("odorTrialStructureTextbox")
        self.verticalLayout_7.addWidget(self.odorTrialStructureTextbox)
        self.odorNamePretrainingTextbox = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.odorNamePretrainingTextbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.odorNamePretrainingTextbox.setObjectName("odorNamePretrainingTextbox")
        self.verticalLayout_7.addWidget(self.odorNamePretrainingTextbox)
        self.odorPortPretrainingTextbox = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.odorPortPretrainingTextbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.odorPortPretrainingTextbox.setObjectName("odorPortPretrainingTextbox")
        self.verticalLayout_7.addWidget(self.odorPortPretrainingTextbox)
        self.rewardedOdorNamesTextbox = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.rewardedOdorNamesTextbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rewardedOdorNamesTextbox.setObjectName("rewardedOdorNamesTextbox")
        self.verticalLayout_7.addWidget(self.rewardedOdorNamesTextbox)
        self.rewardedOdorPortsTextbox = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.rewardedOdorPortsTextbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rewardedOdorPortsTextbox.setObjectName("rewardedOdorPortsTextbox")
        self.verticalLayout_7.addWidget(self.rewardedOdorPortsTextbox)
        self.unrewardedOdorNamesTextbox = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.unrewardedOdorNamesTextbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.unrewardedOdorNamesTextbox.setObjectName("unrewardedOdorNamesTextbox")
        self.verticalLayout_7.addWidget(self.unrewardedOdorNamesTextbox)
        self.unrewardedOdorPortsTextbox = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.unrewardedOdorPortsTextbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.unrewardedOdorPortsTextbox.setObjectName("unrewardedOdorPortsTextbox")
        self.verticalLayout_7.addWidget(self.unrewardedOdorPortsTextbox)
        self.waterBinaryTextbox = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.waterBinaryTextbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.waterBinaryTextbox.setObjectName("waterBinaryTextbox")
        self.verticalLayout_7.addWidget(self.waterBinaryTextbox)
        self.waterPortTextbox = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.waterPortTextbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.waterPortTextbox.setObjectName("waterPortTextbox")
        self.verticalLayout_7.addWidget(self.waterPortTextbox)
        self.waterTrialStructureTextbox = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.waterTrialStructureTextbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.waterTrialStructureTextbox.setObjectName("waterTrialStructureTextbox")
        self.verticalLayout_7.addWidget(self.waterTrialStructureTextbox)
        self.cameraBinaryTextbox = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.cameraBinaryTextbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cameraBinaryTextbox.setObjectName("cameraBinaryTextbox")
        self.verticalLayout_7.addWidget(self.cameraBinaryTextbox)
        self.cameraTriggerPortTextbox = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.cameraTriggerPortTextbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cameraTriggerPortTextbox.setObjectName("cameraTriggerPortTextbox")
        self.verticalLayout_7.addWidget(self.cameraTriggerPortTextbox)
        self.cameraTrialStructureTextbox = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.cameraTrialStructureTextbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cameraTrialStructureTextbox.setObjectName("cameraTrialStructureTextbox")
        self.verticalLayout_7.addWidget(self.cameraTrialStructureTextbox)
        self.twoPhotonTriggerBinaryTextbox = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.twoPhotonTriggerBinaryTextbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.twoPhotonTriggerBinaryTextbox.setObjectName("twoPhotonTriggerBinaryTextbox")
        self.verticalLayout_7.addWidget(self.twoPhotonTriggerBinaryTextbox)
        self.twoPhotonTriggerPortTextbox = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.twoPhotonTriggerPortTextbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.twoPhotonTriggerPortTextbox.setObjectName("twoPhotonTriggerPortTextbox")
        self.verticalLayout_7.addWidget(self.twoPhotonTriggerPortTextbox)
        self.twoPhotonTrialStructureTextbox = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.twoPhotonTrialStructureTextbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.twoPhotonTrialStructureTextbox.setObjectName("twoPhotonTrialStructureTextbox")
        self.verticalLayout_7.addWidget(self.twoPhotonTrialStructureTextbox)
        self.interTrialIntervalTextbox = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.interTrialIntervalTextbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.interTrialIntervalTextbox.setObjectName("interTrialIntervalTextbox")
        self.verticalLayout_7.addWidget(self.interTrialIntervalTextbox)
        self.startTrialTrainingButton = QtWidgets.QPushButton(mousebehaviorstartwindow)
        self.startTrialTrainingButton.setGeometry(QtCore.QRect(610, 180, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.startTrialTrainingButton.setFont(font)
        self.startTrialTrainingButton.setObjectName("startTrialTrainingButton")
        self.startTrialDiscriminationButton = QtWidgets.QPushButton(mousebehaviorstartwindow)
        self.startTrialDiscriminationButton.setGeometry(QtCore.QRect(610, 240, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.startTrialDiscriminationButton.setFont(font)
        self.startTrialDiscriminationButton.setObjectName("startTrialDiscriminationButton")
        self.resetButton = QtWidgets.QPushButton(mousebehaviorstartwindow)
        self.resetButton.setGeometry(QtCore.QRect(610, 732, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.resetButton.setFont(font)
        self.resetButton.setObjectName("resetButton")
        self.browseFileButton = QtWidgets.QPushButton(mousebehaviorstartwindow)
        self.browseFileButton.setGeometry(QtCore.QRect(590, 29, 91, 30))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.browseFileButton.setFont(font)
        self.browseFileButton.setObjectName("browseFileButton")
        self.defaultButton = QtWidgets.QPushButton(mousebehaviorstartwindow)
        self.defaultButton.setGeometry(QtCore.QRect(610, 672, 351, 51))
        self.defaultButton.setMaximumSize(QtCore.QSize(16777212, 16777215))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.defaultButton.setFont(font)
        self.defaultButton.setObjectName("defaultButton")
        self.resetDAQButton = QtWidgets.QPushButton(mousebehaviorstartwindow)
        self.resetDAQButton.setGeometry(QtCore.QRect(610, 300, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.resetDAQButton.setFont(font)
        self.resetDAQButton.setObjectName("resetDAQButton")

        self.retranslateUi(mousebehaviorstartwindow)
        QtCore.QMetaObject.connectSlotsByName(mousebehaviorstartwindow)

    def retranslateUi(self, mousebehaviorstartwindow):
        _translate = QtCore.QCoreApplication.translate
        mousebehaviorstartwindow.setWindowTitle(_translate("mousebehaviorstartwindow", "MainWindow"))
        self.outputFolderLabel.setText(_translate("mousebehaviorstartwindow", "output folder"))
        self.dateLabel.setText(_translate("mousebehaviorstartwindow", "date"))
        self.mouseNumLabel.setText(_translate("mousebehaviorstartwindow", "mouse #"))
        self.numTrialsLabel.setText(_translate("mousebehaviorstartwindow", "#trials"))
        self.trialTimeLabel.setText(_translate("mousebehaviorstartwindow", "trial duration (s)"))
        self.laserBinaryLabel.setText(_translate("mousebehaviorstartwindow", "laser?"))
        self.laserPortLabel.setText(_translate("mousebehaviorstartwindow", "laser port"))
        self.laserTrialStructureLabel.setText(_translate("mousebehaviorstartwindow", "laser delay (s), dur (s), freq, duty cycle"))
        self.odorBinaryLabel.setText(_translate("mousebehaviorstartwindow", "odor?"))
        self.mineralOilPortLabel.setText(_translate("mousebehaviorstartwindow", "control mineral oil port"))
        # self.finalSolenoidsPortDeltaDelayDurationLabel.setText(_translate("mousebehaviorstartwindow", "final valves port, deltaDelay (s), dur (s)"))
        self.odorTrialStructurePretrainingLabel.setText(_translate("mousebehaviorstartwindow", "odor delay (s), dur (s)"))
        self.odorNamePretrainingLabel.setText(_translate("mousebehaviorstartwindow", "odor name (pretraining)"))
        self.odorPortPretrainingLabel.setText(_translate("mousebehaviorstartwindow", "odor port (pretraining)"))
        self.rewardedOdorNamesLabel.setText(_translate("mousebehaviorstartwindow", "rewarded odor names (disc)"))
        self.rewardedOdorPortsLabel.setText(_translate("mousebehaviorstartwindow", "rewarded odor ports (disc)"))
        self.unrewardedOdorNamesLabel.setText(_translate("mousebehaviorstartwindow", "unrewarded odor names (disc)"))
        self.unrewardedOdorPortsLabel.setText(_translate("mousebehaviorstartwindow", "unrewarded odor ports (disc)"))
        self.waterBinaryLabel.setText(_translate("mousebehaviorstartwindow", "water?"))
        self.waterPortLabel.setText(_translate("mousebehaviorstartwindow", "water port"))
        self.waterTrialStructureLabel.setText(_translate("mousebehaviorstartwindow", "water delay (s), dur (s)"))
        self.cameraBinaryLabel.setText(_translate("mousebehaviorstartwindow", "camera?"))
        self.cameraTriggerPortLabel.setText(_translate("mousebehaviorstartwindow", "camera trigger port"))
        self.cameraTrialStructureLabel.setText(_translate("mousebehaviorstartwindow", "camera fps, duty cycle"))
        self.twoPhotonTriggerBinaryLabel.setText(_translate("mousebehaviorstartwindow", "2P + camera trigger?"))
        self.twoPhotonTriggerPortLabel.setText(_translate("mousebehaviorstartwindow", "2P + camera trigger port"))
        self.twoPhotonTrialStructureLabel.setText(_translate("mousebehaviorstartwindow", "2P trigger + camera freq, duty cycle"))
        self.interTrialIntervalLabel.setText(_translate("mousebehaviorstartwindow", "cycle ITI (s)"))
        self.outputFolderTextbox.setHtml(_translate("mousebehaviorstartwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.dateTextbox.setHtml(_translate("mousebehaviorstartwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.mouseNumTextbox.setHtml(_translate("mousebehaviorstartwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.numTrialsTextbox.setHtml(_translate("mousebehaviorstartwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3</p></body></html>"))
        self.trialDurationTextbox.setHtml(_translate("mousebehaviorstartwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10</p></body></html>"))
        self.laserBinaryTextbox.setHtml(_translate("mousebehaviorstartwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.laserPortTextbox.setHtml(_translate("mousebehaviorstartwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.laserTrialStructureTextbox.setHtml(_translate("mousebehaviorstartwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4.5,4,0,0</p></body></html>"))
        self.odorBinaryTextbox.setHtml(_translate("mousebehaviorstartwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.mineralOilPortTextbox.setHtml(_translate("mousebehaviorstartwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5</p></body></html>"))
#         self.finalSolenoidsPortDeltaDelayDurationTextbox.setHtml(_translate("mousebehaviorstartwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3,0.5,2</p></body></html>"))
        self.odorTrialStructureTextbox.setHtml(_translate("mousebehaviorstartwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2,2</p></body></html>"))
        self.odorNamePretrainingTextbox.setHtml(_translate("mousebehaviorstartwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pinene</p></body></html>"))
        self.odorPortPretrainingTextbox.setHtml(_translate("mousebehaviorstartwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6</p></body></html>"))
        self.rewardedOdorNamesTextbox.setHtml(_translate("mousebehaviorstartwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pinene,Limonene</p></body></html>"))
        self.rewardedOdorPortsTextbox.setHtml(_translate("mousebehaviorstartwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6,7</p></body></html>"))
        self.unrewardedOdorNamesTextbox.setHtml(_translate("mousebehaviorstartwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hexenol,Octanol</p></body></html>"))
        self.unrewardedOdorPortsTextbox.setHtml(_translate("mousebehaviorstartwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8,9</p></body></html>"))
        self.waterBinaryTextbox.setHtml(_translate("mousebehaviorstartwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.waterPortTextbox.setHtml(_translate("mousebehaviorstartwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4</p></body></html>"))
        self.waterTrialStructureTextbox.setHtml(_translate("mousebehaviorstartwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8,0.50</p></body></html>"))
        self.cameraBinaryTextbox.setHtml(_translate("mousebehaviorstartwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.cameraTriggerPortTextbox.setHtml(_translate("mousebehaviorstartwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2</p></body></html>"))
        self.cameraTrialStructureTextbox.setHtml(_translate("mousebehaviorstartwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0,0</p></body></html>"))
        self.twoPhotonTriggerBinaryTextbox.setHtml(_translate("mousebehaviorstartwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.twoPhotonTriggerPortTextbox.setHtml(_translate("mousebehaviorstartwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.twoPhotonTrialStructureTextbox.setHtml(_translate("mousebehaviorstartwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0,0</p></body></html>"))
        self.interTrialIntervalTextbox.setHtml(_translate("mousebehaviorstartwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3</p></body></html>"))
        self.startTrialTrainingButton.setText(_translate("mousebehaviorstartwindow", "Start Pretraining"))
        self.startTrialDiscriminationButton.setText(_translate("mousebehaviorstartwindow", "Start Discrimination"))
        self.resetButton.setText(_translate("mousebehaviorstartwindow", "Reset Fields"))
        self.browseFileButton.setText(_translate("mousebehaviorstartwindow", "Browse"))
        self.defaultButton.setText(_translate("mousebehaviorstartwindow", "Default"))
        self.resetDAQButton.setText(_translate("mousebehaviorstartwindow", "Reset DAQ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mousebehaviorstartwindow = QtWidgets.QDialog()
    ui = Ui_mousebehaviorstartwindow()
    ui.setupUi(mousebehaviorstartwindow)
    mousebehaviorstartwindow.show()
    sys.exit(app.exec_())
