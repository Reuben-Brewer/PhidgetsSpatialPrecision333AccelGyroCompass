# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision I, 08/17/2024

Verified working on: Python 2.7, 3.8 for Windows 8.1, 10 64-bit and Raspberry Pi Buster (does not work on Mac).
'''

__author__ = 'reuben.brewer'

###########################################################
from LowPassFilter_ReubenPython2and3Class import *
from ZeroAndSnapshotData_ReubenPython2and3Class import *
###########################################################

###########################################################
import os
import sys
import platform
import time
import datetime
import math
import collections
from copy import * #for deepcopy
import inspect #To enable 'TellWhichFileWereIn'
import threading
import traceback
###########################################################

###########################################################
if sys.version_info[0] < 3:
    from Tkinter import * #Python 2
    import tkFont
    import ttk
else:
    from tkinter import * #Python 3
    import tkinter.font as tkFont #Python 3
    from tkinter import ttk
###########################################################

###########################################################
if sys.version_info[0] < 3:
    import Queue  # Python 2
else:
    import queue as Queue  # Python 3
###########################################################

###########################################################
if sys.version_info[0] < 3:
    from builtins import raw_input as input
else:
    from future.builtins import input as input
########################################################### "sudo pip3 install future" (Python 3) AND "sudo pip install future" (Python 2)

###########################################################
import platform
if platform.system() == "Windows":
    import ctypes
    winmm = ctypes.WinDLL('winmm')
    winmm.timeBeginPeriod(1) #Set minimum timer resolution to 1ms so that time.sleep(0.001) behaves properly.
###########################################################

########################################################### ONLY FOR ConvertQuaterionsToEulerAngles_RollPitchYawAbtXYZ_ScipyCalculation
import numpy
from scipy.spatial.transform import Rotation #unicorn
########################################################### ONLY FOR ConvertQuaterionsToEulerAngles_RollPitchYawAbtXYZ_ScipyCalculation

###########################################################
from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Devices.Log import *
from Phidget22.LogLevel import *
from Phidget22.Devices.Accelerometer import *
from Phidget22.Devices.Gyroscope import *
from Phidget22.Devices.Magnetometer import *
from Phidget22.Devices.Spatial import *
from Phidget22.Devices.TemperatureSensor import *
###########################################################

class PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class(Frame): #Subclass the Tkinter Frame

    #######################################################################################################################
    #######################################################################################################################
    def __init__(self, setup_dict): #Subclass the Tkinter Frame

        print("#################### PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__ starting. ####################")

        #########################################################
        #########################################################
        self.EXIT_PROGRAM_FLAG = 0
        self.OBJECT_CREATED_SUCCESSFULLY_FLAG = -1
        self.EnableInternal_MyPrint_Flag = 0
        self.MainThread_still_running_flag = 0
        self.ZeroAndSnapshotData_OPEN_FLAG = -1
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.CurrentTime_CalculatedFromMainThread = -11111.0
        self.StartingTime_CalculatedFromMainThread = -11111.0
        self.LastTime_CalculatedFromMainThread = -11111.0
        self.DataStreamingFrequency_CalculatedFromMainThread = -11111.0
        self.DataStreamingDeltaT_CalculatedFromMainThread = -11111.0

        self.CurrentTime_TimestampFromPhidget_SpatialData_AccelGyroMag = -11111.0
        self.LastTime_TimestampFromPhidget_SpatialData_AccelGyroMag = -11111.0
        self.DataStreamingFrequency_TimestampFromPhidget_SpatialData_AccelGyroMag = -11111.0
        self.DataStreamingDeltaT_TimestampFromPhidget_SpatialData_AccelGyroMag = -11111.0

        self.CurrentTime_TimestampFromPhidget_AlgorithmData_Quaternions = -11111.0
        self.LastTime_TimestampFromPhidget_AlgorithmData_Quaternions = -11111.0
        self.DataStreamingFrequency_TimestampFromPhidget_AlgorithmData_Quaternions = -11111.0
        self.DataStreamingDeltaT_TimestampFromPhidget_AlgorithmData_Quaternions = -11111.0
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.DetectedDeviceName = "default"
        self.DetectedDeviceID = "default"
        self.DetectedDeviceVersion = "default"
        self.DetectedDeviceSerialNumber = "default"

        self.Spatial_CallbackUpdateDeltaTmilliseconds_ReceivedFromBoard = -1

        self.Algorithm_RxFromDevice_Int = -1
        self.Algorithm_RxFromDevice_Str = "default"

        self.HeatingEnabledToStabilizeSensorTemperature_RxFromDevice_Str = "default"

        self.SpatialData_AccelGyroMag_EventHandler_Queue = Queue.Queue()
        self.AlgorithmData_Quaternions_EventHandler_Queue = Queue.Queue()

        self.Acceleration_PhidgetUnits_DirectFromDataEventHandler = [-11111.0]*3
        self.Acceleration_PhidgetUnits_Raw = [-11111.0]*3
        self.Acceleration_PhidgetUnits_Smoothed = [-11111.0] * 3

        self.AngularRate_PhidgetUnits_DirectFromDataEventHandler = [-11111.0] * 3
        self.AngularRate_PhidgetUnits_Raw = [-11111.0]*3
        self.AngularRate_PhidgetUnits_Smoothed = [-11111.0] * 3

        self.MagneticField_PhidgetUnits_DirectFromDataEventHandler = [-11111.0] * 3
        self.MagneticField_PhidgetUnits_Raw = [-11111.0]*3
        self.MagneticField_PhidgetUnits_Smoothed = [-11111.0] * 3

        self.Quaternions_DirectFromDataEventHandler = [-11111.0]*4

        self.Roll_AbtXaxis_Degrees = -11111.0
        self.Pitch_AbtYaxis_Degrees = -11111.0
        self.Yaw_AbtZaxis_Degrees = -11111.0

        self.Roll_AbtXaxis_Degrees_Last = -11111.0
        self.Pitch_AbtYaxis_Degrees_Last = -11111.0
        self.Yaw_AbtZaxis_Degrees_Last = -11111.0

        self.RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond = -11111.0
        self.PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond = -11111.0
        self.YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond = -11111.0

        self.RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_SMOOTHED = -11111.0
        self.PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_SMOOTHED = -11111.0
        self.YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_SMOOTHED = -11111.0

        self.RollPitchYaw_AbtXYZ_Dict = dict() #What's getting returned in self.MostRecentDataDict
        self.RollPitchYaw_Rate_AbtXYZ_Dict = dict() #What's getting returned in self.MostRecentDataDict

        self.setAHRSParameters_NeedsToBeFiredFlag = 1

        self.MostRecentDataDict = dict()
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.DictPN_IndividualParametersDict = dict([("MOT0110_0", dict([("CallbackUpdateDeltaTmilliseconds_MinimumValue", 1), ("HeatingEnabledToStabilizeSensorTemperature_SupportedOnDevice", True)])),
                                                  ("MOT0109_0", dict([("CallbackUpdateDeltaTmilliseconds_MinimumValue", 4), ("HeatingEnabledToStabilizeSensorTemperature_SupportedOnDevice", True)])),
                                                  ("1044_1", dict([("CallbackUpdateDeltaTmilliseconds_MinimumValue", 5), ("HeatingEnabledToStabilizeSensorTemperature_SupportedOnDevice", False)])),
                                                  ("unknown", dict([("CallbackUpdateDeltaTmilliseconds_MinimumValue", 6), ("HeatingEnabledToStabilizeSensorTemperature_SupportedOnDevice", False)]))])

        print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: self.DictPN_IndividualParametersDict: " + str(self.DictPN_IndividualParametersDict))
        #########################################################
        #########################################################
        
        #########################################################
        #########################################################
        if platform.system() == "Linux":

            if "raspberrypi" in platform.uname(): #os.uname() doesn't work in windows
                self.my_platform = "pi"
            else:
                self.my_platform = "linux"

        elif platform.system() == "Windows":
            self.my_platform = "windows"

        elif platform.system() == "Darwin":
            self.my_platform = "mac"

        else:
            self.my_platform = "other"

        print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: The OS platform is: " + self.my_platform)
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "GUIparametersDict" in setup_dict:
            self.GUIparametersDict = setup_dict["GUIparametersDict"]

            #########################################################
            if "USE_GUI_FLAG" in self.GUIparametersDict:
                self.USE_GUI_FLAG = self.PassThrough0and1values_ExitProgramOtherwise("USE_GUI_FLAG", self.GUIparametersDict["USE_GUI_FLAG"])
            else:
                self.USE_GUI_FLAG = 0

            print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: USE_GUI_FLAG: " + str(self.USE_GUI_FLAG))
            #########################################################

            #########################################################
            if "root" in self.GUIparametersDict:
                self.root = self.GUIparametersDict["root"]
            else:
                print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: Error, must pass in 'root'")
                return
            #########################################################

            #########################################################
            if "EnableInternal_MyPrint_Flag" in self.GUIparametersDict:
                self.EnableInternal_MyPrint_Flag = self.PassThrough0and1values_ExitProgramOtherwise("EnableInternal_MyPrint_Flag", self.GUIparametersDict["EnableInternal_MyPrint_Flag"])
            else:
                self.EnableInternal_MyPrint_Flag = 0

            print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: EnableInternal_MyPrint_Flag: " + str(self.EnableInternal_MyPrint_Flag))
            #########################################################

            #########################################################
            if "PrintToConsoleFlag" in self.GUIparametersDict:
                self.PrintToConsoleFlag = self.PassThrough0and1values_ExitProgramOtherwise("PrintToConsoleFlag", self.GUIparametersDict["PrintToConsoleFlag"])
            else:
                self.PrintToConsoleFlag = 1

            print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: PrintToConsoleFlag: " + str(self.PrintToConsoleFlag))
            #########################################################

            #########################################################
            if "NumberOfPrintLines" in self.GUIparametersDict:
                self.NumberOfPrintLines = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("NumberOfPrintLines", self.GUIparametersDict["NumberOfPrintLines"], 0.0, 50.0))
            else:
                self.NumberOfPrintLines = 10

            print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: NumberOfPrintLines: " + str(self.NumberOfPrintLines))
            #########################################################

            #########################################################
            if "UseBorderAroundThisGuiObjectFlag" in self.GUIparametersDict:
                self.UseBorderAroundThisGuiObjectFlag = self.PassThrough0and1values_ExitProgramOtherwise("UseBorderAroundThisGuiObjectFlag", self.GUIparametersDict["UseBorderAroundThisGuiObjectFlag"])
            else:
                self.UseBorderAroundThisGuiObjectFlag = 0

            print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: UseBorderAroundThisGuiObjectFlag: " + str(self.UseBorderAroundThisGuiObjectFlag))
            #########################################################

            #########################################################
            if "GUI_ROW" in self.GUIparametersDict:
                self.GUI_ROW = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_ROW", self.GUIparametersDict["GUI_ROW"], 0.0, 1000.0))
            else:
                self.GUI_ROW = 0

            print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: GUI_ROW: " + str(self.GUI_ROW))
            #########################################################

            #########################################################
            if "GUI_COLUMN" in self.GUIparametersDict:
                self.GUI_COLUMN = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_COLUMN", self.GUIparametersDict["GUI_COLUMN"], 0.0, 1000.0))
            else:
                self.GUI_COLUMN = 0

            print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: GUI_COLUMN: " + str(self.GUI_COLUMN))
            #########################################################

            #########################################################
            if "GUI_PADX" in self.GUIparametersDict:
                self.GUI_PADX = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_PADX", self.GUIparametersDict["GUI_PADX"], 0.0, 1000.0))
            else:
                self.GUI_PADX = 0

            print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: GUI_PADX: " + str(self.GUI_PADX))
            #########################################################

            #########################################################
            if "GUI_PADY" in self.GUIparametersDict:
                self.GUI_PADY = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_PADY", self.GUIparametersDict["GUI_PADY"], 0.0, 1000.0))
            else:
                self.GUI_PADY = 0

            print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: GUI_PADY: " + str(self.GUI_PADY))
            #########################################################

            #########################################################
            if "GUI_ROWSPAN" in self.GUIparametersDict:
                self.GUI_ROWSPAN = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_ROWSPAN", self.GUIparametersDict["GUI_ROWSPAN"], 1.0, 1000.0))
            else:
                self.GUI_ROWSPAN = 1

            print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: GUI_ROWSPAN: " + str(self.GUI_ROWSPAN))
            #########################################################

            #########################################################
            if "GUI_COLUMNSPAN" in self.GUIparametersDict:
                self.GUI_COLUMNSPAN = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_COLUMNSPAN", self.GUIparametersDict["GUI_COLUMNSPAN"], 1.0, 1000.0))
            else:
                self.GUI_COLUMNSPAN = 1

            print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: GUI_COLUMNSPAN: " + str(self.GUI_COLUMNSPAN))
            #########################################################

            #########################################################
            if "GUI_STICKY" in self.GUIparametersDict:
                self.GUI_STICKY = str(self.GUIparametersDict["GUI_STICKY"])
            else:
                self.GUI_STICKY = "w"

            print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: GUI_STICKY: " + str(self.GUI_STICKY))
            #########################################################

        else:
            self.GUIparametersDict = dict()
            self.USE_GUI_FLAG = 0
            print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: No GUIparametersDict present, setting USE_GUI_FLAG: " + str(self.USE_GUI_FLAG))

        #print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: GUIparametersDict: " + str(self.GUIparametersDict))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "DesiredSerialNumber" in setup_dict:
            try:
                self.DesiredSerialNumber = int(setup_dict["DesiredSerialNumber"])
            except:
                print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: Error, DesiredSerialNumber invalid.")
        else:
            self.DesiredSerialNumber = -1
        
        print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: DesiredSerialNumber: " + str(self.DesiredSerialNumber))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "NameToDisplay_UserSet" in setup_dict:
            self.NameToDisplay_UserSet = str(setup_dict["NameToDisplay_UserSet"])
        else:
            self.NameToDisplay_UserSet = ""

        print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: NameToDisplay_UserSet: " + str(self.NameToDisplay_UserSet))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "WaitForAttached_TimeoutDuration_Milliseconds" in setup_dict:
            self.WaitForAttached_TimeoutDuration_Milliseconds = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("WaitForAttached_TimeoutDuration_Milliseconds", setup_dict["WaitForAttached_TimeoutDuration_Milliseconds"], 0.0, 60000.0))

        else:
            self.WaitForAttached_TimeoutDuration_Milliseconds = 5000

        print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: WaitForAttached_TimeoutDuration_Milliseconds: " + str(self.WaitForAttached_TimeoutDuration_Milliseconds))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "UsePhidgetsLoggingInternalToThisClassObjectFlag" in setup_dict:
            self.UsePhidgetsLoggingInternalToThisClassObjectFlag = self.PassThrough0and1values_ExitProgramOtherwise("UsePhidgetsLoggingInternalToThisClassObjectFlag", setup_dict["UsePhidgetsLoggingInternalToThisClassObjectFlag"])
        else:
            self.UsePhidgetsLoggingInternalToThisClassObjectFlag = 1

        print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: UsePhidgetsLoggingInternalToThisClassObjectFlag: " + str(self.UsePhidgetsLoggingInternalToThisClassObjectFlag))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "SpatialAlgorithm" in setup_dict:
            self.SpatialAlgorithm = str(setup_dict["SpatialAlgorithm"]).upper()

            if self.SpatialAlgorithm not in ["IMU", "AHRS", "NONE"]:
                print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: Error, 'SpatialAlgorithm' must be 'IMU', 'AHRS', or 'NONE'")
                return

        else:
            self.SpatialAlgorithm = "AHRS"
            
        print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: self.SpatialAlgorithm: " + str(self.SpatialAlgorithm))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag" in setup_dict:
            self.RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag = self.PassThrough0and1values_ExitProgramOtherwise("RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag", setup_dict["RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag"])
        else:
            self.RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag = 1

        print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag: " + str(self.RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag" in setup_dict:
            self.RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag = self.PassThrough0and1values_ExitProgramOtherwise("RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag", setup_dict["RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag"])
        else:
            self.RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag = 1

        print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag: " + str(self.RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda" in setup_dict:
            self.RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda", setup_dict["RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda"], 0.0, 1.0)

        else:
            self.RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda = 0.5 #Default to no filtering, new_filtered_value = k * raw_sensor_value + (1 - k) * old_filtered_value

        print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda: " + str(self.RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag" in setup_dict:
            self.PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag = self.PassThrough0and1values_ExitProgramOtherwise("PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag", setup_dict["PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag"])
        else:
            self.PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag = 1

        print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag: " + str(self.PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag" in setup_dict:
            self.PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag = self.PassThrough0and1values_ExitProgramOtherwise("PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag", setup_dict["PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag"])
        else:
            self.PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag = 1

        print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag: " + str(self.PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda" in setup_dict:
            self.PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda", setup_dict["PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda"], 0.0, 1.0)

        else:
            self.PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda = 0.5 #Default to no filtering, new_filtered_value = k * raw_sensor_value + (1 - k) * old_filtered_value

        print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda: " + str(self.PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag" in setup_dict:
            self.YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag = self.PassThrough0and1values_ExitProgramOtherwise("YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag", setup_dict["YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag"])
        else:
            self.YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag = 1

        print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag: " + str(self.YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag" in setup_dict:
            self.YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag = self.PassThrough0and1values_ExitProgramOtherwise("YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag", setup_dict["YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag"])
        else:
            self.YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag = 1

        print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag: " + str(self.YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda" in setup_dict:
            self.YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda", setup_dict["YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda"], 0.0, 1.0)

        else:
            self.YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda = 0.5 #Default to no filtering, new_filtered_value = k * raw_sensor_value + (1 - k) * old_filtered_value

        print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda: " + str(self.YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "AlgorithmMagnetometerGain" in setup_dict:
            self.AlgorithmMagnetometerGain = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("AlgorithmMagnetometerGain", setup_dict["AlgorithmMagnetometerGain"], 0.0, 1.0)

        else:
            self.AlgorithmMagnetometerGain = 0.005

        print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: AlgorithmMagnetometerGain: " + str(self.AlgorithmMagnetometerGain))
        #########################################################
        #########################################################
        
        #########################################################
        #########################################################
        if "DataCollectionDurationInSecondsForSnapshottingAndZeroing" in setup_dict:
            self.DataCollectionDurationInSecondsForSnapshottingAndZeroing = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("DataCollectionDurationInSecondsForSnapshottingAndZeroing", setup_dict["DataCollectionDurationInSecondsForSnapshottingAndZeroing"], 0.0, 60.0)

        else:
            self.DataCollectionDurationInSecondsForSnapshottingAndZeroing = 1.0

        print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: DataCollectionDurationInSecondsForSnapshottingAndZeroing: " + str(self.DataCollectionDurationInSecondsForSnapshottingAndZeroing))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "MainThread_TimeToSleepEachLoop" in setup_dict:
            self.MainThread_TimeToSleepEachLoop = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("MainThread_TimeToSleepEachLoop", setup_dict["MainThread_TimeToSleepEachLoop"], 0.001, 100000)

        else:
            self.MainThread_TimeToSleepEachLoop = 0.008

        print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: MainThread_TimeToSleepEachLoop: " + str(self.MainThread_TimeToSleepEachLoop))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "ZeroGyrosAtStartOfProgramFlag" in setup_dict:
            self.ZeroGyrosAtStartOfProgramFlag = self.PassThrough0and1values_ExitProgramOtherwise("ZeroGyrosAtStartOfProgramFlag", setup_dict["ZeroGyrosAtStartOfProgramFlag"])
        else:
            self.ZeroGyrosAtStartOfProgramFlag = 1

        print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: ZeroGyrosAtStartOfProgramFlag: " + str(self.ZeroGyrosAtStartOfProgramFlag))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "ZeroAlgorithmAtStartOfProgramFlag" in setup_dict:
            self.ZeroAlgorithmAtStartOfProgramFlag = self.PassThrough0and1values_ExitProgramOtherwise("ZeroAlgorithmAtStartOfProgramFlag", setup_dict["ZeroAlgorithmAtStartOfProgramFlag"])
        else:
            self.ZeroAlgorithmAtStartOfProgramFlag = 1

        print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: ZeroAlgorithmAtStartOfProgramFlag: " + str(self.ZeroAlgorithmAtStartOfProgramFlag))
        #########################################################
        #########################################################
        
        #########################################################
        #########################################################
        if "AHRS_Parameters_angularVelocityThreshold" in setup_dict:
            self.AHRS_Parameters_angularVelocityThreshold = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("AHRS_Parameters_angularVelocityThreshold", setup_dict["AHRS_Parameters_angularVelocityThreshold"], 0.0, 1000000000.0)

        else:
            self.AHRS_Parameters_angularVelocityThreshold = 0.0

        print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: AHRS_Parameters_angularVelocityThreshold: " + str(self.AHRS_Parameters_angularVelocityThreshold))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "AHRS_Parameters_angularVelocityDeltaThreshold" in setup_dict:
            self.AHRS_Parameters_angularVelocityDeltaThreshold = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("AHRS_Parameters_angularVelocityDeltaThreshold", setup_dict["AHRS_Parameters_angularVelocityDeltaThreshold"], 0.0, 1000000000.0)

        else:
            self.AHRS_Parameters_angularVelocityDeltaThreshold = 0.0

        print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: AHRS_Parameters_angularVelocityDeltaThreshold: " + str(self.AHRS_Parameters_angularVelocityDeltaThreshold))
        #########################################################
        #########################################################
        
        #########################################################
        #########################################################
        if "AHRS_Parameters_accelerationThreshold" in setup_dict:
            self.AHRS_Parameters_accelerationThreshold = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("AHRS_Parameters_accelerationThreshold", setup_dict["AHRS_Parameters_accelerationThreshold"], 0.0, 1000000000.0)

        else:
            self.AHRS_Parameters_accelerationThreshold = 0.0

        print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: AHRS_Parameters_accelerationThreshold: " + str(self.AHRS_Parameters_accelerationThreshold))
        #########################################################
        #########################################################
        
        #########################################################
        #########################################################
        if "AHRS_Parameters_magTime" in setup_dict:
            self.AHRS_Parameters_magTime = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("AHRS_Parameters_magTime", setup_dict["AHRS_Parameters_magTime"], 0.0, 1000000000.0)

        else:
            self.AHRS_Parameters_magTime = 0.0

        print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: AHRS_Parameters_magTime: " + str(self.AHRS_Parameters_magTime))
        #########################################################
        #########################################################
        
        #########################################################
        #########################################################
        if "AHRS_Parameters_accelTime" in setup_dict:
            self.AHRS_Parameters_accelTime = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("AHRS_Parameters_accelTime", setup_dict["AHRS_Parameters_accelTime"], 0.0, 1000000000.0)

        else:
            self.AHRS_Parameters_accelTime = 0.0

        print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: AHRS_Parameters_accelTime: " + str(self.AHRS_Parameters_accelTime))
        #########################################################
        #########################################################
        
        #########################################################
        #########################################################
        if "AHRS_Parameters_biasTime" in setup_dict:
            self.AHRS_Parameters_biasTime = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("AHRS_Parameters_biasTime", setup_dict["AHRS_Parameters_biasTime"], 0.0, 1000000000.0)

        else:
            self.AHRS_Parameters_biasTime = 0.0

        print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: AHRS_Parameters_biasTime: " + str(self.AHRS_Parameters_biasTime))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.ZeroGyros_NeedsToBeChangedFlag = self.ZeroGyrosAtStartOfProgramFlag
        self.ZeroAlgorithm_NeedsToBeChangedFlag = self.ZeroAlgorithmAtStartOfProgramFlag
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.PrintToGui_Label_TextInputHistory_List = [" "]*self.NumberOfPrintLines
        self.PrintToGui_Label_TextInput_Str = ""
        self.GUI_ready_to_be_updated_flag = 0
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_MyLowPassFilterClass_Object = LowPassFilter_ReubenPython2and3Class(dict([
                    ("UseMedianFilterFlag", self.RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag),
                    ("UseExponentialSmoothingFilterFlag", self.RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag),
                    ("ExponentialSmoothingFilterLambda", self.RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda)]))

        self.PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_MyLowPassFilterClass_Object = LowPassFilter_ReubenPython2and3Class(dict([
                    ("UseMedianFilterFlag", self.PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag),
                    ("UseExponentialSmoothingFilterFlag", self.PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag),
                    ("ExponentialSmoothingFilterLambda", self.PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda)]))

        self.YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_MyLowPassFilterClass_Object = LowPassFilter_ReubenPython2and3Class(dict([
                    ("UseMedianFilterFlag", self.YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag),
                    ("UseExponentialSmoothingFilterFlag", self.YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag),
                    ("ExponentialSmoothingFilterLambda", self.YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda)]))
        #########################################################
        #########################################################

        ######################################################### MUST OPEN THE DEVICE BEFORE WE CAN QUERY ITS INFORMATION
        #########################################################
        try:
            Spatial_OpenedTemporarilyJustToGetDeviceInfo = Spatial()

            if self.DesiredSerialNumber != -1:
                Spatial_OpenedTemporarilyJustToGetDeviceInfo.setDeviceSerialNumber(self.DesiredSerialNumber)

            Spatial_OpenedTemporarilyJustToGetDeviceInfo.openWaitForAttachment(self.WaitForAttached_TimeoutDuration_Milliseconds)

            self.DetectedDeviceName = Spatial_OpenedTemporarilyJustToGetDeviceInfo.getDeviceName()
            print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: DetectedDeviceName: " + self.DetectedDeviceName)

            self.DetectedDeviceSerialNumber = Spatial_OpenedTemporarilyJustToGetDeviceInfo.getDeviceSerialNumber()
            print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: DetectedDeviceSerialNumber: " + str(self.DetectedDeviceSerialNumber))

            self.DetectedDeviceID = Spatial_OpenedTemporarilyJustToGetDeviceInfo.getDeviceID()
            print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: DetectedDeviceID: " + str(self.DetectedDeviceID))

            ###########
            if self.DetectedDeviceID == 22:
                self.DevicePN = "1044_1"
            elif self.DetectedDeviceID  == 140:
                self.DevicePN = "MOT0109_0"
            elif self.DetectedDeviceID  == 141:
                self.DevicePN = "MOT0110_0"
            else:
                self.DevicePN = "unknown"

            print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: self.DevicePN: " + str(self.DevicePN))
            ##########

            self.DetectedDeviceVersion = Spatial_OpenedTemporarilyJustToGetDeviceInfo.getDeviceVersion()
            print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: DetectedDeviceVersion: " + str(self.DetectedDeviceVersion))

            self.DetectedDeviceLibraryVersion = Spatial_OpenedTemporarilyJustToGetDeviceInfo.getLibraryVersion()
            print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: DetectedDeviceLibraryVersion: " + str(self.DetectedDeviceLibraryVersion))

            Spatial_OpenedTemporarilyJustToGetDeviceInfo.close()

        except PhidgetException as e:
            print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: Failed to call Device Information, Phidget Exception %i: %s" % (e.code, e.details))
            return
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if self.DesiredSerialNumber != -1: #'-1' means we should open the device regardless os serial number.
            if self.DetectedDeviceSerialNumber != self.DesiredSerialNumber:
                print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: The desired Serial Number (" + str(self.DesiredSerialNumber) + ") does not match the detected serial number (" + str(self.DetectedDeviceSerialNumber) + ").")
                return
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        try:

            ###########
            self.CallbackUpdateDeltaTmilliseconds_MinimumValue = self.DictPN_IndividualParametersDict[self.DevicePN]["CallbackUpdateDeltaTmilliseconds_MinimumValue"]
            print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: self.CallbackUpdateDeltaTmilliseconds_MinimumValue: " + str(self.CallbackUpdateDeltaTmilliseconds_MinimumValue))
            ##########

            ##########
            if "Spatial_CallbackUpdateDeltaTmilliseconds" in setup_dict:
                self.Spatial_CallbackUpdateDeltaTmilliseconds = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("Spatial_CallbackUpdateDeltaTmilliseconds", setup_dict["Spatial_CallbackUpdateDeltaTmilliseconds"], self.CallbackUpdateDeltaTmilliseconds_MinimumValue, 1000.0))

            else:
                self.Spatial_CallbackUpdateDeltaTmilliseconds = self.CallbackUpdateDeltaTmilliseconds_MinimumValue

            print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: Spatial_CallbackUpdateDeltaTmilliseconds: " + str(self.Spatial_CallbackUpdateDeltaTmilliseconds))
            ##########

        except:
            exceptions = sys.exc_info()[0]
            print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: Error, Spatial_CallbackUpdateDeltaTmilliseconds parsing Exceptions: %s" % exceptions)
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        try:

            ###########
            self.HeatingEnabledToStabilizeSensorTemperature_SupportedOnDevice = self.DictPN_IndividualParametersDict[self.DevicePN]["HeatingEnabledToStabilizeSensorTemperature_SupportedOnDevice"]
            print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: HeatingEnabledToStabilizeSensorTemperature_SupportedOnDevice: " + str(self.HeatingEnabledToStabilizeSensorTemperature_SupportedOnDevice))
            ##########

            ##########
            if self.HeatingEnabledToStabilizeSensorTemperature_SupportedOnDevice == True:
                if "HeatingEnabledToStabilizeSensorTemperature" in setup_dict:
                    self.HeatingEnabledToStabilizeSensorTemperature = bool(self.PassThrough0and1values_ExitProgramOtherwise("HeatingEnabledToStabilizeSensorTemperature", setup_dict["HeatingEnabledToStabilizeSensorTemperature"]))

                else:
                    self.HeatingEnabledToStabilizeSensorTemperature = False
            else:
                self.HeatingEnabledToStabilizeSensorTemperature = False

            print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: HeatingEnabledToStabilizeSensorTemperature: " + str(self.HeatingEnabledToStabilizeSensorTemperature))
            ##########

        except:
            exceptions = sys.exc_info()[0]
            print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: Error, Spatial_CallbackUpdateDeltaTmilliseconds parsing Exceptions: %s" % exceptions)
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        try:

            #########################################################
            self.Spatial_PhidgetsSpatialObject = Spatial()
            self.Spatial_PhidgetsSpatialObject.setDeviceSerialNumber(self.DesiredSerialNumber)
            self.Spatial_PhidgetsSpatialObject.setOnAttachHandler(self.SpatialOnAttachCallback)
            self.Spatial_PhidgetsSpatialObject.setOnDetachHandler(self.SpatialOnDetachCallback)
            self.Spatial_PhidgetsSpatialObject.setOnErrorHandler(self.SpatialOnErrorCallback)
            #self.Spatial_PhidgetsSpatialObject.setOnSpatialDataHandler(self.SpatialOnSpatialDataCallback) #DON'T CURRENTLY NEED THIS DATA (INDIVIDUAL SENSOR OUTPUTS NOT COMBINED INTO AHRS)
            self.Spatial_PhidgetsSpatialObject.setOnAlgorithmDataHandler(self.SpatialOnAlgorithmDataCallback)
            self.Spatial_PhidgetsSpatialObject.openWaitForAttachment(self.WaitForAttached_TimeoutDuration_Milliseconds)
            #########################################################
        
            self.PhidgetsDeviceConnectedFlag = 1

        except PhidgetException as e:
            self.PhidgetsDeviceConnectedFlag = 0
            print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: Failed to attach, Phidget Exception %i: %s" % (e.code, e.details))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if self.PhidgetsDeviceConnectedFlag == 1:

            #########################################################
            if self.UsePhidgetsLoggingInternalToThisClassObjectFlag == 1:
                try:
                    Log.enable(LogLevel.PHIDGET_LOG_INFO, os.getcwd() + "\PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class_PhidgetLog_INFO.txt")
                    print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: Enabled Phidget Logging.")
                except PhidgetException as e:
                    print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: Failed to enable Phidget Logging, Phidget Exception %i: %s" % (e.code, e.details))
            #########################################################

            #########################################################
            self.MainThread_ThreadingObject = threading.Thread(target=self.MainThread, args=())
            self.MainThread_ThreadingObject.start()
            #########################################################

            #########################################################
            if self.USE_GUI_FLAG == 1:
                self.StartGUI(self.root)
            #########################################################

            #################################################
            #################################################
            self.ZeroAndSnapshotData_ReubenPython2and3ClassObject_Variables_ListOfDicts = [dict([("Variable_Name", "Roll_AbtXaxis_Degrees"),("DataCollectionDurationInSecondsForSnapshotting", self.DataCollectionDurationInSecondsForSnapshottingAndZeroing)]),
                                                                                      dict([("Variable_Name", "Pitch_AbtYaxis_Degrees"),("DataCollectionDurationInSecondsForSnapshotting", self.DataCollectionDurationInSecondsForSnapshottingAndZeroing)]),
                                                                                      dict([("Variable_Name", "Yaw_AbtZaxis_Degrees"),("DataCollectionDurationInSecondsForSnapshotting", self.DataCollectionDurationInSecondsForSnapshottingAndZeroing)])]

            self.ZeroAndSnapshotData_ReubenPython2and3ClassObject_GUIparametersDict = dict([("USE_GUI_FLAG", self.USE_GUI_FLAG), #def gui
                                            ("root", self.root),
                                            ("EnableInternal_MyPrint_Flag", 1),
                                            ("NumberOfPrintLines", 10),
                                            ("UseBorderAroundThisGuiObjectFlag", 1),
                                            ("GUI_ROW", 5),
                                            ("GUI_COLUMN", 0),
                                            ("GUI_PADX", 5),
                                            ("GUI_PADY", 5),
                                            ("GUI_ROWSPAN", 1),
                                            ("GUI_COLUMNSPAN", 1)])

            self.ZeroAndSnapshotData_ReubenPython2and3ClassObject_setup_dict = dict([("GUIparametersDict", self.ZeroAndSnapshotData_ReubenPython2and3ClassObject_GUIparametersDict),
                                                                        ("NameToDisplay_UserSet", "ZeroAndSnapshotData"),
                                                                        ("Variables_ListOfDicts", self.ZeroAndSnapshotData_ReubenPython2and3ClassObject_Variables_ListOfDicts)])


            try:
                self.ZeroAndSnapshotData_ReubenPython2and3ClassObject = ZeroAndSnapshotData_ReubenPython2and3Class(self.ZeroAndSnapshotData_ReubenPython2and3ClassObject_setup_dict)
                self.ZeroAndSnapshotData_OPEN_FLAG = self.ZeroAndSnapshotData_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

            except:
                exceptions = sys.exc_info()[0]
                print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class __init__: Exceptions: %s" % exceptions, 0)
                traceback.print_exc()
            #################################################
            #################################################

            #########################################################
            self.OBJECT_CREATED_SUCCESSFULLY_FLAG = 1
            #########################################################

        #########################################################
        #########################################################

    #######################################################################################################################
    #######################################################################################################################

    #######################################################################################################################
    #######################################################################################################################
    def __del__(self):
        pass
    #######################################################################################################################
    #######################################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def PassThrough0and1values_ExitProgramOtherwise(self, InputNameString, InputNumber):

        try:
            InputNumber_ConvertedToFloat = float(InputNumber)
        except:
            exceptions = sys.exc_info()[0]
            print("PassThrough0and1values_ExitProgramOtherwise Error. InputNumber must be a float value, Exceptions: %s" % exceptions)
            input("Press any key to continue")
            sys.exit()

        try:
            if InputNumber_ConvertedToFloat == 0.0 or InputNumber_ConvertedToFloat == 1:
                return InputNumber_ConvertedToFloat
            else:
                input("PassThrough0and1values_ExitProgramOtherwise Error. '" +
                          InputNameString +
                          "' must be 0 or 1 (value was " +
                          str(InputNumber_ConvertedToFloat) +
                          "). Press any key (and enter) to exit.")

                sys.exit()
        except:
            exceptions = sys.exc_info()[0]
            print("PassThrough0and1values_ExitProgramOtherwise Error, Exceptions: %s" % exceptions)
            input("Press any key to continue")
            sys.exit()
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def PassThroughFloatValuesInRange_ExitProgramOtherwise(self, InputNameString, InputNumber, RangeMinValue, RangeMaxValue):
        try:
            InputNumber_ConvertedToFloat = float(InputNumber)
        except:
            exceptions = sys.exc_info()[0]
            print("PassThroughFloatValuesInRange_ExitProgramOtherwise Error. InputNumber must be a float value, Exceptions: %s" % exceptions)
            input("Press any key to continue")
            sys.exit()

        try:
            if InputNumber_ConvertedToFloat >= RangeMinValue and InputNumber_ConvertedToFloat <= RangeMaxValue:
                return InputNumber_ConvertedToFloat
            else:
                input("PassThroughFloatValuesInRange_ExitProgramOtherwise Error. '" +
                          InputNameString +
                          "' must be in the range [" +
                          str(RangeMinValue) +
                          ", " +
                          str(RangeMaxValue) +
                          "] (value was " +
                          str(InputNumber_ConvertedToFloat) + "). Press any key (and enter) to exit.")

                sys.exit()
        except:
            exceptions = sys.exc_info()[0]
            print("PassThroughFloatValuesInRange_ExitProgramOtherwise Error, Exceptions: %s" % exceptions)
            input("Press any key to continue")
            sys.exit()
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def TellWhichFileWereIn(self):

        #We used to use this method, but it gave us the root calling file, not the class calling file
        #absolute_file_path = os.path.dirname(os.path.realpath(sys.argv[0]))
        #filename = absolute_file_path[absolute_file_path.rfind("\\") + 1:]

        frame = inspect.stack()[1]
        filename = frame[1][frame[1].rfind("\\") + 1:]
        filename = filename.replace(".py","")

        return filename
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def SpatialOnAttachCallback(self, HandlerSelf):

        try:
            ##########################################################################################################

            ###############################
            self.Spatial_PhidgetsSpatialObject.setDataInterval(self.Spatial_CallbackUpdateDeltaTmilliseconds)
            #self.Spatial_PhidgetsSpatialObject.setDataRate()
            self.Spatial_CallbackUpdateDeltaTmilliseconds_ReceivedFromBoard = self.Spatial_PhidgetsSpatialObject.getDataInterval()
            ###############################

            ###############################
            if self.SpatialAlgorithm == "NONE":
                self.Spatial_PhidgetsSpatialObject.setAlgorithm(SpatialAlgorithm.SPATIAL_ALGORITHM_NONE) #Must be called AFTER opening the device. SPATIAL_ALGORITHM_NONE, SPATIAL_ALGORITHM_IMU, or SPATIAL_ALGORITHM_AHRS
                print("Trying to set the algorithm to SPATIAL_ALGORITHM_NONE")
            elif self.SpatialAlgorithm == "IMU":
                self.Spatial_PhidgetsSpatialObject.setAlgorithm(SpatialAlgorithm.SPATIAL_ALGORITHM_IMU) #Must be called AFTER opening the device. SPATIAL_ALGORITHM_NONE, SPATIAL_ALGORITHM_IMU, or SPATIAL_ALGORITHM_AHRS
                print("Trying to set the algorithm to SPATIAL_ALGORITHM_IMU")
            else:
                self.Spatial_PhidgetsSpatialObject.setAlgorithm(SpatialAlgorithm.SPATIAL_ALGORITHM_AHRS) #Must be called AFTER opening the device. SPATIAL_ALGORITHM_NONE, SPATIAL_ALGORITHM_IMU, or SPATIAL_ALGORITHM_AHRS
                print("Trying to set the algorithm to SPATIAL_ALGORITHM_AHRS")
            ###############################

            ###############################
            self.Algorithm_RxFromDevice_Int = self.Spatial_PhidgetsSpatialObject.getAlgorithm()
            if self.Algorithm_RxFromDevice_Int == 0:
                self.Algorithm_RxFromDevice_Str = "SPATIAL_ALGORITHM_NONE" #No AHRS algorithm is used.
            elif self.Algorithm_RxFromDevice_Int == 1:
                self.Algorithm_RxFromDevice_Str = "SPATIAL_ALGORITHM_AHRS" #AHRS algorithm, incorporating magnetometer data for yaw correction.
            elif self.Algorithm_RxFromDevice_Int == 2:
                self.Algorithm_RxFromDevice_Str = "SPATIAL_ALGORITHM_IMU" #IMU algorithm, using gyro and accelerometer, but not magnetometer.
            else:
                self.Algorithm_RxFromDevice_Str = "Unrecognized integer"

            print("Reading from the actual device, the algorithm is: " + self.Algorithm_RxFromDevice_Str)
            ###############################

            ###############################
            if self.HeatingEnabledToStabilizeSensorTemperature_SupportedOnDevice == True:
                self.Spatial_PhidgetsSpatialObject.setHeatingEnabled(self.HeatingEnabledToStabilizeSensorTemperature)
                self.HeatingEnabledToStabilizeSensorTemperature_RxFromDevice_Str = self.Spatial_PhidgetsSpatialObject.getHeatingEnabled()
                print("self.HeatingEnabledToStabilizeSensorTemperature_RxFromDevice_Str: " + str(self.HeatingEnabledToStabilizeSensorTemperature_RxFromDevice_Str))
            ###############################

            ###############################
            if self.DevicePN == "1044_1" or self.DevicePN == "MOT0109_0":
                self.Spatial_PhidgetsSpatialObject.setAlgorithmMagnetometerGain(self.AlgorithmMagnetometerGain)
                self.AlgorithmMagnetometerGain_RxFromDevice_Str = self.Spatial_PhidgetsSpatialObject.getAlgorithmMagnetometerGain()
            else:
                self.AlgorithmMagnetometerGain_RxFromDevice_Str = "setAlgorithmMagnetometerGain no supported on " + str(self.DevicePN)

            print("self.AlgorithmMagnetometerGain_RxFromDevice_Str: " + str(self.AlgorithmMagnetometerGain_RxFromDevice_Str))
            ###############################

            ###############################
            self.Spatial_AttachedAndOpenFlag = 1
            self.MyPrint_WithoutLogFile("$$$$$$$$$$ SpatialOnAttachCallback event for SpatialChannel, Attached! $$$$$$$$$$")
            ###############################

        ##########################################################################################################

        ##########################################################################################################
        except PhidgetException as e:
            self.Spatial_AttachedAndOpenFlag = 0
            self.MyPrint_WithoutLogFile("SpatialOnAttachCallback event, ERROR: Failed to attach, Phidget Exception %i: %s" % (e.code, e.details))
        ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def SpatialOnDetachCallback(self, HandlerSelf):

        self.Spatial_AttachedAndOpenFlag = 0

        self.MyPrint_WithoutLogFile("$$$$$$$$$$ SpatialOnDetachCallback event, Detatched! $$$$$$$$$$")

        try:
            self.Spatial_PhidgetsSpatialObject.openWaitForAttachment(self.WaitForAttached_TimeoutDuration_Milliseconds)
            time.sleep(0.250)

        except PhidgetException as e:
            self.MyPrint_WithoutLogFile("SpatialOnDetachCallback event, failed to openWaitForAttachment, Phidget Exception %i: %s" % (e.code, e.details))
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def SpatialOnErrorCallback(self, HandlerSelf, code, description):

        self.Spatial_ErrorCallbackFiredFlag = 1

        self.MyPrint_WithoutLogFile("SpatialOnErrorCallback event, Error Code " + ErrorEventCode.getName(code) + ", description: " + str(description))
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def SpatialOnSpatialDataCallback(self, HandlerSelf, acceleration, angularRate, magneticField, timestamp):

        try:
            #########################################################
            self.CurrentTime_TimestampFromPhidget_SpatialData_AccelGyroMag = timestamp/1000.0 #Convert milliseconds to seconds
            self.Acceleration_PhidgetUnits_DirectFromDataEventHandler = acceleration
            self.AngularRate_PhidgetUnits_DirectFromDataEventHandler = angularRate
            self.MagneticField_PhidgetUnits_DirectFromDataEventHandler = magneticField

            self.SpatialData_AccelGyroMag_EventHandler_Queue.put([self.Acceleration_PhidgetUnits_DirectFromDataEventHandler, self.AngularRate_PhidgetUnits_DirectFromDataEventHandler, self.MagneticField_PhidgetUnits_DirectFromDataEventHandler, self.CurrentTime_TimestampFromPhidget_SpatialData_AccelGyroMag])
            self.UpdateFrequencyCalculation_TimestampFromPhidget_SpatialData_AccelGyroMag()

            #print("SpatialOnSpatialDataCallback event fired: acceleration = " + str(acceleration) + ", angularRate = " + str(angularRate) + ", magneticField = " + str(magneticField) + ", timestamp = " + str(timestamp))
            #########################################################

        except PhidgetException as e:
            print("SpatialOnSpatialDataCallback ERROR, Phidget Exception %i: %s" % (e.code, e.details))
    ##########################################################################################################
    ##########################################################################################################

    ########################################################################################################## unicorn
    ##########################################################################################################
    def SpatialOnAlgorithmDataCallback(self, HandlerSelf, quaternion, timestamp):

        try:
            #########################################################
            self.CurrentTime_TimestampFromPhidget_AlgorithmData_Quaternions = timestamp/1000.0 #Convert milliseconds to seconds
            self.UpdateFrequencyCalculation_TimestampFromPhidget_AlgorithmData_Quaternions()

            Quaternions_DirectFromDataEventHandler_temp = quaternion



            '''
            print("Timestamp: " + str(timestamp))

            eulerAngles = self.Spatial_PhidgetsSpatialObject.getEulerAngles()
            print("EulerAngles: ")
            print("pitch: " + str(eulerAngles.pitch))
            print("roll: " + str(eulerAngles.roll))
            print("heading: " + str(eulerAngles.heading))
        
            quaternion = self.Spatial_PhidgetsSpatialObject.getQuaternion()
            print("Quaternion: ")
            print("x: " + str(quaternion.x))
            print("y: " + str(quaternion.y))
            print("z: " + str(quaternion.z))
            print("w: " + str(quaternion.w))
            print("----------")
            '''

            self.AlgorithmData_Quaternions_EventHandler_Queue.put([Quaternions_DirectFromDataEventHandler_temp, self.CurrentTime_TimestampFromPhidget_AlgorithmData_Quaternions, self.DataStreamingDeltaT_TimestampFromPhidget_AlgorithmData_Quaternions])

            #print("SpatialOnAlgorithmDataCallback event fired: quaternion = " + str(quaternion) + ", timestamp = " + str(timestamp))
            #########################################################


        except PhidgetException as e:
            print("SpatialOnAlgorithmDataCallback ERROR, Phidget Exception %i: %s" % (e.code, e.details))
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def SetAHRSParameters_MyFunction(self, AHRS_Parameters_angularVelocityThreshold, AHRS_Parameters_angularVelocityDeltaThreshold, AHRS_Parameters_accelerationThreshold, AHRS_Parameters_magTime, AHRS_Parameters_accelTime, AHRS_Parameters_biasTime):
        '''
        AHRS_Parameters_angularVelocityThreshold(type: float):The maximum angular velocity reading where the device is assumed to be "at rest"
        AHRS_Parameters_angularVelocityDeltaThreshold(type: float):The acceptable amount of change in angular velocity between measurements before movement is assumed.
        AHRS_Parameters_accelerationThreshold(type: float):The maximum acceleration applied to the device (minus gravity) where it is assumed to be "at rest". This is also the maximum acceleration allowable before the device stops correcting to the acceleration vector.
        AHRS_Parameters_magTime(type: float):The time it will take to correct the heading 95% of the way to aligning with the compass (in seconds),up to 15 degrees of error. Beyond 15 degrees, this is the time it will take for the bearing to move 45 degrees towards the compass reading. Remember you can zero the algorithm at any time to instantly realign the spatial with acceleration and magnetic field vectors regardless of magnitude.
        AHRS_Parameters_accelTime(type: float):The time it will take to correct the pitch and roll 95% of the way to aligning with the accelerometer (in seconds).
        AHRS_Parameters_biasTime(type: float):The time it will take to have the gyro biases settle to within 95% of the measured steady state (in seconds).
        '''

        self.AHRS_Parameters_angularVelocityThreshold = self.LimitNumber_FloatOutputOnly(0.0, 1000000000.0, AHRS_Parameters_angularVelocityThreshold)
        self.AHRS_Parameters_angularVelocityDeltaThreshold = self.LimitNumber_FloatOutputOnly(0.0, 1000000000.0, AHRS_Parameters_angularVelocityDeltaThreshold)
        self.AHRS_Parameters_accelerationThreshold = self.LimitNumber_FloatOutputOnly(0.0, 1000000000.0, AHRS_Parameters_accelerationThreshold)
        self.AHRS_Parameters_magTime = self.LimitNumber_FloatOutputOnly(0.0, 1000000000.0, AHRS_Parameters_magTime)
        self.AHRS_Parameters_accelTime = self.LimitNumber_FloatOutputOnly(0.0, 1000000000.0, AHRS_Parameters_accelTime)
        self.AHRS_Parameters_biasTime = self.LimitNumber_FloatOutputOnly(0.0, 1000000000.0, AHRS_Parameters_biasTime)

        self.setAHRSParameters_NeedsToBeFiredFlag = 1

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def LimitNumber_IntOutputOnly(self, min_val, max_val, test_val):
        if test_val > max_val:
            test_val = max_val

        elif test_val < min_val:
            test_val = min_val

        else:
            test_val = test_val

        test_val = int(test_val)

        return test_val
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def LimitNumber_FloatOutputOnly(self, min_val, max_val, test_val):
        if test_val > max_val:
            test_val = max_val

        elif test_val < min_val:
            test_val = min_val

        else:
            test_val = test_val

        test_val = float(test_val)

        return test_val
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def LimitTextEntryInput(self, min_val, max_val, test_val, TextEntryObject):

        try:
            test_val = float(test_val)  # MUST HAVE THIS LINE TO CATCH STRINGS PASSED INTO THE FUNCTION

            if test_val > max_val:
                test_val = max_val
            elif test_val < min_val:
                test_val = min_val
            else:
                test_val = test_val

        except:
            pass

        try:
            if TextEntryObject != "":
                if isinstance(TextEntryObject, list) == 1:  # Check if the input 'TextEntryObject' is a list or not
                    TextEntryObject[0].set(str(test_val))  # Reset the text, overwriting the bad value that was entered.
                else:
                    TextEntryObject.set(str(test_val))  # Reset the text, overwriting the bad value that was entered.
        except:
            pass

        return test_val
    ##########################################################################################################
    ##########################################################################################################


    ##########################################################################################################
    ##########################################################################################################
    def getPreciseSecondsTimeStampString(self):
        ts = time.time()

        return ts
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def GetMostRecentDataDict(self):

        if self.EXIT_PROGRAM_FLAG == 0:

            return deepcopy(self.MostRecentDataDict) #deepcopy IS required as MostRecentDataDict contains lists.

        else:
            return dict() #So that we're not returning variables during the close-down process.

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def UpdateFrequencyCalculation_MainThread(self):

        try:
            self.DataStreamingDeltaT_CalculatedFromMainThread = self.CurrentTime_CalculatedFromMainThread - self.LastTime_CalculatedFromMainThread

            if self.DataStreamingDeltaT_CalculatedFromMainThread != 0.0:
                self.DataStreamingFrequency_CalculatedFromMainThread = 1.0/self.DataStreamingDeltaT_CalculatedFromMainThread

            self.LastTime_CalculatedFromMainThread = self.CurrentTime_CalculatedFromMainThread
        except:
            exceptions = sys.exc_info()[0]
            print("UpdateFrequencyCalculation_MainThread: exceptions: %s" % exceptions)
            #traceback.print_exc()
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def UpdateFrequencyCalculation_TimestampFromPhidget_SpatialData_AccelGyroMag(self):

        try:
            self.DataStreamingDeltaT_TimestampFromPhidget_SpatialData_AccelGyroMag = self.CurrentTime_TimestampFromPhidget_SpatialData_AccelGyroMag - self.LastTime_TimestampFromPhidget_SpatialData_AccelGyroMag

            ##########################
            if self.DataStreamingDeltaT_TimestampFromPhidget_SpatialData_AccelGyroMag != 0.0:
                self.DataStreamingFrequency_TimestampFromPhidget_SpatialData_AccelGyroMag = 1.0/self.DataStreamingDeltaT_TimestampFromPhidget_SpatialData_AccelGyroMag
            ##########################

            self.LastTime_TimestampFromPhidget_SpatialData_AccelGyroMag = self.CurrentTime_TimestampFromPhidget_SpatialData_AccelGyroMag

        except:
            exceptions = sys.exc_info()[0]
            print("UpdateFrequencyCalculation_TimestampFromPhidget_SpatialData_AccelGyroMag: exceptions: %s" % exceptions)
            #traceback.print_exc()
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def UpdateFrequencyCalculation_TimestampFromPhidget_AlgorithmData_Quaternions(self):

        try:
            self.DataStreamingDeltaT_TimestampFromPhidget_AlgorithmData_Quaternions = self.CurrentTime_TimestampFromPhidget_AlgorithmData_Quaternions - self.LastTime_TimestampFromPhidget_AlgorithmData_Quaternions

            ##########################
            if self.DataStreamingDeltaT_TimestampFromPhidget_AlgorithmData_Quaternions != 0.0:
                self.DataStreamingFrequency_TimestampFromPhidget_AlgorithmData_Quaternions = 1.0/self.DataStreamingDeltaT_TimestampFromPhidget_AlgorithmData_Quaternions
            ##########################

            self.LastTime_TimestampFromPhidget_AlgorithmData_Quaternions = self.CurrentTime_TimestampFromPhidget_AlgorithmData_Quaternions

        except:
            exceptions = sys.exc_info()[0]
            print("UpdateFrequencyCalculation_TimestampFromPhidget_AlgorithmData_Quaternions: exceptions: %s" % exceptions)
            #traceback.print_exc()
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def ZeroAlgorithmFromExternalProgram(self):

        self.ZeroAlgorithm_NeedsToBeChangedFlag = 1

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def __ZeroAlgorithm(self): #The "__ prefix" makes it private to this class.

        try:
            #########################################################
            self.Spatial_PhidgetsSpatialObject.zeroAlgorithm()
            self.MyPrint_WithoutLogFile("@@@@@ ZeroAlgorithm function fired! @@@@@")
            #########################################################

        except PhidgetException as e:
            self.MyPrint_WithoutLogFile("__ZeroAlgorithm ERROR, Phidget Exception %i: %s" % (e.code, e.details))

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def ZeroGyrosFromExternalProgram(self):

        self.ZeroGyros_NeedsToBeChangedFlag = 1

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def __ZeroGyros(self): #The "__ prefix" makes it private to this class.

        try:
            #########################################################
            self.Spatial_PhidgetsSpatialObject.zeroGyro()
            self.MyPrint_WithoutLogFile("@@@@@ ZeroGyros function fired! @@@@@")
            #########################################################

        except PhidgetException as e:
            self.MyPrint_WithoutLogFile("ZeroGyros ERROR, Phidget Exception %i: %s" % (e.code, e.details))

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def ConvertQuaterionsToEulerAngles_RollPitchYawAbtXYZ_ManualCalculation(self, QuaternionsInputListXYZW):

        try:
            #########################
            if self.IsInputList(QuaternionsInputListXYZW) != 1 or len(QuaternionsInputListXYZW) != 4:
                print("ConvertQuaterionsToEulerAngles_RollPitchYawAbtXYZ_ManualCalculation ERROR: Input must be a list of length 4.")
                return dict()
            #########################

            #########################
            [X, Y, Z, W] = list(QuaternionsInputListXYZW)
            #print("X: " + str(X) + ", Y: " + str(Y) + ", Z: " + str(Z) + ", W: " + str(W))
            #########################

            #https://en.wikipedia.org/wiki/Conversion_between_quaternions_and_Euler_angles

            ######################### Roll abt X-axis
            sinr_cosp = 2.0*(W*X + Y*Z)
            cosr_cosp = 1 - 2.0*(X*X + Y*Y)
            Roll_AbtXaxis_Radians = math.atan2(sinr_cosp, cosr_cosp)
            #########################

            ######################### #Pitch aby Y-axis
            sinp = 2.0*(W*Y - Z*X)
            if abs(sinp) >= 1.0:
                Pitch_AbtYaxis_Radians = math.copysign(math.pi/2.0, sinp)
            else:
                Pitch_AbtYaxis_Radians = math.asin(sinp)
            #########################

            ######################### Yaw about Z-axis
            siny_cosp = 2.0*(W*Z + X*Y)
            cosy_cosp = 1 - 2.0*(Y*Y + Z*Z)
            Yaw_AbtZaxis_Radians = math.atan2(siny_cosp, cosy_cosp)
            #########################

            #########################
            Roll_AbtXaxis_Degrees = Roll_AbtXaxis_Radians * 180.0/math.pi
            Pitch_AbtYaxis_Degrees = Pitch_AbtYaxis_Radians * 180.0/math.pi
            Yaw_AbtZaxis_Degrees = Yaw_AbtZaxis_Radians * 180.0/math.pi
            #########################

            DictToReturn = dict([("RollPitchYaw_AbtXYZ_List_Degrees", [Roll_AbtXaxis_Degrees, Pitch_AbtYaxis_Degrees, Yaw_AbtZaxis_Degrees]),
                                 ("RollPitchYaw_AbtXYZ_List_Radians", [Roll_AbtXaxis_Radians, Pitch_AbtYaxis_Radians, Yaw_AbtZaxis_Radians])])

            return DictToReturn

        except:
            exceptions = sys.exc_info()[0]
            print("ConvertQuaterionsToEulerAngles_RollPitchYawAbtXYZ_ManualCalculation, Exceptions: %s" % exceptions)
            traceback.print_exc()
            return dict()
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def ConvertQuaterionsToEulerAngles_RollPitchYawAbtXYZ_ScipyCalculation(self, QuaternionsInputListXYZW):

        try:
            #########################
            if self.IsInputList(QuaternionsInputListXYZW) != 1 or len(QuaternionsInputListXYZW) != 4:
                print("ConvertQuaterionsToEulerAngles_RollPitchYawAbtXYZ_ScipyCalculation ERROR: Input must be a list of length 4.")
                return dict()
            #########################

            #########################
            [X, Y, Z, W] = list(QuaternionsInputListXYZW)
            #print("X: " + str(X) + ", Y: " + str(Y) + ", Z: " + str(Z) + ", W: " + str(W))
            #########################

            RotationObject = Rotation.from_quat(QuaternionsInputListXYZW)
            [Roll_AbtXaxis_Radians, Pitch_AbtYaxis_Radians, Yaw_AbtZaxis_Radians] = RotationObject.as_euler("xyz")  ################## must run with python 3.7.3

            #########################
            Roll_AbtXaxis_Degrees = Roll_AbtXaxis_Radians * 180.0/math.pi
            Pitch_AbtYaxis_Degrees = Pitch_AbtYaxis_Radians * 180.0/math.pi
            Yaw_AbtZaxis_Degrees = Yaw_AbtZaxis_Radians * 180.0/math.pi
            #########################

            DictToReturn = dict([("RollPitchYaw_AbtXYZ_List_Degrees", [Roll_AbtXaxis_Degrees, Pitch_AbtYaxis_Degrees, Yaw_AbtZaxis_Degrees]),
                                 ("RollPitchYaw_AbtXYZ_List_Radians", [Roll_AbtXaxis_Radians, Pitch_AbtYaxis_Radians, Yaw_AbtZaxis_Radians])])

            return DictToReturn

        except:
            exceptions = sys.exc_info()[0]
            print("ConvertQuaterionsToEulerAngles_RollPitchYawAbtXYZ_ScipyCalculation, Exceptions: %s" % exceptions)
            traceback.print_exc()
            return dict()
    ##########################################################################################################
    ##########################################################################################################

    ########################################################################################################## unicorn
    ##########################################################################################################
    ##########################################################################################################
    def MainThread(self):

        self.MyPrint_WithoutLogFile("Started MainThread for PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class object.")
        
        self.MainThread_still_running_flag = 1

        self.StartingTime_CalculatedFromMainThread = self.getPreciseSecondsTimeStampString()

        ##########################################################################################################
        ##########################################################################################################
        while self.EXIT_PROGRAM_FLAG == 0:
            try:

                ##########################################################################################################
                self.CurrentTime_CalculatedFromMainThread = self.getPreciseSecondsTimeStampString() - self.StartingTime_CalculatedFromMainThread
                ##########################################################################################################

                ##########################################################################################################
                if self.ZeroAlgorithm_NeedsToBeChangedFlag == 1:
                    self.__ZeroAlgorithm()
                    self.ZeroAlgorithm_NeedsToBeChangedFlag = 0
                ##########################################################################################################

                ##########################################################################################################
                if self.ZeroGyros_NeedsToBeChangedFlag == 1:
                    self.__ZeroGyros()
                    self.ZeroGyros_NeedsToBeChangedFlag = 0
                ##########################################################################################################

                ##########################################################################################################
                if self.setAHRSParameters_NeedsToBeFiredFlag == 1:
                    self.Spatial_PhidgetsSpatialObject.setAHRSParameters(self.AHRS_Parameters_angularVelocityThreshold,
                                                                         self.AHRS_Parameters_angularVelocityDeltaThreshold,
                                                                         self.AHRS_Parameters_accelerationThreshold,
                                                                         self.AHRS_Parameters_magTime,
                                                                         self.AHRS_Parameters_accelTime,
                                                                         self.AHRS_Parameters_biasTime)

                    print("setAHRSParameters event fired for\n" +
                          "self.AHRS_Parameters_angularVelocityThreshold = " + str(self.AHRS_Parameters_angularVelocityThreshold) + "\n" +\
                          "self.AHRS_Parameters_angularVelocityDeltaThreshold = " + str(self.AHRS_Parameters_angularVelocityDeltaThreshold) + "\n" +\
                          "self.AHRS_Parameters_accelerationThreshold = " + str(self.AHRS_Parameters_accelerationThreshold) + "\n" +\
                          "self.AHRS_Parameters_magTime = " + str(self.AHRS_Parameters_magTime) + "\n" +\
                          "self.AHRS_Parameters_accelTime = " + str(self.AHRS_Parameters_accelTime) + "\n" +\
                          "self.AHRS_Parameters_biasTime = " + str(self.AHRS_Parameters_biasTime))

                    self.setAHRSParameters_NeedsToBeFiredFlag = 0
                ##########################################################################################################

                ##########################################################################################################
                if self.SpatialData_AccelGyroMag_EventHandler_Queue.qsize() > 0:
                    [Acceleration_PhidgetUnits_Raw_temp, AngularRate_PhidgetUnits_Raw_temp, MagneticField_PhidgetUnits_Raw_temp, Timestamp_temp] = self.SpatialData_AccelGyroMag_EventHandler_Queue.get()

                    #NOT ACTIVELY DOING ANYTHING WITH THIS DATA CURRENTLY
                ##########################################################################################################

                ########################################################################################################## unicorn
                if self.AlgorithmData_Quaternions_EventHandler_Queue.qsize() > 0:
                    [Quaternions_DirectFromDataEventHandler_temp, Timestamp_DirectFromDataEventHandler_temp, DeltaT_DirectFromDataEventHandler_temp] = self.AlgorithmData_Quaternions_EventHandler_Queue.get()

                    if DeltaT_DirectFromDataEventHandler_temp > 0:
                        self.Quaternions_DirectFromDataEventHandler = Quaternions_DirectFromDataEventHandler_temp

                        #'''
                        self.RollPitchYaw_AbtXYZ_Dict = self.ConvertQuaterionsToEulerAngles_RollPitchYawAbtXYZ_ManualCalculation(self.Quaternions_DirectFromDataEventHandler)
                        #RollPitchYaw_AbtXYZ_Dict = self.ConvertQuaterionsToEulerAngles_RollPitchYawAbtXYZ_ScipyCalculation(self.Quaternions_DirectFromDataEventHandler)

                        #print("self.RollPitchYaw_AbtXYZ_Dict: " + str(self.RollPitchYaw_AbtXYZ_Dict))

                        ###################################################
                        ###################################################
                        #COULD FILTER THE QUATERNIONS WITH SLERP IF WE WANT HERE, BUT I THINK THAT PHIDGETS IS DOING THAT INTERNALLY.
                        self.Roll_AbtXaxis_Degrees = self.RollPitchYaw_AbtXYZ_Dict["RollPitchYaw_AbtXYZ_List_Degrees"][0]
                        self.Pitch_AbtYaxis_Degrees = self.RollPitchYaw_AbtXYZ_Dict["RollPitchYaw_AbtXYZ_List_Degrees"][1]
                        self.Yaw_AbtZaxis_Degrees = self.RollPitchYaw_AbtXYZ_Dict["RollPitchYaw_AbtXYZ_List_Degrees"][2]
                        ###################################################
                        ###################################################

                        ################################################### SET's
                        ###################################################
                        if self.ZeroAndSnapshotData_OPEN_FLAG == 1:

                            ####################################################
                            self.ZeroAndSnapshotData_ReubenPython2and3ClassObject.CheckStateMachine()
                            ####################################################

                            ####################################################
                            self.RollPitchYaw_AbtXYZ_ListOfDictsAsInputToZeroingObject = [dict([("Variable_Name", "Roll_AbtXaxis_Degrees"), ("Raw_CurrentValue", self.Roll_AbtXaxis_Degrees )]),
                                                            dict([("Variable_Name", "Pitch_AbtYaxis_Degrees"), ("Raw_CurrentValue", self.Pitch_AbtYaxis_Degrees)]),
                                                            dict([("Variable_Name", "Yaw_AbtZaxis_Degrees"), ("Raw_CurrentValue", self.Yaw_AbtZaxis_Degrees)])]

                            self.ZeroAndSnapshotData_MostRecentDict = self.ZeroAndSnapshotData_ReubenPython2and3ClassObject.UpdateData(self.RollPitchYaw_AbtXYZ_ListOfDictsAsInputToZeroingObject)

                            self.ZeroAndSnapshotData_MostRecentDict_DataUpdateNumber = self.ZeroAndSnapshotData_MostRecentDict["DataUpdateNumber"]
                            self.ZeroAndSnapshotData_MostRecentDict_LoopFrequencyHz = self.ZeroAndSnapshotData_MostRecentDict["LoopFrequencyHz"]
                            self.ZeroAndSnapshotData_MostRecentDict_OnlyVariablesAndValuesDictOfDicts = self.ZeroAndSnapshotData_MostRecentDict["OnlyVariablesAndValuesDictOfDicts"]

                            self.Roll_AbtXaxis_Degrees = self.ZeroAndSnapshotData_MostRecentDict_OnlyVariablesAndValuesDictOfDicts["Roll_AbtXaxis_Degrees"]["Raw_CurrentValue_Zeroed"]
                            self.Pitch_AbtYaxis_Degrees = self.ZeroAndSnapshotData_MostRecentDict_OnlyVariablesAndValuesDictOfDicts["Pitch_AbtYaxis_Degrees"]["Raw_CurrentValue_Zeroed"]
                            self.Yaw_AbtZaxis_Degrees = self.ZeroAndSnapshotData_MostRecentDict_OnlyVariablesAndValuesDictOfDicts["Yaw_AbtZaxis_Degrees"]["Raw_CurrentValue_Zeroed"]

                            ###################################################
                            ###################################################
                            #COULD FILTER THE QUATERNIONS WITH SLERP IF WE WANT HERE, BUT I THINK THAT PHIDGETS IS DOING THAT INTERNALLY.
                            self.RollPitchYaw_AbtXYZ_Dict["RollPitchYaw_AbtXYZ_List_Degrees"][0] = self.Roll_AbtXaxis_Degrees
                            self.RollPitchYaw_AbtXYZ_Dict["RollPitchYaw_AbtXYZ_List_Degrees"][1] = self.Pitch_AbtYaxis_Degrees
                            self.RollPitchYaw_AbtXYZ_Dict["RollPitchYaw_AbtXYZ_List_Degrees"][2] = self.Yaw_AbtZaxis_Degrees
                            ###################################################
                            ###################################################

                            ####################################################

                        ###################################################
                        ###################################################

                        ###################################################
                        ###################################################
                        self.RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond = (self.Roll_AbtXaxis_Degrees - self.Roll_AbtXaxis_Degrees_Last)/DeltaT_DirectFromDataEventHandler_temp
                        self.RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_SMOOTHED = self.RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_MyLowPassFilterClass_Object.AddDataPointFromExternalProgram(self.RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond)["SignalOutSmoothed"]
                        self.Roll_AbtXaxis_Degrees_Last = self.Roll_AbtXaxis_Degrees

                        self.PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond = (self.Pitch_AbtYaxis_Degrees - self.Pitch_AbtYaxis_Degrees_Last)/DeltaT_DirectFromDataEventHandler_temp
                        self.PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_SMOOTHED = self.PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_MyLowPassFilterClass_Object.AddDataPointFromExternalProgram(self.PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond)["SignalOutSmoothed"]
                        self.Pitch_AbtYaxis_Degrees_Last = self.Pitch_AbtYaxis_Degrees

                        self.YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond = (self.Yaw_AbtZaxis_Degrees - self.Yaw_AbtZaxis_Degrees_Last)/DeltaT_DirectFromDataEventHandler_temp
                        self.YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_SMOOTHED = self.YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_MyLowPassFilterClass_Object.AddDataPointFromExternalProgram(self.YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond)["SignalOutSmoothed"]
                        self.Yaw_AbtZaxis_Degrees_Last = self.Yaw_AbtZaxis_Degrees

                        self.RollPitchYaw_Rate_AbtXYZ_Dict = dict([
                            ("RollPitchYaw_Rate_AbtXYZ_List_DegreesPerSecond",
                                    [self.RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_SMOOTHED,
                                    self.PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_SMOOTHED,
                                    self.YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_SMOOTHED]),
                            ("RollPitchYaw_Rate_AbtXYZ_List_RadiansPerSecond",
                                    [self.RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_SMOOTHED*math.pi/180.0,
                                    self.PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_SMOOTHED*math.pi/180.0,
                                    self.YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_SMOOTHED*math.pi/180.0])])
                        ###################################################
                        ###################################################

                        ################################################### unicorn
                        ###################################################
                        self.MostRecentDataDict = dict([("Quaternions_DirectFromDataEventHandler", self.Quaternions_DirectFromDataEventHandler),
                                            ("RollPitchYaw_AbtXYZ_Dict", self.RollPitchYaw_AbtXYZ_Dict), #WE'RE RETURNING DICT, NOT INDIVIDUAL VALUES
                                            ("RollPitchYaw_Rate_AbtXYZ_Dict", self.RollPitchYaw_Rate_AbtXYZ_Dict), #WE'RE RETURNING DICT, NOT INDIVIDUAL VALUES
                                            ("DataStreamingFrequency_CalculatedFromMainThread", self.DataStreamingFrequency_CalculatedFromMainThread),
                                            ("DataStreamingFrequency_TimestampFromPhidget_AlgorithmData_Quaternions", self.DataStreamingFrequency_TimestampFromPhidget_AlgorithmData_Quaternions),
                                            ("Time", Timestamp_DirectFromDataEventHandler_temp)])

                                            #("DataStreamingFrequency_TimestampFromPhidget_SpatialData_AccelGyroMag", self.DataStreamingFrequency_TimestampFromPhidget_SpatialData_AccelGyroMag),
                                            #("Roll_AbtXaxis_Degrees", self.Roll_AbtXaxis_Degrees),
                                            #("Pitch_AbtYaxis_Degrees", self.Pitch_AbtYaxis_Degrees),
                                            #("Yaw_AbtZaxis_Degrees", self.Yaw_AbtZaxis_Degrees),
                                            #("RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_SMOOTHED", self.RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_SMOOTHED),
                                            #("PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_SMOOTHED", self.PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_SMOOTHED),
                                            #("YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_SMOOTHED", self.YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_SMOOTHED),
                        ###################################################
                        ###################################################

                ##########################################################################################################

                ############################################### USE THE TIME.SLEEP() TO SET THE LOOP FREQUENCY
                ###############################################
                ###############################################
                self.UpdateFrequencyCalculation_MainThread()  # ONLY UPDATE IF WE HAD NEW DATA

                if self.MainThread_TimeToSleepEachLoop > 0.0:
                    time.sleep(self.MainThread_TimeToSleepEachLoop)
                ###############################################
                ###############################################
                ###############################################

                ##########################################################################################################

            except PhidgetException as e:
                print("MainThread ERROR, Phidget Exception %i: %s" % (e.code, e.details))
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        self.Spatial_PhidgetsSpatialObject.close()
        self.MyPrint_WithoutLogFile("Finished MainThread for PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class object.")
        self.MainThread_still_running_flag = 0
        ##########################################################################################################
        ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def ExitProgram_Callback(self):

        print("Exiting all threads for PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class object")

        self.EXIT_PROGRAM_FLAG = 1

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def StartGUI(self, GuiParent):

        #self.GUI_Thread_ThreadingObject = threading.Thread(target=self.GUI_Thread, args=(GuiParent,))
        #self.GUI_Thread_ThreadingObject.setDaemon(True) #Should mean that the GUI thread is destroyed automatically when the main thread is destroyed.
        #self.GUI_Thread_ThreadingObject.start()

        self.GUI_Thread(GuiParent)
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def GUI_Thread(self, parent):

        print("Starting the GUI_Thread for PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class object.")

        ###################################################
        ###################################################
        self.root = parent
        self.parent = parent
        ###################################################
        ###################################################

        ###################################################
        ###################################################
        self.myFrame = Frame(self.root)

        if self.UseBorderAroundThisGuiObjectFlag == 1:
            self.myFrame["borderwidth"] = 2
            self.myFrame["relief"] = "ridge"

        self.myFrame.grid(row = self.GUI_ROW,
                          column = self.GUI_COLUMN,
                          padx = self.GUI_PADX,
                          pady = self.GUI_PADY,
                          rowspan = self.GUI_ROWSPAN,
                          columnspan= self.GUI_COLUMNSPAN,
                          sticky = self.GUI_STICKY)
        ###################################################
        ###################################################

        ###################################################
        ###################################################
        self.TKinter_LightGreenColor = '#%02x%02x%02x' % (150, 255, 150) #RGB
        self.TKinter_LightRedColor = '#%02x%02x%02x' % (255, 150, 150) #RGB
        self.TKinter_LightYellowColor = '#%02x%02x%02x' % (255, 255, 150)  # RGB
        self.TKinter_DefaultGrayColor = '#%02x%02x%02x' % (240, 240, 240)  # RGB
        ###################################################
        ###################################################

        ###################################################
        ###################################################
        self.DeviceInfo_Label = Label(self.myFrame, text="Device Info", width=50)
        self.DeviceInfo_Label.grid(row=0, column=0, padx=5, pady=1, columnspan=1, rowspan=1)
        ###################################################
        ###################################################

        ###################################################
        ###################################################
        self.ZeroingButtonsFrame = Frame(self.myFrame)
        self.ZeroingButtonsFrame.grid(row = 1, column = 0, padx = 10, pady = 10, rowspan = 1, columnspan = 1)
        ###################################################
        ###################################################

        ###################################################
        ###################################################
        self.ZeroGyros_Button = Button(self.ZeroingButtonsFrame, text="Zero Gyros\nPhidgets Function Call", state="normal", width=30,command=lambda i=1: self.ZeroGyros_ButtonResponse())
        self.ZeroGyros_Button.grid(row=0, column=0, padx=1, pady=1, columnspan=1, rowspan=1)
        ###################################################
        ###################################################

        ###################################################
        ###################################################
        self.ZeroAlgorithm_Button = Button(self.ZeroingButtonsFrame, text="Zero Algorithm\nPhidgets Function Call", state="normal", width=30,command=lambda i=1: self.ZeroAlgorithm_ButtonResponse())
        self.ZeroAlgorithm_Button.grid(row=0, column=1, padx=1, pady=1, columnspan=1, rowspan=1)
        ###################################################
        ###################################################

        ###################################################
        ###################################################
        self.QuaternionsAndEulerAngles_Label = Label(self.myFrame, text="QuaternionsAndEulerAngles_Label", width=100)
        self.QuaternionsAndEulerAngles_Label.grid(row=2, column=0, padx=1, pady=1, columnspan=1, rowspan=1)
        ###################################################
        ###################################################

        ###################################################
        ###################################################
        self.Spatials_Label = Label(self.myFrame, text="Spatials_Label", width=80)
        self.Spatials_Label.grid(row=3, column=0, padx=5, pady=1, columnspan=1, rowspan=1)
        ###################################################
        ###################################################

        ###################################################
        ###################################################
        self.PrintToGui_Label = Label(self.myFrame, text="PrintToGui_Label", width=100)
        if self.EnableInternal_MyPrint_Flag == 1:
            self.PrintToGui_Label.grid(row=6, column=0, padx=10, pady=10, columnspan=10, rowspan=10)
        ###################################################
        ###################################################

        ###################################################
        ###################################################
        self.GUI_ready_to_be_updated_flag = 1
        ###################################################
        ###################################################

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def ZeroAlgorithm_ButtonResponse(self):

        self.ZeroAlgorithm_NeedsToBeChangedFlag = 1

        self.MyPrint_WithoutLogFile("ZeroAlgorithm_ButtonResponse event fired!")
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def ZeroGyros_ButtonResponse(self):

        self.ZeroGyros_NeedsToBeChangedFlag = 1

        self.MyPrint_WithoutLogFile("ZeroGyros_ButtonResponse event fired!")
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def GUI_update_clock(self):

        #######################################################
        #######################################################
        #######################################################
        #######################################################
        if self.USE_GUI_FLAG == 1 and self.EXIT_PROGRAM_FLAG == 0:

            #######################################################
            #######################################################
            #######################################################
            if self.GUI_ready_to_be_updated_flag == 1:

                #######################################################
                #######################################################
                try:
                    #######################################################
                    self.DeviceInfo_Label["text"] = self.NameToDisplay_UserSet + \
                                                    "\nDevice Name: " + self.DetectedDeviceName + \
                                                    "\nDevice Serial Number: " + str(self.DetectedDeviceSerialNumber) + \
                                                    "\nDevice Version: " + str(self.DetectedDeviceVersion) + \
                                                    "\nDevice ID: " + str(self.DetectedDeviceID) + \
                                                    "\nDevice PN: " + str(self.DevicePN) + \
                                                    "\nCallback DeltaT ms: " + str(self.Spatial_CallbackUpdateDeltaTmilliseconds_ReceivedFromBoard) +\
                                                    "\nAlgorithm, RxFromDevice: " + self.Algorithm_RxFromDevice_Str +\
                                                    "\nHeatingEnable, RxFromDevice: " + str(self.HeatingEnabledToStabilizeSensorTemperature_RxFromDevice_Str)+\
                                                    "\nAlgorithmMagnetometerGain, RxFromDevice_Str: " + str(self.AlgorithmMagnetometerGain_RxFromDevice_Str)
                    #######################################################

                    #######################################################
                    self.QuaternionsAndEulerAngles_Label["text"] = "Quaternions: " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self.Quaternions_DirectFromDataEventHandler, 0, 3) + \
                                                "\nRoll_AbtXaxis_Degrees: " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self.Roll_AbtXaxis_Degrees, 0, 3) + \
                                                "\nPitch_AbtYaxis_Degrees: " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self.Pitch_AbtYaxis_Degrees, 0, 3) + \
                                                "\nYaw_AbtZaxis_Degrees: " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self.Yaw_AbtZaxis_Degrees, 0, 3) + \
                                                "\nRollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_SMOOTHED: " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self.RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_SMOOTHED, 0, 3) + \
                                                "\nPitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_SMOOTHED: " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self.PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_SMOOTHED, 0, 3) + \
                                                "\nYawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_SMOOTHED: " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self.YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_SMOOTHED, 0, 3) + \
                                                "\nSpatialData Queue Size: " + str(self.SpatialData_AccelGyroMag_EventHandler_Queue.qsize()) + \
                                                "\nAlgorithmData Queue Size: " + str(self.AlgorithmData_Quaternions_EventHandler_Queue.qsize())
                    #######################################################

                    #######################################################
                    self.Spatials_Label["text"] = "Time: " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self.CurrentTime_CalculatedFromMainThread, 0, 3) + \
                                                "\nSpatial Callback Frequency: " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self.DataStreamingFrequency_TimestampFromPhidget_SpatialData_AccelGyroMag, 0, 3) + \
                                                "\nAlgorithm Callback Frequency: " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self.DataStreamingFrequency_TimestampFromPhidget_AlgorithmData_Quaternions, 0, 3) + \
                                                "\nMain Thread Frequency: " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self.DataStreamingFrequency_CalculatedFromMainThread, 0, 3)
                    #######################################################

                    #########################################################
                    if self.ZeroAndSnapshotData_OPEN_FLAG == 1:
                        self.ZeroAndSnapshotData_ReubenPython2and3ClassObject.GUI_update_clock()
                    #########################################################

                    #######################################################
                    self.PrintToGui_Label.config(text=self.PrintToGui_Label_TextInput_Str)
                    #######################################################

                except:
                    exceptions = sys.exc_info()[0]
                    print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class GUI_update_clock ERROR: Exceptions: %s" % exceptions)
                    traceback.print_exc()
                #######################################################
                #######################################################

            #######################################################
            #######################################################
            #######################################################

        #######################################################
        #######################################################
        #######################################################
        #######################################################

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Spatial_ZeroingButtonObjectResponse(self, SpatialChannelNumber):

        self.Spatial_NeedsToBeZeroedFlag[SpatialChannelNumber] = 1
        #self.MyPrint_WithoutLogFile("Spatial_ZeroingButtonObjectResponse: Event fired for SpatialChannelNumber " + str(SpatialChannelNumber))

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def TimerCallbackFunctionWithFunctionAsArgument_SingleShot_NoParenthesesAfterFunctionName(self, CallbackAfterDeltaTseconds, FunctionToCall_NoParenthesesAfterFunctionName, ArgumentListToFunction):

        self.TimerObject = threading.Timer(CallbackAfterDeltaTseconds, FunctionToCall_NoParenthesesAfterFunctionName, ArgumentListToFunction) #Must pass arguments to callback-function via list as the third argument to Timer call
        self.TimerObject.daemon = True #Without the daemon=True, this recursive function won't terminate when the main program does.
        self.TimerObject.start()

        print("TimerCallbackFunctionWithFunctionAsArgument_SingleShot_NoParenthesesAfterFunctionName event fired to call function: '" + str(FunctionToCall_NoParenthesesAfterFunctionName.__name__) + "' at time " + str(self.getPreciseSecondsTimeStampString()))
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def MyPrint_WithoutLogFile(self, input_string):

        input_string = str(input_string)

        if input_string != "":

            #input_string = input_string.replace("\n", "").replace("\r", "")

            ################################ Write to console
            # Some people said that print crashed for pyinstaller-built-applications and that sys.stdout.write fixed this.
            # http://stackoverflow.com/questions/13429924/pyinstaller-packaged-application-works-fine-in-console-mode-crashes-in-window-m
            if self.PrintToConsoleFlag == 1:
                sys.stdout.write(input_string + "\n")
            ################################

            ################################ Write to GUI
            self.PrintToGui_Label_TextInputHistory_List.append(self.PrintToGui_Label_TextInputHistory_List.pop(0)) #Shift the list
            self.PrintToGui_Label_TextInputHistory_List[-1] = str(input_string) #Add the latest value

            self.PrintToGui_Label_TextInput_Str = ""
            for Counter, Line in enumerate(self.PrintToGui_Label_TextInputHistory_List):
                self.PrintToGui_Label_TextInput_Str = self.PrintToGui_Label_TextInput_Str + Line

                if Counter < len(self.PrintToGui_Label_TextInputHistory_List) - 1:
                    self.PrintToGui_Label_TextInput_Str = self.PrintToGui_Label_TextInput_Str + "\n"
            ################################

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def IsInputList(self, InputToCheck):

        result = isinstance(InputToCheck, list)
        return result
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    def ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self, input, number_of_leading_numbers = 4, number_of_decimal_places = 3):

        number_of_decimal_places = max(1, number_of_decimal_places) #Make sure we're above 1

        ListOfStringsToJoin = []

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        if isinstance(input, str) == 1:
            ListOfStringsToJoin.append(input)
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        elif isinstance(input, int) == 1 or isinstance(input, float) == 1:
            element = float(input)
            prefix_string = "{:." + str(number_of_decimal_places) + "f}"
            element_as_string = prefix_string.format(element)

            ##########################################################################################################
            ##########################################################################################################
            if element >= 0:
                element_as_string = element_as_string.zfill(number_of_leading_numbers + number_of_decimal_places + 1 + 1)  # +1 for sign, +1 for decimal place
                element_as_string = "+" + element_as_string  # So that our strings always have either + or - signs to maintain the same string length
            else:
                element_as_string = element_as_string.zfill(number_of_leading_numbers + number_of_decimal_places + 1 + 1 + 1)  # +1 for sign, +1 for decimal place
            ##########################################################################################################
            ##########################################################################################################

            ListOfStringsToJoin.append(element_as_string)
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        elif isinstance(input, list) == 1:

            if len(input) > 0:
                for element in input: #RECURSION
                    ListOfStringsToJoin.append(self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(element, number_of_leading_numbers, number_of_decimal_places))

            else: #Situation when we get a list() or []
                ListOfStringsToJoin.append(str(input))

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        elif isinstance(input, tuple) == 1:

            if len(input) > 0:
                for element in input: #RECURSION
                    ListOfStringsToJoin.append("TUPLE" + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(element, number_of_leading_numbers, number_of_decimal_places))

            else: #Situation when we get a list() or []
                ListOfStringsToJoin.append(str(input))

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        elif isinstance(input, dict) == 1:

            if len(input) > 0:
                for Key in input: #RECURSION
                    ListOfStringsToJoin.append(str(Key) + ": " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(input[Key], number_of_leading_numbers, number_of_decimal_places))

            else: #Situation when we get a dict()
                ListOfStringsToJoin.append(str(input))

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        else:
            ListOfStringsToJoin.append(str(input))
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        if len(ListOfStringsToJoin) > 1:

            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            StringToReturn = ""
            for Index, StringToProcess in enumerate(ListOfStringsToJoin):

                ################################################
                if Index == 0: #The first element
                    if StringToProcess.find(":") != -1 and StringToProcess[0] != "{": #meaning that we're processing a dict()
                        StringToReturn = "{"
                    elif StringToProcess.find("TUPLE") != -1 and StringToProcess[0] != "(":  # meaning that we're processing a tuple
                        StringToReturn = "("
                    else:
                        StringToReturn = "["

                    StringToReturn = StringToReturn + StringToProcess.replace("TUPLE","") + ", "
                ################################################

                ################################################
                elif Index < len(ListOfStringsToJoin) - 1: #The middle elements
                    StringToReturn = StringToReturn + StringToProcess + ", "
                ################################################

                ################################################
                else: #The last element
                    StringToReturn = StringToReturn + StringToProcess

                    if StringToProcess.find(":") != -1 and StringToProcess[-1] != "}":  # meaning that we're processing a dict()
                        StringToReturn = StringToReturn + "}"
                    elif StringToProcess.find("TUPLE") != -1 and StringToProcess[-1] != ")":  # meaning that we're processing a tuple
                        StringToReturn = StringToReturn + ")"
                    else:
                        StringToReturn = StringToReturn + "]"

                ################################################

            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################

        elif len(ListOfStringsToJoin) == 1:
            StringToReturn = ListOfStringsToJoin[0]

        else:
            StringToReturn = ListOfStringsToJoin

        return StringToReturn
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def ConvertDictToProperlyFormattedStringForPrinting(self, DictToPrint, NumberOfDecimalsPlaceToUse = 3, NumberOfEntriesPerLine = 1, NumberOfTabsBetweenItems = 3):

        ProperlyFormattedStringForPrinting = ""
        ItemsPerLineCounter = 0

        for Key in DictToPrint:

            ##########################################################################################################
            if isinstance(DictToPrint[Key], dict): #RECURSION
                ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + \
                                                     str(Key) + ":\n" + \
                                                     self.ConvertDictToProperlyFormattedStringForPrinting(DictToPrint[Key], NumberOfDecimalsPlaceToUse, NumberOfEntriesPerLine, NumberOfTabsBetweenItems)

            else:
                ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + \
                                                     str(Key) + ": " + \
                                                     self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(DictToPrint[Key], 0, NumberOfDecimalsPlaceToUse)
            ##########################################################################################################

            ##########################################################################################################
            if ItemsPerLineCounter < NumberOfEntriesPerLine - 1:
                ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + "\t"*NumberOfTabsBetweenItems
                ItemsPerLineCounter = ItemsPerLineCounter + 1
            else:
                ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + "\n"
                ItemsPerLineCounter = 0
            ##########################################################################################################

        return ProperlyFormattedStringForPrinting
    ##########################################################################################################
    ##########################################################################################################



