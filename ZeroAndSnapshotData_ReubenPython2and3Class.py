# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision E, 12/26/2025

Verified working on: Python 3.11/12/13 for Windows 10/11 64-bit and Raspberry Pi Bookworm (does not work on Mac).
'''

__author__ = 'reuben.brewer'

##########################################################################################################
##########################################################################################################

#################################################
import ReubenGithubCodeModulePaths #Replaces the need to have "ReubenGithubCodeModulePaths.pth" within "C:\Anaconda3\Lib\site-packages".
ReubenGithubCodeModulePaths.Enable()
#################################################

#################################################
from EntryListWithBlinking_ReubenPython2and3Class import *
from LowPassFilter_ReubenPython2and3Class import *
#################################################

#################################################
import os
import sys
import platform
import time
import datetime
import math
import collections
from copy import * #for deepcopy(dict)
import inspect #To enable 'TellWhichFileWereIn'
import threading
import queue as Queue
import traceback
#################################################

#################################################
from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk
#################################################

#################################################
import platform
if platform.system() == "Windows":
    import ctypes
    winmm = ctypes.WinDLL('winmm')
    winmm.timeBeginPeriod(1) #Set minimum timer resolution to 1ms so that time.sleep(0.001) behaves properly.
#################################################

##########################################################################################################
##########################################################################################################

class ZeroAndSnapshotData_ReubenPython2and3Class(Frame): #Subclass the Tkinter Frame

    ##########################################################################################################
    ##########################################################################################################
    def __init__(self, SetupDict): #Subclass the Tkinter Frame

        print("#################### ZeroAndSnapshotData_ReubenPython2and3Class __init__ starting. ####################")

        #########################################################
        #########################################################
        self.EXIT_PROGRAM_FLAG = 0
        self.OBJECT_CREATED_SUCCESSFULLY_FLAG = 0
        self.EntryListWithBlinking_OPEN_FLAG = 0

        self.EnableInternal_MyPrint_Flag = 0

        self.CurrentTime_CalculatedFromUpdateFunction = -11111.0
        self.LastTime_CalculatedFromUpdateFunction = -11111.0
        self.DataStreamingFrequency_CalculatedFromUpdateFunction = -11111.0
        self.DataStreamingDeltaT_CalculatedFromUpdateFunction = -11111.0

        self.DataUpdateNumber = -1

        self.MostRecentDataDict = dict()

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

        print("ZeroAndSnapshotData_ReubenPython2and3Class __init__: The OS platform is: " + self.my_platform)
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "GUIparametersDict" in SetupDict:
            self.GUIparametersDict = SetupDict["GUIparametersDict"]

            #########################################################
            #########################################################
            if "USE_GUI_FLAG" in self.GUIparametersDict:
                self.USE_GUI_FLAG = self.PassThrough0and1values_ExitProgramOtherwise("USE_GUI_FLAG", self.GUIparametersDict["USE_GUI_FLAG"])
            else:
                self.USE_GUI_FLAG = 0

            print("ZeroAndSnapshotData_ReubenPython2and3Class __init__: USE_GUI_FLAG: " + str(self.USE_GUI_FLAG))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "EnableInternal_MyPrint_Flag" in self.GUIparametersDict:
                self.EnableInternal_MyPrint_Flag = self.PassThrough0and1values_ExitProgramOtherwise("EnableInternal_MyPrint_Flag", self.GUIparametersDict["EnableInternal_MyPrint_Flag"])
            else:
                self.EnableInternal_MyPrint_Flag = 0

            print("ZeroAndSnapshotData_ReubenPython2and3Class __init__: EnableInternal_MyPrint_Flag: " + str(self.EnableInternal_MyPrint_Flag))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "PrintToConsoleFlag" in self.GUIparametersDict:
                self.PrintToConsoleFlag = self.PassThrough0and1values_ExitProgramOtherwise("PrintToConsoleFlag", self.GUIparametersDict["PrintToConsoleFlag"])
            else:
                self.PrintToConsoleFlag = 1

            print("ZeroAndSnapshotData_ReubenPython2and3Class __init__: PrintToConsoleFlag: " + str(self.PrintToConsoleFlag))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "NumberOfPrintLines" in self.GUIparametersDict:
                self.NumberOfPrintLines = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("NumberOfPrintLines", self.GUIparametersDict["NumberOfPrintLines"], 0.0, 50.0))
            else:
                self.NumberOfPrintLines = 10

            print("ZeroAndSnapshotData_ReubenPython2and3Class __init__: NumberOfPrintLines: " + str(self.NumberOfPrintLines))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "UseBorderAroundThisGuiObjectFlag" in self.GUIparametersDict:
                self.UseBorderAroundThisGuiObjectFlag = self.PassThrough0and1values_ExitProgramOtherwise("UseBorderAroundThisGuiObjectFlag", self.GUIparametersDict["UseBorderAroundThisGuiObjectFlag"])
            else:
                self.UseBorderAroundThisGuiObjectFlag = 0

            print("ZeroAndSnapshotData_ReubenPython2and3Class __init__: UseBorderAroundThisGuiObjectFlag: " + str(self.UseBorderAroundThisGuiObjectFlag))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_ROW" in self.GUIparametersDict:
                self.GUI_ROW = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_ROW", self.GUIparametersDict["GUI_ROW"], 0.0, 1000.0))
            else:
                self.GUI_ROW = 0

            print("ZeroAndSnapshotData_ReubenPython2and3Class __init__: GUI_ROW: " + str(self.GUI_ROW))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_COLUMN" in self.GUIparametersDict:
                self.GUI_COLUMN = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_COLUMN", self.GUIparametersDict["GUI_COLUMN"], 0.0, 1000.0))
            else:
                self.GUI_COLUMN = 0

            print("ZeroAndSnapshotData_ReubenPython2and3Class __init__: GUI_COLUMN: " + str(self.GUI_COLUMN))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_PADX" in self.GUIparametersDict:
                self.GUI_PADX = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_PADX", self.GUIparametersDict["GUI_PADX"], 0.0, 1000.0))
            else:
                self.GUI_PADX = 0

            print("ZeroAndSnapshotData_ReubenPython2and3Class __init__: GUI_PADX: " + str(self.GUI_PADX))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_PADY" in self.GUIparametersDict:
                self.GUI_PADY = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_PADY", self.GUIparametersDict["GUI_PADY"], 0.0, 1000.0))
            else:
                self.GUI_PADY = 0

            print("ZeroAndSnapshotData_ReubenPython2and3Class __init__: GUI_PADY: " + str(self.GUI_PADY))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_ROWSPAN" in self.GUIparametersDict:
                self.GUI_ROWSPAN = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_ROWSPAN", self.GUIparametersDict["GUI_ROWSPAN"], 0.0, 1000.0))
            else:
                self.GUI_ROWSPAN = 1

            print("ZeroAndSnapshotData_ReubenPython2and3Class __init__: GUI_ROWSPAN: " + str(self.GUI_ROWSPAN))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_COLUMNSPAN" in self.GUIparametersDict:
                self.GUI_COLUMNSPAN = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_COLUMNSPAN", self.GUIparametersDict["GUI_COLUMNSPAN"], 0.0, 1000.0))
            else:
                self.GUI_COLUMNSPAN = 1

            print("ZeroAndSnapshotData_ReubenPython2and3Class __init__: GUI_COLUMNSPAN: " + str(self.GUI_COLUMNSPAN))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_STICKY" in self.GUIparametersDict:
                self.GUI_STICKY = str(self.GUIparametersDict["GUI_STICKY"])
            else:
                self.GUI_STICKY = "w"

            print("ZeroAndSnapshotData_ReubenPython2and3Class __init__: GUI_STICKY: " + str(self.GUI_STICKY))
            #########################################################
            #########################################################

        else:
            self.GUIparametersDict = dict()
            self.USE_GUI_FLAG = 0
            print("ZeroAndSnapshotData_ReubenPython2and3Class __init__: No GUIparametersDict present, setting USE_GUI_FLAG: " + str(self.USE_GUI_FLAG))

        #print("ZeroAndSnapshotData_ReubenPython2and3Class __init__: GUIparametersDict: " + str(self.GUIparametersDict))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "NameToDisplay_UserSet" in SetupDict:
            self.NameToDisplay_UserSet = str(SetupDict["NameToDisplay_UserSet"])
        else:
            self.NameToDisplay_UserSet = ""

        print("ZeroAndSnapshotData_ReubenPython2and3Class __init__: NameToDisplay_UserSet: " + str(self.NameToDisplay_UserSet))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        #########################################################
        #########################################################
        if "Variables_ListOfDicts" in SetupDict:

            #########################################################
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            Variables_ListOfDicts_TEMP = SetupDict["Variables_ListOfDicts"]

            if isinstance(Variables_ListOfDicts_TEMP, list) == 0:
                Variables_ListOfDicts_TEMP = [Variables_ListOfDicts_TEMP]

            self.Variables_DictOfDicts = dict()
            self.MostRecentDataDict_OnlyVariablesAndValuesDictOfDicts = dict()
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            for Variable_Dict in Variables_ListOfDicts_TEMP:

                if "Variable_Name" in Variable_Dict:

                    #########################################################
                    Variable_Name = str(Variable_Dict["Variable_Name"])
                    #########################################################

                    #########################################################
                    if "DataCollectionDurationInSecondsForSnapshottingAndZeroing" in Variable_Dict:
                        Variable_DataCollectionDurationInSecondsForSnapshottingAndZeroing = float(Variable_Dict["DataCollectionDurationInSecondsForSnapshottingAndZeroing"])
                    else:
                        Variable_DataCollectionDurationInSecondsForSnapshottingAndZeroing = 1.0 #1 second
                    #########################################################

                    #########################################################
                    self.Variables_DictOfDicts[Variable_Name] = dict([("NeedsToBeZeroedFlag", 0),
                                                                        ("NeedsToBeSnapshottedFlag", 0),
                                                                        ("DataForSnapshotting_EnableCollectionFlag", 0),
                                                                        ("DataCollectionDurationInSecondsForSnapshottingAndZeroing", Variable_DataCollectionDurationInSecondsForSnapshottingAndZeroing),
                                                                        ("Raw_CurrentValue", -11111),
                                                                        ("Filtered_CurrentValue", -11111),
                                                                        ("Raw_CurrentValue_Zeroed", -11111),
                                                                        ("Filtered_CurrentValue_Zeroed", -11111),
                                                                        ("Raw_SnapshottedValue", -11111),
                                                                        ("Filtered_SnapshottedValue", -11111),
                                                                        ("Raw_ZeroOffsetValue", 0.0),
                                                                        ("Filtered_ZeroOffsetValue", 0.0),
                                                                        ("Raw_DataForSnapshottingQueue", Queue.Queue()),
                                                                        ("Filtered_DataForSnapshottingQueue", Queue.Queue()),
                                                                        ("Raw_DataForSnapshottingQueueSize", 0),
                                                                        ("Filtered_DataForSnapshottingQueueSize", 0)])

                    self.MostRecentDataDict_OnlyVariablesAndValuesDictOfDicts[Variable_Name] = dict([("Raw_CurrentValue", -11111),
                                                                                                    ("Filtered_CurrentValue", -11111),
                                                                                                    ("Raw_CurrentValue_Zeroed", -11111),
                                                                                                    ("Filtered_CurrentValue_Zeroed", -11111),
                                                                                                    ("Raw_SnapshottedValue", -11111),
                                                                                                    ("Filtered_SnapshottedValue", -11111),
                                                                                                    ("Raw_ZeroOffsetValue", 0.0),
                                                                                                    ("Filtered_ZeroOffsetValue", 0.0),
                                                                                                    ("Raw_DataForSnapshottingQueueSize", 0),
                                                                                                    ("Filtered_DataForSnapshottingQueueSize", 0)])
                                        #########################################################

            #########################################################
            #########################################################

            #########################################################
            #########################################################
            #########################################################

        else:
            self.Variables_ListOfDicts = list()

        print("ZeroAndSnapshotData_ReubenPython2and3Class __init__: Variables_DictOfDicts: " + str(self.Variables_DictOfDicts))
        print("ZeroAndSnapshotData_ReubenPython2and3Class __init__: MostRecentDataDict_OnlyVariablesAndValuesDictOfDicts: " + str(self.MostRecentDataDict_OnlyVariablesAndValuesDictOfDicts))
        #########################################################
        #########################################################
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
        self.OBJECT_CREATED_SUCCESSFULLY_FLAG = 1
        #########################################################
        #########################################################

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
    ##########################################################################################################
    ##########################################################################################################
    def PassThrough0and1values_ExitProgramOtherwise(self, InputNameString, InputNumber, ExitProgramIfFailureFlag=1):

        ##########################################################################################################
        ##########################################################################################################
        try:

            ##########################################################################################################
            InputNumber_ConvertedToFloat = float(InputNumber)
            ##########################################################################################################

        except:

            ##########################################################################################################
            exceptions = sys.exc_info()[0]
            print("PassThrough0and1values_ExitProgramOtherwise Error. InputNumber must be a numerical value, Exceptions: %s" % exceptions)

            ##########################
            if ExitProgramIfFailureFlag == 1:
                sys.exit()
            else:
                return -1
            ##########################

            ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        try:

            ##########################################################################################################
            if InputNumber_ConvertedToFloat == 0.0 or InputNumber_ConvertedToFloat == 1.0:
                return InputNumber_ConvertedToFloat

            else:

                print("PassThrough0and1values_ExitProgramOtherwise Error. '" +
                      str(InputNameString) +
                      "' must be 0 or 1 (value was " +
                      str(InputNumber_ConvertedToFloat) +
                      ").")

                ##########################
                if ExitProgramIfFailureFlag == 1:
                    sys.exit()

                else:
                    return -1
                ##########################

            ##########################################################################################################

        except:

            ##########################################################################################################
            exceptions = sys.exc_info()[0]
            print("PassThrough0and1values_ExitProgramOtherwise Error, Exceptions: %s" % exceptions)

            ##########################
            if ExitProgramIfFailureFlag == 1:
                sys.exit()
            else:
                return -1
            ##########################

            ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    def PassThroughFloatValuesInRange_ExitProgramOtherwise(self, InputNameString, InputNumber, RangeMinValue, RangeMaxValue, ExitProgramIfFailureFlag=1):

        ##########################################################################################################
        ##########################################################################################################
        try:
            ##########################################################################################################
            InputNumber_ConvertedToFloat = float(InputNumber)
            ##########################################################################################################

        except:
            ##########################################################################################################
            exceptions = sys.exc_info()[0]
            print("PassThroughFloatValuesInRange_ExitProgramOtherwise Error. InputNumber must be a float value, Exceptions: %s" % exceptions)
            traceback.print_exc()

            ##########################
            if ExitProgramIfFailureFlag == 1:
                sys.exit()
            else:
                return -11111.0
            ##########################

            ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        try:

            ##########################################################################################################
            InputNumber_ConvertedToFloat_Limited = self.LimitNumber_FloatOutputOnly(RangeMinValue, RangeMaxValue, InputNumber_ConvertedToFloat)

            if InputNumber_ConvertedToFloat_Limited != InputNumber_ConvertedToFloat:
                print("PassThroughFloatValuesInRange_ExitProgramOtherwise Error. '" +
                      str(InputNameString) +
                      "' must be in the range [" +
                      str(RangeMinValue) +
                      ", " +
                      str(RangeMaxValue) +
                      "] (value was " +
                      str(InputNumber_ConvertedToFloat) + ")")

                ##########################
                if ExitProgramIfFailureFlag == 1:
                    sys.exit()
                else:
                    return -11111.0
                ##########################

            else:
                return InputNumber_ConvertedToFloat_Limited
            ##########################################################################################################

        except:
            ##########################################################################################################
            exceptions = sys.exc_info()[0]
            print("PassThroughFloatValuesInRange_ExitProgramOtherwise Error, Exceptions: %s" % exceptions)
            traceback.print_exc()

            ##########################
            if ExitProgramIfFailureFlag == 1:
                sys.exit()
            else:
                return -11111.0
            ##########################

            ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
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
    def getPreciseSecondsTimeStampString(self):
        ts = time.time()

        return ts
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def UpdateFrequencyCalculation_CalculatedFromUpdateFunction(self):

        try:
            self.DataStreamingDeltaT_CalculatedFromUpdateFunction = self.CurrentTime_CalculatedFromUpdateFunction - self.LastTime_CalculatedFromUpdateFunction

            if self.DataStreamingDeltaT_CalculatedFromUpdateFunction != 0.0:
                self.DataStreamingFrequency_CalculatedFromUpdateFunction = 1.0/self.DataStreamingDeltaT_CalculatedFromUpdateFunction

            self.LastTime_CalculatedFromUpdateFunction = self.CurrentTime_CalculatedFromUpdateFunction
        except:
            exceptions = sys.exc_info()[0]
            print("UpdateFrequencyCalculation_MainThread ERROR with Exceptions: %s" % exceptions)
            traceback.print_exc()
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
    def CheckStateMachine(self):

        ##########################################################################################################
        ##########################################################################################################
        for Variable_Name in self.Variables_DictOfDicts:

            if self.Variables_DictOfDicts[Variable_Name]["NeedsToBeZeroedFlag"] == 1:
                if self.Variables_DictOfDicts[Variable_Name]["DataForSnapshotting_EnableCollectionFlag"] == 0:
                    #print("Starting to collect data to Snapshot (FOR ZEROING) variable " + Variable_Name)
                    self.Variables_DictOfDicts[Variable_Name]["DataForSnapshotting_EnableCollectionFlag"] = 1
                    self.TimerCallbackFunctionWithFunctionAsArgument_SingleShot_NoParenthesesAfterFunctionName(self.Variables_DictOfDicts[Variable_Name]["DataCollectionDurationInSecondsForSnapshottingAndZeroing"], self.StopCollectingDataForSnapshotting, [Variable_Name])

                elif self.Variables_DictOfDicts[Variable_Name]["DataForSnapshotting_EnableCollectionFlag"] == 1:
                    pass

                else: #Like 2
                    #print("Computing average for channel " + str(Variable_Name))
                    self.Variables_DictOfDicts[Variable_Name]["DataForSnapshotting_EnableCollectionFlag"] = 0

                    Sum_Raw = 0.0
                    Sum_Filtered = 0.0
                    Counter = 0.0
                    while self.Variables_DictOfDicts[Variable_Name]["Raw_DataForSnapshottingQueue"].qsize() > 0:
                        Sum_Raw = Sum_Raw + self.Variables_DictOfDicts[Variable_Name]["Raw_DataForSnapshottingQueue"].get()
                        Sum_Filtered = Sum_Filtered + self.Variables_DictOfDicts[Variable_Name]["Filtered_DataForSnapshottingQueue"].get()
                        Counter = Counter + 1

                        ##########################################################################################################
                        self.Variables_DictOfDicts[Variable_Name]["Raw_DataForSnapshottingQueueSize"] = self.Variables_DictOfDicts[Variable_Name]["Raw_DataForSnapshottingQueue"].qsize()
                        self.Variables_DictOfDicts[Variable_Name]["Filtered_DataForSnapshottingQueueSize"] = self.Variables_DictOfDicts[Variable_Name]["Filtered_DataForSnapshottingQueue"].qsize()
                        ##########################################################################################################

                    if Counter > 0:
                        Average_Raw = Sum_Raw/Counter
                        Average_Filtered = Sum_Filtered/Counter
                        self.Variables_DictOfDicts[Variable_Name]["Raw_SnapshottedValue"] = Average_Raw
                        self.Variables_DictOfDicts[Variable_Name]["Filtered_SnapshottedValue"] = Average_Filtered
                    else:
                        self.Variables_DictOfDicts[Variable_Name]["Raw_SnapshottedValue"] = -11111.0
                        self.Variables_DictOfDicts[Variable_Name]["Filtered_SnapshottedValue"] = -11111.0

                    self.Variables_DictOfDicts[Variable_Name]["Raw_ZeroOffsetValue"]  = self.Variables_DictOfDicts[Variable_Name]["Raw_SnapshottedValue"]
                    self.Variables_DictOfDicts[Variable_Name]["Filtered_ZeroOffsetValue"]  = self.Variables_DictOfDicts[Variable_Name]["Filtered_SnapshottedValue"]

                    self.MyPrint_WithoutLogFile("Raw_ZeroOffsetValue for variable " + str(Variable_Name) +
                                                ":" + str(self.Variables_DictOfDicts[Variable_Name]["Raw_ZeroOffsetValue"]) +
                                                ", Filtered_ZeroOffsetValue for variable " + str(Variable_Name) +
                                                ":" + str(self.Variables_DictOfDicts[Variable_Name]["Filtered_ZeroOffsetValue"]))



                    self.Variables_DictOfDicts[Variable_Name]["NeedsToBeZeroedFlag"] = 0

        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        for Variable_Name in self.Variables_DictOfDicts:

            if self.Variables_DictOfDicts[Variable_Name]["NeedsToBeSnapshottedFlag"] == 1:

                if self.Variables_DictOfDicts[Variable_Name]["DataForSnapshotting_EnableCollectionFlag"] == 0:
                    #print("Starting to collect data to Snapshot variable " + str(Variable_Name))
                    self.Variables_DictOfDicts[Variable_Name]["DataForSnapshotting_EnableCollectionFlag"] = 1
                    self.TimerCallbackFunctionWithFunctionAsArgument_SingleShot_NoParenthesesAfterFunctionName(self.Variables_DictOfDicts[Variable_Name]["DataCollectionDurationInSecondsForSnapshottingAndZeroing"], self.StopCollectingDataForSnapshotting, [Variable_Name])

                elif self.Variables_DictOfDicts[Variable_Name]["DataForSnapshotting_EnableCollectionFlag"] == 1:
                    pass

                else: #Like 2
                    #print("Computing average for channel " + str(Variable_Name))
                    self.Variables_DictOfDicts[Variable_Name]["DataForSnapshotting_EnableCollectionFlag"] = 0

                    Sum_Raw = 0.0
                    Sum_Filtered = 0.0
                    Counter = 0.0
                    while self.Variables_DictOfDicts[Variable_Name]["Raw_DataForSnapshottingQueue"].qsize() > 0:
                        Sum_Raw = Sum_Raw + self.Variables_DictOfDicts[Variable_Name]["Raw_DataForSnapshottingQueue"].get()
                        Sum_Filtered = Sum_Filtered + self.Variables_DictOfDicts[Variable_Name]["Filtered_DataForSnapshottingQueue"].get()
                        Counter = Counter + 1

                        ##########################################################################################################
                        self.Variables_DictOfDicts[Variable_Name]["Raw_DataForSnapshottingQueueSize"] = self.Variables_DictOfDicts[Variable_Name]["Raw_DataForSnapshottingQueue"].qsize()
                        self.Variables_DictOfDicts[Variable_Name]["Filtered_DataForSnapshottingQueueSize"] = self.Variables_DictOfDicts[Variable_Name]["Filtered_DataForSnapshottingQueue"].qsize()
                        ##########################################################################################################

                    if Counter > 0:
                        Average_Raw = Sum_Raw/Counter
                        Average_Filtered = Sum_Filtered/Counter
                        self.Variables_DictOfDicts[Variable_Name]["Raw_SnapshottedValue"] = Average_Raw
                        self.Variables_DictOfDicts[Variable_Name]["Filtered_SnapshottedValue"] = Average_Filtered
                    else:
                        self.Variables_DictOfDicts[Variable_Name]["Raw_SnapshottedValue"] = -11111.0
                        self.Variables_DictOfDicts[Variable_Name]["Filtered_SnapshottedValue"] = -11111.0

                    self.MyPrint_WithoutLogFile("Raw_SnapshottedValue for variable " + str(Variable_Name) +
                                                ":" + str(self.Variables_DictOfDicts[Variable_Name]["Raw_SnapshottedValue"]) +
                                                ", Filtered_SnapshottedValue for variable " + str(Variable_Name) +
                                                ":" + str(self.Variables_DictOfDicts[Variable_Name]["Filtered_SnapshottedValue"]))

                    ##########################################################################################################
                    self.Variables_DictOfDicts[Variable_Name]["Raw_DataForSnapshottingQueueSize"] = self.Variables_DictOfDicts[Variable_Name]["Raw_DataForSnapshottingQueue"].qsize()
                    self.Variables_DictOfDicts[Variable_Name]["Filtered_DataForSnapshottingQueueSize"] = self.Variables_DictOfDicts[Variable_Name]["Filtered_DataForSnapshottingQueue"].qsize()
                    ##########################################################################################################

                    self.Variables_DictOfDicts[Variable_Name]["NeedsToBeSnapshottedFlag"] = 0
        ##########################################################################################################
        ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################

    ########################################################################################################## unicorn
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    def UpdateData(self, UpdatedActualValues_ListOfVariableDicts):

        ##########################################################################################################
        ##########################################################################################################
        try:

            ##########################################################################################################
            if isinstance(UpdatedActualValues_ListOfVariableDicts, list) == 0:
                UpdatedActualValues_ListOfVariableDicts = [UpdatedActualValues_ListOfVariableDicts]
            ##########################################################################################################

            ##########################################################################################################
            for Variable_Dict in UpdatedActualValues_ListOfVariableDicts:

                ################################
                #print("Variable_Dict: " + str(Variable_Dict))
                Variable_Name = Variable_Dict["Variable_Name"]
                ################################

                ################################
                if "Raw_CurrentValue" in Variable_Dict:
                    Updated_Raw_CurrentValue = Variable_Dict["Raw_CurrentValue"]
                else:
                    Updated_Raw_CurrentValue = self.Variables_DictOfDicts[Variable_Name]["Raw_CurrentValue"]
                ################################

                ################################
                if "Filtered_CurrentValue" in Variable_Dict:
                    Updated_Filtered_CurrentValue = Variable_Dict["Filtered_CurrentValue"]
                else:
                    Updated_Filtered_CurrentValue = self.Variables_DictOfDicts[Variable_Name]["Filtered_CurrentValue"]
                ################################

                ################################
                self.Variables_DictOfDicts[Variable_Name]["Raw_CurrentValue"] = Updated_Raw_CurrentValue #WITHOUT any offset
                self.Variables_DictOfDicts[Variable_Name]["Raw_CurrentValue_Zeroed"] = Updated_Raw_CurrentValue - self.Variables_DictOfDicts[Variable_Name]["Raw_ZeroOffsetValue"]

                #maintain a separate filtered vs raw zero value.
                self.Variables_DictOfDicts[Variable_Name]["Filtered_CurrentValue"] = Updated_Filtered_CurrentValue #WITHOUT any offset
                self.Variables_DictOfDicts[Variable_Name]["Filtered_CurrentValue_Zeroed"] = Updated_Filtered_CurrentValue - self.Variables_DictOfDicts[Variable_Name]["Filtered_ZeroOffsetValue"]
                ################################

                ################################ unicorn
                if self.Variables_DictOfDicts[Variable_Name]["DataForSnapshotting_EnableCollectionFlag"] == 1:

                    if self.Variables_DictOfDicts[Variable_Name]["NeedsToBeZeroedFlag"] == 0: #Collecting data AS IS, WITH OFFSET (without caring if we're trying to find the zero value).
                        self.Variables_DictOfDicts[Variable_Name]["Raw_DataForSnapshottingQueue"].put(self.Variables_DictOfDicts[Variable_Name]["Raw_CurrentValue_Zeroed"])
                        self.Variables_DictOfDicts[Variable_Name]["Filtered_DataForSnapshottingQueue"].put(self.Variables_DictOfDicts[Variable_Name]["Filtered_CurrentValue_Zeroed"])

                    else: #WITHOUT any offset
                        self.Variables_DictOfDicts[Variable_Name]["Raw_DataForSnapshottingQueue"].put(self.Variables_DictOfDicts[Variable_Name]["Raw_CurrentValue"])
                        self.Variables_DictOfDicts[Variable_Name]["Filtered_DataForSnapshottingQueue"].put(self.Variables_DictOfDicts[Variable_Name]["Filtered_CurrentValue"])
                ################################

                ################################
                self.Variables_DictOfDicts[Variable_Name]["Raw_DataForSnapshottingQueueSize"] = self.Variables_DictOfDicts[Variable_Name]["Raw_DataForSnapshottingQueue"].qsize()
                self.Variables_DictOfDicts[Variable_Name]["Filtered_DataForSnapshottingQueueSize"] = self.Variables_DictOfDicts[Variable_Name]["Filtered_DataForSnapshottingQueue"].qsize()
                ################################

            ##########################################################################################################

        except:
            exceptions = sys.exc_info()[0]
            print("UpdateData: Exceptions: %s" % exceptions)
            traceback.print_exc()
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        self.CurrentTime_CalculatedFromUpdateFunction = self.getPreciseSecondsTimeStampString()
        self.UpdateFrequencyCalculation_CalculatedFromUpdateFunction()
        self.DataUpdateNumber = self.DataUpdateNumber + 1
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        for Variable_Name in self.Variables_DictOfDicts:

            ##########################################################################################################
            for Key_String in ["Raw_CurrentValue",
                                "Filtered_CurrentValue",
                                "Raw_CurrentValue_Zeroed",
                                "Filtered_CurrentValue_Zeroed",
                                "Raw_SnapshottedValue",
                                "Filtered_SnapshottedValue",
                                "Raw_ZeroOffsetValue",
                                "Filtered_ZeroOffsetValue",
                                "Raw_DataForSnapshottingQueueSize",
                                "Filtered_DataForSnapshottingQueueSize"]:

                self.MostRecentDataDict_OnlyVariablesAndValuesDictOfDicts[Variable_Name][Key_String] = self.Variables_DictOfDicts[Variable_Name][Key_String]
            ##########################################################################################################

        ##########################################################################################################
        self.MostRecentDataDict = dict([("DataUpdateNumber", self.DataUpdateNumber),
                                        ("LoopFrequencyHz", self.DataStreamingFrequency_CalculatedFromUpdateFunction),
                                        ("OnlyVariablesAndValuesDictOfDicts", self.MostRecentDataDict_OnlyVariablesAndValuesDictOfDicts)])
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        #self.ActualValue_last = list(self.ActualValue)
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        # deepcopy IS required as MostRecentDataDict sometimes contains lists (e.g. self.MostRecentDataDict["DesiredValue"] can be a list).
        return deepcopy(self.MostRecentDataDict)

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def StopCollectingDataForSnapshotting(self, Variable_Name):

        self.Variables_DictOfDicts[Variable_Name]["DataForSnapshotting_EnableCollectionFlag"] = 2
        self.MyPrint_WithoutLogFile("StopCollectingDataForSnapshotting event fired for variable " + str(Variable_Name))
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def GetMostRecentDataDict(self):

        if self.EXIT_PROGRAM_FLAG == 0:

            #deepcopy IS required as MostRecentDataDict sometimes contains lists (e.g. self.MostRecentDataDict["DesiredValue"] can be a list).
            return deepcopy(self.MostRecentDataDict)

        else:
            return dict() #So that we're not returning variables during the close-down process.
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def ExitProgram_Callback(self):

        print("Exiting all threads for ZeroAndSnapshotData_ReubenPython2and3Class object")

        self.EXIT_PROGRAM_FLAG = 1

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def CreateGUIobjects(self, TkinterParent):

        print("ZeroAndSnapshotData_ReubenPython2and3Class, CreateGUIobjects event fired.")

        #################################################
        #################################################
        self.root = TkinterParent
        self.parent = TkinterParent
        #################################################
        #################################################

        #################################################
        #################################################
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
        #################################################
        #################################################

        #################################################
        #################################################
        self.TKinter_LightGreenColor = '#%02x%02x%02x' % (150, 255, 150) #RGB
        self.TKinter_LightRedColor = '#%02x%02x%02x' % (255, 150, 150) #RGB
        self.TKinter_LightYellowColor = '#%02x%02x%02x' % (255, 255, 150)  # RGB
        self.TKinter_DefaultGrayColor = '#%02x%02x%02x' % (240, 240, 240)  # RGB
        self.ButtonWidth = 30
        self.LabelWidth = 35
        self.FontSize = 12
        #################################################
        #################################################

        #################################################
        #################################################
        self.NameLabel = Label(self.myFrame, text=self.NameToDisplay_UserSet, width=100, font=("Helvetica", int(self.FontSize)))
        self.NameLabel.grid(row=0, column=0, padx=5, pady=5, columnspan=1, rowspan=1)
        #################################################
        #################################################

        #################################################
        self.Data_Label = Label(self.myFrame, text="Data_Label", width=100)
        self.Data_Label.grid(row=2, column=0, padx=5, pady=5, columnspan=1, rowspan=1)
        #################################################
        #################################################

        ###################################################
        ###################################################
        self.ButtonsFrame = Frame(self.myFrame)
        self.ButtonsFrame.grid(row = 1, column = 0, padx = 1, pady = 1, rowspan = 1, columnspan = 1)

        ###################################################
        self.IndividualZeroingButtonObjects = []
        self.IndividualSnapshottingButtonObjects = []
        ButtonColumnIndex = 0
        for Variable_Name in self.Variables_DictOfDicts:
            self.IndividualZeroingButtonObjects.append(Button(self.ButtonsFrame, text="Zero " + Variable_Name, state="normal", width=self.ButtonWidth, command=lambda i=Variable_Name: self.IndividualZeroingButtonObjectsResponse(i)))
            self.IndividualZeroingButtonObjects[ButtonColumnIndex].grid(row=0, column=ButtonColumnIndex, padx=1, pady=1)

            self.IndividualSnapshottingButtonObjects.append(Button(self.ButtonsFrame, text="Snapshot " + Variable_Name, state="normal", width=self.ButtonWidth, command=lambda i=Variable_Name: self.IndividualSnapshottingButtonObjectsResponse(i)))
            self.IndividualSnapshottingButtonObjects[ButtonColumnIndex].grid(row=1, column=ButtonColumnIndex, padx=1, pady=1)

            ButtonColumnIndex = ButtonColumnIndex + 1
        ###################################################

        ###################################################
        self.ZeroAllVariables_Button = Button(self.ButtonsFrame, text="Zero All Data", state="normal", width=self.ButtonWidth, command=lambda i=1: self.ZeroAllVariables())
        self.ZeroAllVariables_Button.grid(row=2, column=0, padx=1, pady=1, rowspan=1, columnspan=1)
        ###################################################

        ###################################################
        self.SnapshotAllVariables_Button = Button(self.ButtonsFrame, text="Snapshot All Data", state="normal", width=self.ButtonWidth, command=lambda i=1: self.SnapshotAllVariables())
        self.SnapshotAllVariables_Button.grid(row=2, column=1, padx=1, pady=1, rowspan=1, columnspan=1)
        ###################################################

        ###################################################
        ###################################################

        #################################################
        #################################################
        self.PrintToGui_Label = Label(self.myFrame, text="PrintToGui_Label", width=100)
        if self.EnableInternal_MyPrint_Flag == 1:
            self.PrintToGui_Label.grid(row=3, column=0, padx=5, pady=5, columnspan=10, rowspan=1)
        #################################################
        #################################################

        #################################################
        #################################################
        self.GUI_ready_to_be_updated_flag = 1
        #################################################
        #################################################

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def IndividualZeroingButtonObjectsResponse(self, Variable_Name):

        self.Variables_DictOfDicts[Variable_Name]["NeedsToBeZeroedFlag"] = 1
        
        self.MyPrint_WithoutLogFile("IndividualZeroingButtonObjectsResponse: Event fired for " + str(Variable_Name))

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def IndividualSnapshottingButtonObjectsResponse(self, Variable_Name):

        self.Variables_DictOfDicts[Variable_Name]["NeedsToBeSnapshottedFlag"] = 1

        self.MyPrint_WithoutLogFile("IndividualSnapshottingButtonObjectsResponse: Event fired for " + str(Variable_Name))

    ##########################################################################################################
    ##########################################################################################################

    ########################################################################################################## #lorax
    ##########################################################################################################
    def ZeroAllVariables(self):

        for Variable_Name in self.Variables_DictOfDicts:
            self.Variables_DictOfDicts[Variable_Name]["NeedsToBeZeroedFlag"] = 1

        #self.MyPrint_WithoutLogFile("ZeroAllVariables: Event fired!")

    ##########################################################################################################
    ##########################################################################################################

    ########################################################################################################## #lorax
    ##########################################################################################################
    def SnapshotAllVariables(self):

        for Variable_Name in self.Variables_DictOfDicts:
            self.Variables_DictOfDicts[Variable_Name]["NeedsToBeSnapshottedFlag"] = 1

        #self.MyPrint_WithoutLogFile("SnapshotAllVariables: Event fired!")

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
                    Data_Label_TextToDisplay = self.ConvertDictToProperlyFormattedStringForPrinting(self.MostRecentDataDict, NumberOfDecimalsPlaceToUse = 3, NumberOfEntriesPerLine = 1, NumberOfTabsBetweenItems = 3)
                    self.Data_Label["text"] = Data_Label_TextToDisplay
                    #######################################################

                    #######################################################
                    self.PrintToGui_Label.config(text=self.PrintToGui_Label_TextInput_Str)
                    #######################################################

                except:
                    exceptions = sys.exc_info()[0]
                    print("ZeroAndSnapshotData_ReubenPython2and3Class GUI_update_clock ERROR: Exceptions: %s" % exceptions)
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

