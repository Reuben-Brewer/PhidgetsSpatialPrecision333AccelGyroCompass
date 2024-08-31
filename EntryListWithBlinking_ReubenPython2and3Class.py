# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision G, 08/31/2024

Verified working on: Python 2.7, 3.8 for Windows 8.1, 10 64-bit and Raspberry Pi Buster (no Mac testing yet).
'''

__author__ = 'reuben.brewer'

#########################################################
import os
import sys
import platform
import time
import datetime
import math
import threading
import inspect #To enable 'TellWhichFileWereIn'
import traceback
#########################################################

#########################################################
if sys.version_info[0] < 3:
    from Tkinter import * #Python 2
    import tkFont
    import ttk
else:
    from tkinter import * #Python 3
    import tkinter.font as tkFont #Python 3
    from tkinter import ttk
#########################################################

#########################################################
if sys.version_info[0] < 3:
    from builtins import raw_input as input
else:
    from future.builtins import input as input
######################################################### #"sudo pip3 install future" (Python 3) AND "sudo pip install future" (Python 2)

#########################################################
import platform
if platform.system() == "Windows":
    import ctypes
    winmm = ctypes.WinDLL('winmm')
    winmm.timeBeginPeriod(1) #Set minimum timer resolution to 1ms so that time.sleep(0.001) behaves properly.
#########################################################

class EntryListWithBlinking_ReubenPython2and3Class(Frame): #Subclass the Tkinter Frame

    ##########################################################################################################
    ##########################################################################################################
    def __init__(self, setup_dict): #Subclass the Tkinter Frame

        print("#################### EntryListWithBlinking_ReubenPython2and3Class __init__ starting. ####################")

        #########################################################
        #########################################################
        self.EXIT_PROGRAM_FLAG = 0
        self.OBJECT_CREATED_SUCCESSFULLY_FLAG = 0
        self.GUI_ready_to_be_updated_flag = 0

        #################################################
        self.TKinter_LightGreenColor = '#%02x%02x%02x' % (150, 255, 150) #RGB
        self.TKinter_LightRedColor = '#%02x%02x%02x' % (255, 150, 150) #RGB
        self.TKinter_LightYellowColor = '#%02x%02x%02x' % (255, 255, 150)  # RGB
        self.TKinter_DefaultGrayColor = '#%02x%02x%02x' % (240, 240, 240)  # RGB
        self.TKinter_WhiteColor = '#%02x%02x%02x' % (255, 255, 255)  # RGB
        #################################################

        self.Variables_AcceptableTypes_ListOfStrings = ["int", "float", "str"]

        self.MostRecentDataDict = dict([("DataUpdateNumber", 0)])
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

        print("EntryListWithBlinking_ReubenPython2and3Class __init__: The OS platform is: " + self.my_platform)
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "GUIparametersDict" in setup_dict:
            self.GUIparametersDict = setup_dict["GUIparametersDict"]

            #########################################################
            #########################################################
            if "root" in self.GUIparametersDict:
                self.root = self.GUIparametersDict["root"]
            else:
                print("EntryListWithBlinking_ReubenPython2and3Class __init__: ERROR, must pass in 'root'")
                return
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "UseBorderAroundThisGuiObjectFlag" in self.GUIparametersDict:
                self.UseBorderAroundThisGuiObjectFlag = self.PassThrough0and1values_ExitProgramOtherwise("UseBorderAroundThisGuiObjectFlag", self.GUIparametersDict["UseBorderAroundThisGuiObjectFlag"])
            else:
                self.UseBorderAroundThisGuiObjectFlag = 0

            print("EntryListWithBlinking_ReubenPython2and3Class __init__: UseBorderAroundThisGuiObjectFlag: " + str(self.UseBorderAroundThisGuiObjectFlag))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_ROW" in self.GUIparametersDict:
                self.GUI_ROW = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_ROW", self.GUIparametersDict["GUI_ROW"], 0.0, 1000.0))
            else:
                self.GUI_ROW = 0

            print("EntryListWithBlinking_ReubenPython2and3Class __init__: GUI_ROW: " + str(self.GUI_ROW))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_COLUMN" in self.GUIparametersDict:
                self.GUI_COLUMN = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_COLUMN", self.GUIparametersDict["GUI_COLUMN"], 0.0, 1000.0))
            else:
                self.GUI_COLUMN = 0

            print("EntryListWithBlinking_ReubenPython2and3Class __init__: GUI_COLUMN: " + str(self.GUI_COLUMN))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_PADX" in self.GUIparametersDict:
                self.GUI_PADX = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_PADX", self.GUIparametersDict["GUI_PADX"], 0.0, 1000.0))
            else:
                self.GUI_PADX = 0

            print("EntryListWithBlinking_ReubenPython2and3Class __init__: GUI_PADX: " + str(self.GUI_PADX))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_PADY" in self.GUIparametersDict:
                self.GUI_PADY = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_PADY", self.GUIparametersDict["GUI_PADY"], 0.0, 1000.0))
            else:
                self.GUI_PADY = 0

            print("EntryListWithBlinking_ReubenPython2and3Class __init__: GUI_PADY: " + str(self.GUI_PADY))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_ROWSPAN" in self.GUIparametersDict:
                self.GUI_ROWSPAN = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_ROWSPAN", self.GUIparametersDict["GUI_ROWSPAN"], 1.0, 1000.0))
            else:
                self.GUI_ROWSPAN = 1

            print("EntryListWithBlinking_ReubenPython2and3Class __init__: GUI_ROWSPAN: " + str(self.GUI_ROWSPAN))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_COLUMNSPAN" in self.GUIparametersDict:
                self.GUI_COLUMNSPAN = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_COLUMNSPAN", self.GUIparametersDict["GUI_COLUMNSPAN"], 1.0, 1000.0))
            else:
                self.GUI_COLUMNSPAN = 1

            print("EntryListWithBlinking_ReubenPython2and3Class __init__: GUI_COLUMNSPAN: " + str(self.GUI_COLUMNSPAN))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_STICKY" in self.GUIparametersDict:
                self.GUI_STICKY = str(self.GUIparametersDict["GUI_STICKY"])
            else:
                self.GUI_STICKY = "w"

            print("EntryListWithBlinking_ReubenPython2and3Class __init__: GUI_STICKY: " + str(self.GUI_STICKY))
            #########################################################
            #########################################################

        else:
            self.GUIparametersDict = dict()
            print("EntryListWithBlinking_ReubenPython2and3Class __init__: ERROR, must pass in GUIparametersDict.")
            return
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "DebugByPrintingVariablesFlag" in setup_dict:
            self.DebugByPrintingVariablesFlag = self.PassThrough0and1values_ExitProgramOtherwise("DebugByPrintingVariablesFlag", setup_dict["DebugByPrintingVariablesFlag"])
        else:
            self.DebugByPrintingVariablesFlag = 0

        print("EntryListWithBlinking_ReubenPython2and3Class __init__: DebugByPrintingVariablesFlag: " + str(self.DebugByPrintingVariablesFlag))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "LoseFocusIfMouseLeavesEntryFlag" in setup_dict:
            self.LoseFocusIfMouseLeavesEntryFlag = self.PassThrough0and1values_ExitProgramOtherwise("LoseFocusIfMouseLeavesEntryFlag", setup_dict["LoseFocusIfMouseLeavesEntryFlag"])
        else:
            self.LoseFocusIfMouseLeavesEntryFlag = 1

        print("EntryListWithBlinking_ReubenPython2and3Class __init__: LoseFocusIfMouseLeavesEntryFlag: " + str(self.LoseFocusIfMouseLeavesEntryFlag))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        #########################################################
        #########################################################
        try:
            self.EntryListWithBlinking_Variables_DictOfDicts = dict()

            #########################################################
            #########################################################
            #########################################################
            #########################################################
            #########################################################
            #########################################################
            #########################################################
            if "EntryListWithBlinking_Variables_ListOfDicts" in setup_dict:
                EntryListWithBlinking_Variables_ListOfDicts_TEMP = setup_dict["EntryListWithBlinking_Variables_ListOfDicts"]

                #########################################################
                #########################################################
                #########################################################
                #########################################################
                #########################################################
                #########################################################
                if self.IsInputList(EntryListWithBlinking_Variables_ListOfDicts_TEMP) == 1:

                    #########################################################
                    #########################################################
                    #########################################################
                    #########################################################
                    #########################################################
                    for counter, Variable_dict in enumerate(EntryListWithBlinking_Variables_ListOfDicts_TEMP):

                        #########################################################
                        #########################################################
                        #########################################################
                        #########################################################
                        if "Name" in Variable_dict:
                            Variable_name = Variable_dict["Name"]

                            #########################################################
                            #########################################################
                            #########################################################
                            if "Type" in Variable_dict:

                                #############################
                                Variable_type = Variable_dict["Type"]
                                #############################

                                #############################
                                if "EntryBlinkEnabled" in Variable_dict:
                                    Variable_EntryBlinkEnabled = self.PassThrough0and1values_ExitProgramOtherwise(Variable_name + ", EntryBlinkEnabled", Variable_dict["EntryBlinkEnabled"])
                                else:
                                    Variable_EntryBlinkEnabled = 0
                                #############################

                                #############################
                                if "EntryBlinkInactiveColor" in Variable_dict:
                                    Variable_EntryBlinkInactiveColor = Variable_dict["EntryBlinkInactiveColor"]
                                else:
                                    Variable_EntryBlinkInactiveColor = self.TKinter_WhiteColor
                                #############################

                                #############################
                                if "EntryBlinkActiveColor" in Variable_dict:
                                    Variable_EntryBlinkActiveColor = Variable_dict["EntryBlinkActiveColor"]
                                else:
                                    Variable_EntryBlinkActiveColor = self.TKinter_LightRedColor
                                #############################

                                #############################
                                if "EntryWidth" in Variable_dict:
                                    Variable_EntryWidth = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise(Variable_name + ", EntryWidth", Variable_dict["EntryWidth"], 5, 500))
                                else:
                                    Variable_EntryWidth = 10
                                #############################

                                #############################
                                if "LabelWidth" in Variable_dict:
                                    Variable_LabelWidth = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise(Variable_name + ", LabelWidth", Variable_dict["LabelWidth"], 5, 500))
                                else:
                                    Variable_LabelWidth = 25
                                #############################

                                #############################
                                if "FontSize" in Variable_dict:
                                    Variable_FontSize = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise(Variable_name + ", FontSize", Variable_dict["FontSize"], 8, 500))
                                else:
                                    Variable_FontSize = 8
                                #############################

                                #############################
                                Variable_BlinkDict = dict([("EntryBlinkEnabled", Variable_EntryBlinkEnabled),
                                                            ("EntryBlinkInactiveColor", Variable_EntryBlinkInactiveColor),
                                                            ("EntryBlinkActiveColor", Variable_EntryBlinkActiveColor),
                                                            ("ActivelyBlinking", 0),
                                                            ("ActivelyBlinking_last", 0),
                                                            ("NeedToBlinkBackgroundFlag", 0),
                                                            ("NeedToBlinkBackgroundFlag_last", 0),
                                                            ("CurrentBlinkTime", 0),
                                                            ("LastBlinkTime", 0),
                                                            ("BlinkDuration", 1.0),
                                                            ("BlinkState", 0)])
                                #############################

                                #########################################################
                                #########################################################
                                if Variable_type in self.Variables_AcceptableTypes_ListOfStrings:

                                    #########################################################
                                    if Variable_type == "int" or Variable_type == "float":

                                        #############################
                                        if "MinVal" in Variable_dict:
                                            Variable_MinVal =  self.PassThroughFloatValuesInRange_ExitProgramOtherwise(Variable_name + ", Minval", Variable_dict["MinVal"], -sys.float_info.max, sys.float_info.max)
                                        else:
                                            Variable_MinVal = -sys.float_info.max
                                        #############################

                                        #############################
                                        if "MaxVal" in Variable_dict:
                                            Variable_MaxVal =  self.PassThroughFloatValuesInRange_ExitProgramOtherwise(Variable_name + ", Maxval", Variable_dict["MaxVal"], -sys.float_info.max, sys.float_info.max)
                                        else:
                                            Variable_MaxVal = sys.float_info.max
                                        #############################

                                        #############################
                                        if "StartingVal" in Variable_dict:
                                            Variable_StartingVal_validated = self.PassThroughFloatValuesInRange_ExitProgramOtherwise(Variable_name + ", StartingVal", Variable_dict["StartingVal"], Variable_MinVal, Variable_MaxVal)
                                        else:
                                            Variable_StartingVal_validated = 0.0
                                        #############################

                                        #############################
                                        if Variable_type == "int":
                                            Variable_MinVal = int(Variable_MinVal)
                                            Variable_MaxVal = int(Variable_MaxVal)
                                            Variable_StartingVal_validated = int(Variable_StartingVal_validated)
                                        #############################

                                    #########################################################

                                    #########################################################
                                    elif Variable_type == "str":
                                        Variable_MinVal = ""
                                        Variable_MaxVal = ""
                                        Variable_StartingVal_validated = str(Variable_dict["StartingVal"])
                                    #########################################################

                                    #########################################################
                                    self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name] = dict([("Value", Variable_StartingVal_validated),
                                                                                                            ("Type", Variable_type),
                                                                                                            ("StartingVal", Variable_StartingVal_validated),
                                                                                                            ("MinVal", Variable_MinVal),
                                                                                                            ("MaxVal", Variable_MaxVal),
                                                                                                            ("EntryWidth", Variable_EntryWidth),
                                                                                                            ("LabelWidth", Variable_LabelWidth),
                                                                                                            ("FontSize", Variable_FontSize),
                                                                                                            ("BlinkDict", Variable_BlinkDict)])
                                    self.MostRecentDataDict[Variable_name] = Variable_StartingVal_validated
                                    #########################################################

                                #########################################################
                                #########################################################

                                #########################################################
                                #########################################################
                                else:
                                    print("EntryListWithBlinking_ReubenPython2and3Class  __init__ ERROR: Variable '" + Variable_name + "' must have type " + str(self.Variables_AcceptableTypes_ListOfStrings))
                                #########################################################
                                #########################################################

                            #########################################################
                            #########################################################
                            #########################################################

                            #########################################################
                            #########################################################
                            #########################################################
                            else:
                                print("EntryListWithBlinking_ReubenPython2and3Class  __init__ ERROR: Variable '" + Variable_name + "' must have type " + str(self.Variables_AcceptableTypes_ListOfStrings))
                            #########################################################
                            #########################################################
                            #########################################################

                        #########################################################
                        #########################################################
                        #########################################################
                        #########################################################

                        #########################################################
                        #########################################################
                        #########################################################
                        #########################################################
                        else:
                            print("EntryListWithBlinking_ReubenPython2and3Class  __init__ ERROR: Must include 'name' for each variable.")
                        #########################################################
                        #########################################################
                        #########################################################
                        #########################################################

                    #########################################################
                    #########################################################
                    #########################################################
                    #########################################################
                    #########################################################

                #########################################################
                #########################################################
                #########################################################
                #########################################################
                #########################################################
                #########################################################

            #########################################################
            #########################################################
            #########################################################
            #########################################################
            #########################################################
            #########################################################
            #########################################################
            else:
                pass
            #########################################################
            #########################################################
            #########################################################
            #########################################################
            #########################################################
            #########################################################
            #########################################################

            print("EntryListWithBlinking_Variables_DictOfDicts: " + str(self.EntryListWithBlinking_Variables_DictOfDicts))

            #########################################################
            #########################################################
            #########################################################
            #########################################################
            #########################################################
            #########################################################
            #########################################################

        except:
            exceptions = sys.exc_info()[0]
            print("EntryListWithBlinking_ReubenPython2and3Class  __init__: EntryListWithBlinking_Variables_ListOfDicts, Exceptions: %s" % exceptions)
            traceback.print_exc()
        #########################################################
        #########################################################
        #########################################################
        #########################################################
        #########################################################
        #########################################################
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.StartGUI(self.root)
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        time.sleep(0.25)
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
    def __del__(self):
        pass
    ##########################################################################################################
    ##########################################################################################################

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
    def getPreciseSecondsTimeStampString(self):
        ts = time.time()

        return ts
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def SetEntryValue(self, Variable_name, Value):

        if isinstance(Value, float) == 1 or isinstance(Value, int) == 1:
            Value = self.LimitNumber(self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["MinVal"], self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["MaxVal"], Value)

        if isinstance(Value, int) == 1:
            Value = int(Value)

        self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name][Value] = Value
        self.MostRecentDataDict[Variable_name] = Value

        self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["StringVar"].set(str(Value))
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def SetEntryEnabledState(self, Variable_name, EnabledState):

        if EnabledState == 0:
            self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["Entry"].config(state= "disabled")

        elif EnabledState == 1:
            self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["Entry"].config(state= "normal")

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def GetMostRecentDataDict(self):

        if self.EXIT_PROGRAM_FLAG == 0:
            return self.MostRecentDataDict.copy() #deepcopy is not required as MostRecentDataDict only contains numbers (no lists, dicts, etc. that go beyond 1-level).

        else:
            return dict() #So that we're not returning variables during the close-down process.
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def ExitProgram_Callback(self):

        print("Exiting all threads for EntryListWithBlinking_ReubenPython2and3Class object")

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

        #################################################
        self.root = parent
        self.parent = parent
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
        self.EntryFrame = Frame(self.myFrame)
        self.EntryFrame.grid(row=0, column=0, padx=1, pady=1, rowspan=1, columnspan=1)
        #################################################

        #################################################
        self.DebugByPrintingVariables_Label = Label(self.myFrame, text="DebugByPrintingVariables_Label", width=50)
        if self.DebugByPrintingVariablesFlag == 1:
            self.DebugByPrintingVariables_Label.grid(row=0, column=1, padx=1, pady=1, columnspan=1, rowspan=1)
        #################################################

        ####################################################
        EntryRow = 0
        for Variable_name in self.EntryListWithBlinking_Variables_DictOfDicts:

            self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["Label"] = Label(self.EntryFrame, text=Variable_name, width=self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["LabelWidth"], font=("Helvetica", int(self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["FontSize"])))
            self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["Label"].grid(row=EntryRow, column=0, padx=1, pady=1, columnspan=1, rowspan=1)

            self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["StringVar"] = StringVar()
            self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["StringVar"].set(str(self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["StartingVal"]))

            self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["Entry"] = Entry(self.EntryFrame,
                                                font=("Helvetica", int(self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["FontSize"])),
                                                state="normal",
                                                width=int(self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["EntryWidth"]),
                                                textvariable=self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["StringVar"],
                                                justify='center')

            self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["Entry"].grid(row=EntryRow, column=1, padx=0, pady=0, columnspan=1, rowspan=1)
            self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["Entry"].bind('<Return>', lambda event, Variable_name=Variable_name: self.EntryEventResponse(event, Variable_name))
            self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["Entry"].bind('<ButtonPress-1>', lambda event, Variable_name=Variable_name: self.EntryEventResponse(event, Variable_name))

            if self.LoseFocusIfMouseLeavesEntryFlag == 1:
                self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["Entry"].bind('<Leave>', lambda event, Variable_name=Variable_name: self.EntryEventResponse(event, Variable_name))

            EntryRow = EntryRow + 1
        ###################################################

        #################################################
        self.GUI_ready_to_be_updated_flag = 1
        #################################################

    ##########################################################################################################
    ##########################################################################################################

    ###########################################################################################################
    ##########################################################################################################
    def EntryEventResponse(self, event, Variable_name):

        #################################################Take away focus so that we're not continuing to tpye into entry when logging waypoints.
        self.myFrame.focus_set()
        #################################################

        try:
            Value = self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["StringVar"].get()

            #################################################
            if self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["Type"] == "int" or self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["Type"] == "float":

                if str(Value) != "":

                    try:
                        Value = self.LimitTextEntryInput(self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["MinVal"], self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["MaxVal"], Value, self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["StringVar"])

                        if self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["Type"] == "int":
                            Value = int(Value)
                            self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["StringVar"].set(Value) #if we don't set the integer value, then it appears as a float

                        elif self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["Type"] == "float":
                            Value = float(Value)

                        self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["Value"] = Value
                        self.MostRecentDataDict[Variable_name] = Value
                        self.MostRecentDataDict["DataUpdateNumber"] = self.MostRecentDataDict["DataUpdateNumber"] + 1

                    except:
                        pass

            else: #string
                self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["Value"] = Value
                self.MostRecentDataDict[Variable_name] = Value
                self.MostRecentDataDict["DataUpdateNumber"] = self.MostRecentDataDict["DataUpdateNumber"] + 1

            #print("EntryEventResponse event fired on '" + Variable_name + "', Value =  " + str(Value) + ", MostRecentDataDict: " + str(self.MostRecentDataDict))
            #################################################

            #################################################
            if self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["BlinkDict"]["EntryBlinkEnabled"] == 1:
                if str(Value) == "":
                    self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["BlinkDict"]["ActivelyBlinking"] = 1
                else:
                    self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["BlinkDict"]["ActivelyBlinking"] = 0
            #################################################

        except:
            exceptions = sys.exc_info()[0]
            print("Variable_dictEntryEventResponse ERROR: Exceptions: %s" % exceptions, 0)
            traceback.print_exc()
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def GUI_update_clock(self):

        #######################################################
        #######################################################
        #######################################################
        #######################################################
        if self.EXIT_PROGRAM_FLAG == 0:

            #######################################################
            #######################################################
            #######################################################
            if self.GUI_ready_to_be_updated_flag == 1:

                #######################################################
                #######################################################
                try:

                    ######################################################## Blinking code
                    ########################################################
                    TextToDisplay = ""
                    for Variable_name in self.EntryListWithBlinking_Variables_DictOfDicts:

                        if self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["Type"] == "str":
                            ValueString = self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["Value"]
                        elif self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["Type"] == "int":
                            ValueString = str(self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["Value"])
                        elif self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["Type"] == "float":
                            ValueString = self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["Value"], 0, 3)
                        else:
                            ValueString = ""

                        TextToDisplay = TextToDisplay + Variable_name + ": " + ValueString + "\n"

                        Variable_BlinkDict = self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["BlinkDict"]

                        if Variable_BlinkDict["EntryBlinkEnabled"] == 1:

                            if Variable_BlinkDict["ActivelyBlinking"] == 1:

                                Variable_BlinkDict["CurrentBlinkTime"] = self.getPreciseSecondsTimeStampString()

                                if Variable_BlinkDict["CurrentBlinkTime"] - Variable_BlinkDict["LastBlinkTime"] >= Variable_BlinkDict["BlinkDuration"]:

                                    if Variable_BlinkDict["BlinkState"] == 0:
                                        Variable_BlinkDict["BlinkState"] = 1
                                        self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["Entry"].configure(bg=Variable_BlinkDict["EntryBlinkActiveColor"])

                                    elif Variable_BlinkDict["BlinkState"] == 1:
                                        Variable_BlinkDict["BlinkState"] = 0
                                        self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["Entry"].configure(bg=Variable_BlinkDict["EntryBlinkInactiveColor"])

                                    Variable_BlinkDict["LastBlinkTime"] = Variable_BlinkDict["CurrentBlinkTime"]

                            elif Variable_BlinkDict["ActivelyBlinking"] == 0 and Variable_BlinkDict["ActivelyBlinking_last"] == 1:
                                Variable_BlinkDict["BlinkState"] = 0
                                self.EntryListWithBlinking_Variables_DictOfDicts[Variable_name]["Entry"].configure(bg=Variable_BlinkDict["EntryBlinkInactiveColor"])

                            Variable_BlinkDict["ActivelyBlinking_last"] = Variable_BlinkDict["ActivelyBlinking"]
                    ########################################################
                    ########################################################

                    ########################################################
                    ########################################################
                    self.DebugByPrintingVariables_Label["text"] = TextToDisplay
                    ########################################################
                    ########################################################

                except:
                    exceptions = sys.exc_info()[0]
                    print("EntryListWithBlinking_ReubenPython2and3Class GUI_update_clock ERROR: Exceptions: %s" % exceptions)
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
    def LimitNumber(self, min_val, max_val, test_val):

        if test_val > max_val:
            test_val = max_val

        elif test_val < min_val:
            test_val = min_val

        else:
            test_val = test_val

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
