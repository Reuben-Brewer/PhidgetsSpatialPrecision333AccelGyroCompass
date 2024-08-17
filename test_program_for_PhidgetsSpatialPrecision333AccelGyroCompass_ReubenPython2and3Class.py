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
from EntryListWithBlinking_ReubenPython2and3Class import *
from MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class import *
from MyPrint_ReubenPython2and3Class import *
from PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class import *
###########################################################

###########################################################
import os
import sys
import platform
import time
import datetime
import threading
import collections
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
import platform
if platform.system() == "Windows":
    import ctypes
    winmm = ctypes.WinDLL('winmm')
    winmm.timeBeginPeriod(1) #Set minimum timer resolution to 1ms so that time.sleep(0.001) behaves properly.
###########################################################

###########################################################################################################
##########################################################################################################
def getPreciseSecondsTimeStampString():
    ts = time.time()

    return ts
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
def ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(input, number_of_leading_numbers = 4, number_of_decimal_places = 3):

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
                ListOfStringsToJoin.append(ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(element, number_of_leading_numbers, number_of_decimal_places))

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
                ListOfStringsToJoin.append("TUPLE" + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(element, number_of_leading_numbers, number_of_decimal_places))

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
                ListOfStringsToJoin.append(str(Key) + ": " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(input[Key], number_of_leading_numbers, number_of_decimal_places))

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
def ConvertDictToProperlyFormattedStringForPrinting(DictToPrint, NumberOfDecimalsPlaceToUse = 3, NumberOfEntriesPerLine = 1, NumberOfTabsBetweenItems = 3):

    ProperlyFormattedStringForPrinting = ""
    ItemsPerLineCounter = 0

    for Key in DictToPrint:

        if isinstance(DictToPrint[Key], dict): #RECURSION
            ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + \
                                                 str(Key) + ":\n" + \
                                                 ConvertDictToProperlyFormattedStringForPrinting(DictToPrint[Key], NumberOfDecimalsPlaceToUse, NumberOfEntriesPerLine, NumberOfTabsBetweenItems)

        else:
            ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + \
                                                 str(Key) + ": " + \
                                                 ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(DictToPrint[Key], 0, NumberOfDecimalsPlaceToUse)

        if ItemsPerLineCounter < NumberOfEntriesPerLine - 1:
            ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + "\t"*NumberOfTabsBetweenItems
            ItemsPerLineCounter = ItemsPerLineCounter + 1
        else:
            ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + "\n"
            ItemsPerLineCounter = 0

    return ProperlyFormattedStringForPrinting
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def UpdateFrequencyCalculation():
    global CurrentTime_MainLoopThread
    global LastTime_MainLoopThread
    global DataStreamingFrequency_MainLoopThread
    global DataStreamingDeltaT_MainLoopThread
    global Counter_MainLoopThread

    try:
        DataStreamingDeltaT_MainLoopThread = CurrentTime_MainLoopThread - LastTime_MainLoopThread

        if DataStreamingDeltaT_MainLoopThread != 0.0:
            DataStreamingFrequency_MainLoopThread = 1.0 / DataStreamingDeltaT_MainLoopThread

        LastTime_MainLoopThread = CurrentTime_MainLoopThread
        Counter_MainLoopThread = Counter_MainLoopThread + 1

    except:
        exceptions = sys.exc_info()[0]
        print("UpdateFrequencyCalculation ERROR, Exceptions: %s" % exceptions)
        traceback.print_exc()
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_update_clock():
    global root
    global EXIT_PROGRAM_FLAG
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_GUI_FLAG

    global PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3ClassObject
    global SpatialPrecision333_OPEN_FLAG
    global SHOW_IN_GUI_SpatialPrecision333_FLAG

    global EntryListWithBlinking_ReubenPython2and3ClassObject
    global EntryListWithBlinking_OPEN_FLAG
    global SHOW_IN_GUI_EntryListWithBlinking_FLAG

    global MyPrint_ReubenPython2and3ClassObject
    global MyPrint_OPEN_FLAG
    global SHOW_IN_GUI_MyPrint_FLAG

    if USE_GUI_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
        #########################################################
        #########################################################

            #########################################################
            if SpatialPrecision333_OPEN_FLAG == 1 and SHOW_IN_GUI_SpatialPrecision333_FLAG == 1:
                PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3ClassObject.GUI_update_clock()
            #########################################################

            #########################################################
            if EntryListWithBlinking_OPEN_FLAG == 1 and SHOW_IN_GUI_EntryListWithBlinking_FLAG == 1:
                EntryListWithBlinking_ReubenPython2and3ClassObject.GUI_update_clock()
            #########################################################

            #########################################################
            if MyPrint_OPEN_FLAG == 1 and SHOW_IN_GUI_MyPrint_FLAG == 1:
                MyPrint_ReubenPython2and3ClassObject.GUI_update_clock()
            #########################################################

            root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
        #########################################################
        #########################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ExitProgram_Callback():
    global EXIT_PROGRAM_FLAG

    print("ExitProgram_Callback event fired!")

    EXIT_PROGRAM_FLAG = 1
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_Thread():
    global root
    global root_Xpos
    global root_Ypos
    global root_width
    global root_height
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_TABS_IN_GUI_FLAG

    ################################################# KEY GUI LINE
    #################################################
    root = Tk()
    #################################################
    #################################################

    #################################################
    #################################################
    global TabControlObject
    global Tab_MainControls
    global Tab_SpatialPrecision333
    global Tab_EntryListWithBlinking
    global Tab_MyPrint

    if USE_TABS_IN_GUI_FLAG == 1:
        #################################################
        TabControlObject = ttk.Notebook(root)

        Tab_SpatialPrecision333 = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_SpatialPrecision333, text='   SpatialPrecision333   ')

        Tab_MainControls = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_MainControls, text='   Main Controls   ')

        Tab_EntryListWithBlinking = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_EntryListWithBlinking, text='   EntryListWithBlinking   ')

        Tab_MyPrint = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_MyPrint, text='   MyPrint Terminal   ')

        TabControlObject.pack(expand=1, fill="both")  # CANNOT MIX PACK AND GRID IN THE SAME FRAME/TAB, SO ALL .GRID'S MUST BE CONTAINED WITHIN THEIR OWN FRAME/TAB.

        ############# #Set the tab header font
        TabStyle = ttk.Style()
        TabStyle.configure('TNotebook.Tab', font=('Helvetica', '12', 'bold'))
        #############
        #################################################
    else:
        #################################################
        Tab_MainControls = root
        Tab_SpatialPrecision333 = root
        Tab_EntryListWithBlinking = root
        Tab_MyPrint = root
        #################################################

    #################################################
    #################################################

    ################################################# THIS BLOCK MUST COME 2ND-TO-LAST IN def GUI_Thread() IF USING TABS.
    root.protocol("WM_DELETE_WINDOW", ExitProgram_Callback)  # Set the callback function for when the window's closed.
    root.title("test_program_for_PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class")
    root.geometry('%dx%d+%d+%d' % (root_width, root_height, root_Xpos, root_Ypos)) # set the dimensions of the screen and where it is placed
    root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
    root.mainloop()
    #################################################

    #################################################  THIS BLOCK MUST COME LAST IN def GUI_Thread() REGARDLESS OF CODE.
    root.quit() #Stop the GUI thread, MUST BE CALLED FROM GUI_Thread
    root.destroy() #Close down the GUI thread, MUST BE CALLED FROM GUI_Thread
    #################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
if __name__ == '__main__':

    #################################################
    #################################################
    global my_platform

    if platform.system() == "Linux":

        if "raspberrypi" in platform.uname():  # os.uname() doesn't work in windows
            my_platform = "pi"
        else:
            my_platform = "linux"

    elif platform.system() == "Windows":
        my_platform = "windows"

    elif platform.system() == "Darwin":
        my_platform = "mac"

    else:
        my_platform = "other"

    print("The OS platform is: " + my_platform)
    #################################################
    #################################################

    #################################################
    #################################################
    global USE_GUI_FLAG
    USE_GUI_FLAG = 1

    global USE_TABS_IN_GUI_FLAG
    USE_TABS_IN_GUI_FLAG = 1

    global USE_SpatialPrecision333_FLAG
    USE_SpatialPrecision333_FLAG = 1

    global USE_EntryListWithBlinking_FLAG
    USE_EntryListWithBlinking_FLAG = 1

    global USE_MyPrint_FLAG
    USE_MyPrint_FLAG = 1

    global USE_PLOTTER_FLAG
    USE_PLOTTER_FLAG = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global SHOW_IN_GUI_SpatialPrecision333_FLAG
    SHOW_IN_GUI_SpatialPrecision333_FLAG = 1

    global SHOW_IN_GUI_EntryListWithBlinking_FLAG
    SHOW_IN_GUI_EntryListWithBlinking_FLAG = 1

    global SHOW_IN_GUI_MyPrint_FLAG
    SHOW_IN_GUI_MyPrint_FLAG = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global GUI_ROW_SpatialPrecision333
    global GUI_COLUMN_SpatialPrecision333
    global GUI_PADX_SpatialPrecision333
    global GUI_PADY_SpatialPrecision333
    global GUI_ROWSPAN_SpatialPrecision333
    global GUI_COLUMNSPAN_SpatialPrecision333
    GUI_ROW_SpatialPrecision333 = 1

    GUI_COLUMN_SpatialPrecision333 = 0
    GUI_PADX_SpatialPrecision333 = 1
    GUI_PADY_SpatialPrecision333 = 1
    GUI_ROWSPAN_SpatialPrecision333 = 1
    GUI_COLUMNSPAN_SpatialPrecision333 = 1

    global GUI_ROW_EntryListWithBlinking
    global GUI_COLUMN_EntryListWithBlinking
    global GUI_PADX_EntryListWithBlinking
    global GUI_PADY_EntryListWithBlinking
    global GUI_ROWSPAN_EntryListWithBlinking
    global GUI_COLUMNSPAN_EntryListWithBlinking
    GUI_ROW_EntryListWithBlinking = 2

    GUI_COLUMN_EntryListWithBlinking = 0
    GUI_PADX_EntryListWithBlinking = 1
    GUI_PADY_EntryListWithBlinking = 1
    GUI_ROWSPAN_EntryListWithBlinking = 1
    GUI_COLUMNSPAN_EntryListWithBlinking = 1

    global GUI_ROW_MyPrint
    global GUI_COLUMN_MyPrint
    global GUI_PADX_MyPrint
    global GUI_PADY_MyPrint
    global GUI_ROWSPAN_MyPrint
    global GUI_COLUMNSPAN_MyPrint
    GUI_ROW_MyPrint = 3

    GUI_COLUMN_MyPrint = 0
    GUI_PADX_MyPrint = 1
    GUI_PADY_MyPrint = 1
    GUI_ROWSPAN_MyPrint = 1
    GUI_COLUMNSPAN_MyPrint = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global EXIT_PROGRAM_FLAG
    EXIT_PROGRAM_FLAG = 0

    global CurrentTime_MainLoopThread
    CurrentTime_MainLoopThread = -11111.0

    global LastTime_MainLoopThread
    LastTime_MainLoopThread = -11111.0

    global DataStreamingFrequency_MainLoopThread
    DataStreamingFrequency_MainLoopThread = -11111.0

    global DataStreamingDeltaT_MainLoopThread
    DataStreamingDeltaT_MainLoopThread = -11111.0

    global StartingTime_MainLoopThread
    StartingTime_MainLoopThread = -1

    global Counter_MainLoopThread
    Counter_MainLoopThread = 0

    global root

    global root_Xpos
    root_Xpos = 900

    global root_Ypos
    root_Ypos = 0

    global root_width
    root_width = 1920 - root_Xpos

    global root_height
    root_height = 1020 - root_Ypos

    global TabControlObject
    global Tab_MainControls
    global Tab_EntryListWithBlinking
    global Tab_SpatialPrecision333
    global Tab_MyPrint

    global GUI_RootAfterCallbackInterval_Milliseconds
    GUI_RootAfterCallbackInterval_Milliseconds = 30
    #################################################
    #################################################

    #################################################
    #################################################
    global PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3ClassObject

    global SpatialPrecision333_OPEN_FLAG
    SpatialPrecision333_OPEN_FLAG = -1

    global SpatialPrecision333_MostRecentDict
    SpatialPrecision333_MostRecentDict = dict()

    global SpatialPrecision333_MostRecentDict_Quaternions_DirectFromDataEventHandler
    SpatialPrecision333_MostRecentDict_Quaternions_DirectFromDataEventHandler = [-11111.0]*4

    global SpatialPrecision333_MostRecentDict_RollPitchYaw_AbtXYZ_Dict
    SpatialPrecision333_MostRecentDict_RollPitchYaw_AbtXYZ_Dict = dict([("RollPitchYaw_AbtXYZ_List_Degrees",[-11111.0]*3),("RollPitchYaw_AbtXYZ_List_Radians",[-11111.0]*3)])

    global SpatialPrecision333_MostRecentDict_RollPitchYaw_Rate_AbtXYZ_Dict
    SpatialPrecision333_MostRecentDict_RollPitchYaw_Rate_AbtXYZ_Dict = dict([("RollPitchYaw_Rate_AbtXYZ_List_DegreesPerSecond",[-11111.0]*3),("RollPitchYaw_Rate_AbtXYZ_List_RadiansPerSecond",[-11111.0]*3)])

    global SpatialPrecision333_MostRecentDict_DataStreamingFrequency_CalculatedFromMainThread
    SpatialPrecision333_MostRecentDict_DataStreamingFrequency_CalculatedFromMainThread = -11111.0

    global SpatialPrecision333_MostRecentDict_DataStreamingFrequency_TimestampFromPhidget_AlgorithmData_Quaternions
    SpatialPrecision333_MostRecentDict_DataStreamingFrequency_TimestampFromPhidget_AlgorithmData_Quaternions = -11111.0

    global SpatialPrecision333_MostRecentDict_Time
    SpatialPrecision333_MostRecentDict_Time = -11111.0

    '''
    angularVelocityThreshold(type: float): The maximum angular velocity reading where the device is assumed to be "at rest"
    The closer you can set this value to zero, the slower the device needs to turn (or think it’s turning) to stop adjusting the gyro biases. 
    If this value is too high, the gyros can be biased away from what is truly stationary. 
    If this value is too low, the gyros will never adjust their bias, and you will see drift over time.
    
    angularVelocityDeltaThreshold(type: float): The acceptable amount of change in angular velocity between measurements before movement is assumed.
    If this value is too low, the device will never think it's at rest. 
    If it's too high, certain vibrations could affect your gyro biases (though the effects of these may also be limited by the Angular Velocity Threshold).
    
    accelerationThreshold(type: float): The maximum acceleration applied to the device (minus gravity) where it is assumed to be "at rest". This is also the maximum acceleration allowable before the device stops correcting to the acceleration vector.
    If this value is too high, your device can adjust to thinking “down” is the wrong direction, or be swayed by fast motions. 
    If this value is too low, the device may never think it is at rest to begin the process of correcting its pitch and roll.
    
    magTime(type: float): The time it will take to correct the heading 95% of the way to aligning with the compass (in seconds),up to 15 degrees of error. 
    Beyond 15 degrees, this is the time it will take for the bearing to move 45 degrees towards the compass reading. 
    Remember you can zero the algorithm at any time to instantly realign the spatial with acceleration and magnetic field vectors regardless of magnitude.
    By setting this value higher your device can become more (but never entirely) resistant to magnetic interference, at the expense of placing more weight on accurate gyroscope readings. 
    By setting this value lower, the device’s orientation will more quickly adjust to the magnetic field readings. 
    If this value is low enough, white noise in your compass readings will begin to show up in your measured heading.
    
    accelTime(type: float): The time it will take to correct the pitch and roll 95% of the way to aligning with the accelerometer (in seconds).
    By setting this value higher your device can become more resistant to acceleration affecting orientation, at the expense of placing more weight on accurate gyroscope readings. 
    By setting this value lower, the device’s orientation will more quickly adjust to the accelerometer readings (limited by the above Acceleration Threshold).
    
    biasTime(type: float): The time it will take to have the gyro biases settle to within 95% of the measured steady state (in seconds).
    The speed the gyros should be biased is a balance between getting a solid average and having the zeroing occur quickly enough that biases can be fully compensated for during short periods or rest.
    '''

    #AHRS_Parameters_List = [1.0, 0.1, 0.05, 10.0, 10.0, 1.25] #General Purpose
    #AHRS_Parameters_List = [0.001, 0.5, 2.0, 0.0, 0.0, 1.25] #No Gyro
    #AHRS_Parameters_List = [0.0, 0.0, 0.0, 1000.0, 1000.0, 1000.0] #AllGyro
    #AHRS_Parameters_List = [0.5, 0.1, 0.05, 120.0, 120.0, 1.25] #Zeroed
    #AHRS_Parameters_List = [50., 2.5, 0.2, 5.0, 20.0, 5.0] #High Vibrations
    AHRS_Parameters_List = [1.0, 0.1, 0.05, 0.1, 0.1, 0.1] #Reuben custom

    global AHRS_Parameters_angularVelocityThreshold
    AHRS_Parameters_angularVelocityThreshold = AHRS_Parameters_List[0]
    
    global AHRS_Parameters_angularVelocityDeltaThreshold
    AHRS_Parameters_angularVelocityDeltaThreshold = AHRS_Parameters_List[1]
    
    global AHRS_Parameters_accelerationThreshold
    AHRS_Parameters_accelerationThreshold = AHRS_Parameters_List[2]
    
    global AHRS_Parameters_magTime
    AHRS_Parameters_magTime = AHRS_Parameters_List[3]
    
    global AHRS_Parameters_accelTime
    AHRS_Parameters_accelTime = AHRS_Parameters_List[4]
    
    global AHRS_Parameters_biasTime
    AHRS_Parameters_biasTime = AHRS_Parameters_List[5]
    #################################################
    #################################################

    #################################################
    #################################################
    global EntryListWithBlinking_ReubenPython2and3ClassObject

    global EntryListWithBlinking_OPEN_FLAG
    EntryListWithBlinking_OPEN_FLAG = -1

    global EntryListWithBlinking_MostRecentDict
    EntryListWithBlinking_MostRecentDict = dict()

    global EntryListWithBlinking_MostRecentDict_DataUpdateNumber
    EntryListWithBlinking_MostRecentDict_DataUpdateNumber = 0

    global EntryListWithBlinking_MostRecentDict_DataUpdateNumber_last
    EntryListWithBlinking_MostRecentDict_DataUpdateNumber_last = -1

    EntryWidth = 10
    LabelWidth = 40
    FontSize = 8
    #################################################
    #################################################

    #################################################
    #################################################
    global MyPrint_ReubenPython2and3ClassObject

    global MyPrint_OPEN_FLAG
    MyPrint_OPEN_FLAG = -1
    #################################################
    #################################################

    #################################################
    #################################################
    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject

    global PLOTTER_OPEN_FLAG
    PLOTTER_OPEN_FLAG = -1

    global MyPlotterPureTkinter_MostRecentDict
    MyPlotterPureTkinter_MostRecentDict = dict()

    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag
    MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag = -1

    global LastTime_MainLoopThread_PLOTTER
    LastTime_MainLoopThread_PLOTTER = -11111.0
    #################################################
    #################################################

    #################################################  KEY GUI LINE
    #################################################
    if USE_GUI_FLAG == 1:
        print("Starting GUI thread...")
        GUI_Thread_ThreadingObject = threading.Thread(target=GUI_Thread)
        GUI_Thread_ThreadingObject.setDaemon(True) #Should mean that the GUI thread is destroyed automatically when the main thread is destroyed.
        GUI_Thread_ThreadingObject.start()
        time.sleep(0.5)  #Allow enough time for 'root' to be created that we can then pass it into other classes.
    else:
        root = None
        Tab_MainControls = None
        Tab_SpatialPrecision333 = None
        Tab_EntryListWithBlinking = None
        Tab_MyPrint = None
    #################################################
    #################################################

    #################################################
    #################################################
    global PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3ClassObject_GUIparametersDict
    PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3ClassObject_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_SpatialPrecision333_FLAG),
                                    ("root", Tab_SpatialPrecision333),
                                    ("EnableInternal_MyPrint_Flag", 1),
                                    ("NumberOfPrintLines", 10),
                                    ("UseBorderAroundThisGuiObjectFlag", 0),
                                    ("GUI_ROW", GUI_ROW_SpatialPrecision333),
                                    ("GUI_COLUMN", GUI_COLUMN_SpatialPrecision333),
                                    ("GUI_PADX", GUI_PADX_SpatialPrecision333),
                                    ("GUI_PADY", GUI_PADY_SpatialPrecision333),
                                    ("GUI_ROWSPAN", GUI_ROWSPAN_SpatialPrecision333),
                                    ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_SpatialPrecision333)])

    global PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3ClassObject_setup_dict
    PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3ClassObject_setup_dict = dict([("GUIparametersDict", PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3ClassObject_GUIparametersDict),
                                                                                        ("DesiredSerialNumber", -1), #-1 MEANS ANY SN, OR CHANGE THIS TO MATCH YOUR UNIQUE SERIAL NUMBER
                                                                                        ("WaitForAttached_TimeoutDuration_Milliseconds", 5000),
                                                                                        ("NameToDisplay_UserSet", "Reuben's Test SpatialPrecision333 Board"),
                                                                                        ("UsePhidgetsLoggingInternalToThisClassObjectFlag", 1),
                                                                                        ("SpatialAlgorithm", "IMU"), #IMU, AHRS, or None
                                                                                        ("RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegPerSec_UseMedianFilterFlag", 1),
                                                                                        ("RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegPerSec_UseExponentialSmoothingFilterFlag", 1),
                                                                                        ("RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegPerSec_ExponentialSmoothingFilterLambda", 0.98), #For lambda: new_filtered_value = lambda * raw_sensor_value + (1 - lambda) * old_filtered_value
                                                                                        ("PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegPerSec_UseMedianFilterFlag", 1),
                                                                                        ("PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegPerSec_UseExponentialSmoothingFilterFlag", 1),
                                                                                        ("PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegPerSec_ExponentialSmoothingFilterLambda", 0.98),
                                                                                        ("YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegPerSec_UseMedianFilterFlag", 1),
                                                                                        ("YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegPerSec_UseExponentialSmoothingFilterFlag", 1),
                                                                                        ("YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegPerSec_ExponentialSmoothingFilterLambda", 0.98),
                                                                                        ("Spatial_CallbackUpdateDeltaTmilliseconds", 2),
                                                                                        ("DataCollectionDurationInSecondsForSnapshottingAndZeroing", 2.0),
                                                                                        ("MainThread_TimeToSleepEachLoop", 0.001),
                                                                                        ("HeatingEnabledToStabilizeSensorTemperature", True),
                                                                                        ("ZeroGyrosAtStartOfProgramFlag", 0),
                                                                                        ("ZeroAlgorithmAtStartOfProgramFlag", 0),
                                                                                        ("AHRS_Parameters_angularVelocityThreshold", AHRS_Parameters_angularVelocityThreshold),
                                                                                        ("AHRS_Parameters_angularVelocityDeltaThreshold", AHRS_Parameters_angularVelocityDeltaThreshold),
                                                                                        ("AHRS_Parameters_accelerationThreshold", AHRS_Parameters_accelerationThreshold),
                                                                                        ("AHRS_Parameters_magTime", AHRS_Parameters_magTime),
                                                                                        ("AHRS_Parameters_accelTime", AHRS_Parameters_accelTime),
                                                                                        ("AHRS_Parameters_biasTime", AHRS_Parameters_biasTime)])

    if USE_SpatialPrecision333_FLAG == 1:
        try:
            PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3ClassObject = PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class(PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3ClassObject_setup_dict)
            SpatialPrecision333_OPEN_FLAG = PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions, 0)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    global EntryListWithBlinking_ReubenPython2and3ClassObject_GUIparametersDict
    EntryListWithBlinking_ReubenPython2and3ClassObject_GUIparametersDict = dict([("root", Tab_EntryListWithBlinking),
                                    ("UseBorderAroundThisGuiObjectFlag", 0),
                                    ("GUI_ROW", GUI_ROW_EntryListWithBlinking),
                                    ("GUI_COLUMN", GUI_COLUMN_EntryListWithBlinking),
                                    ("GUI_PADX", GUI_PADX_EntryListWithBlinking),
                                    ("GUI_PADY", GUI_PADY_EntryListWithBlinking),
                                    ("GUI_ROWSPAN", GUI_ROWSPAN_EntryListWithBlinking),
                                    ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_EntryListWithBlinking)])
    
    global EntryListWithBlinking_Variables_ListOfDicts
    EntryListWithBlinking_Variables_ListOfDicts = [dict([("Name", "AHRS_Parameters_angularVelocityThreshold"), ("Type", "float"), ("StartingVal", AHRS_Parameters_angularVelocityThreshold), ("EntryBlinkEnabled", 0), ("EntryWidth", EntryWidth),("LabelWidth", LabelWidth),("FontSize", FontSize)]),
                                                   dict([("Name", "AHRS_Parameters_angularVelocityDeltaThreshold"), ("Type", "float"), ("StartingVal", AHRS_Parameters_angularVelocityDeltaThreshold), ("EntryBlinkEnabled", 0), ("EntryWidth", EntryWidth),("LabelWidth", LabelWidth),("FontSize", FontSize)]),
                                                   dict([("Name", "AHRS_Parameters_accelerationThreshold"), ("Type", "float"), ("StartingVal", AHRS_Parameters_accelerationThreshold), ("EntryBlinkEnabled", 0),("EntryWidth", EntryWidth), ("LabelWidth", LabelWidth),("FontSize", FontSize)]),
                                                   dict([("Name", "AHRS_Parameters_magTime"), ("Type", "float"), ("StartingVal", AHRS_Parameters_magTime), ("EntryBlinkEnabled", 0),("EntryWidth", EntryWidth),("LabelWidth", LabelWidth), ("FontSize", FontSize)]),
                                                   dict([("Name", "AHRS_Parameters_accelTime"), ("Type", "float"), ("StartingVal", AHRS_Parameters_accelTime), ("EntryBlinkEnabled", 0),("EntryWidth", EntryWidth),("LabelWidth", LabelWidth), ("FontSize", FontSize)]),
                                                   dict([("Name", "AHRS_Parameters_biasTime"), ("Type", "float"), ("StartingVal", AHRS_Parameters_biasTime), ("EntryBlinkEnabled", 0),("EntryWidth", EntryWidth),("LabelWidth", LabelWidth), ("FontSize", FontSize)])]

    global EntryListWithBlinking_ReubenPython2and3ClassObject_setup_dict
    EntryListWithBlinking_ReubenPython2and3ClassObject_setup_dict = dict([("GUIparametersDict", EntryListWithBlinking_ReubenPython2and3ClassObject_GUIparametersDict),
                                                                          ("EntryListWithBlinking_Variables_ListOfDicts", EntryListWithBlinking_Variables_ListOfDicts),
                                                                          ("DebugByPrintingVariablesFlag", 0),
                                                                          ("LoseFocusIfMouseLeavesEntryFlag", 0)])
    if USE_EntryListWithBlinking_FLAG == 1:
        try:
            EntryListWithBlinking_ReubenPython2and3ClassObject = EntryListWithBlinking_ReubenPython2and3Class(EntryListWithBlinking_ReubenPython2and3ClassObject_setup_dict)
            EntryListWithBlinking_OPEN_FLAG = EntryListWithBlinking_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("EntryListWithBlinking_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions, 0)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MyPrint_FLAG == 1:

        MyPrint_ReubenPython2and3ClassObject_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_MyPrint_FLAG),
                                                                        ("root", Tab_MyPrint),
                                                                        ("UseBorderAroundThisGuiObjectFlag", 0),
                                                                        ("GUI_ROW", GUI_ROW_MyPrint),
                                                                        ("GUI_COLUMN", GUI_COLUMN_MyPrint),
                                                                        ("GUI_PADX", GUI_PADX_MyPrint),
                                                                        ("GUI_PADY", GUI_PADY_MyPrint),
                                                                        ("GUI_ROWSPAN", GUI_ROWSPAN_MyPrint),
                                                                        ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_MyPrint)])

        MyPrint_ReubenPython2and3ClassObject_setup_dict = dict([("NumberOfPrintLines", 10),
                                                                ("WidthOfPrintingLabel", 200),
                                                                ("PrintToConsoleFlag", 1),
                                                                ("LogFileNameFullPath", os.getcwd() + "//TestLog.txt"),
                                                                ("GUIparametersDict", MyPrint_ReubenPython2and3ClassObject_GUIparametersDict)])

        try:
            MyPrint_ReubenPython2and3ClassObject = MyPrint_ReubenPython2and3Class(MyPrint_ReubenPython2and3ClassObject_setup_dict)
            MyPrint_OPEN_FLAG = MyPrint_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPrint_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_GUIparametersDict
    MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_GUIparametersDict = dict([("EnableInternal_MyPrint_Flag", 1),
                                                                                                ("NumberOfPrintLines", 10),
                                                                                                ("UseBorderAroundThisGuiObjectFlag", 0),
                                                                                                ("GraphCanvasWidth", 890),
                                                                                                ("GraphCanvasHeight", 700),
                                                                                                ("GraphCanvasWindowStartingX", 0),
                                                                                                ("GraphCanvasWindowStartingY", 0),
                                                                                                ("GUI_RootAfterCallbackInterval_Milliseconds_IndependentOfParentRootGUIloopEvents", 20)])

    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_setup_dict
    MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_setup_dict = dict([("GUIparametersDict", MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_GUIparametersDict),
                                                                                        ("ParentPID", os.getpid()),
                                                                                        ("WatchdogTimerExpirationDurationSeconds_StandAlonePlottingProcess", 0.0),
                                                                                        ("MarkerSize", 3),
                                                                                        ("CurvesToPlotNamesAndColorsDictOfLists", dict([("NameList", ["Roll", "Pitch", "Yaw"]),("ColorList", ["Red", "Green", "Blue"])])),
                                                                                        ("NumberOfDataPointToPlot", 50),
                                                                                        ("XaxisNumberOfTickMarks", 10),
                                                                                        ("YaxisNumberOfTickMarks", 10),
                                                                                        ("XaxisNumberOfDecimalPlacesForLabels", 3),
                                                                                        ("YaxisNumberOfDecimalPlacesForLabels", 3),
                                                                                        ("XaxisAutoscaleFlag", 1),
                                                                                        ("YaxisAutoscaleFlag", 1),
                                                                                        ("X_min", 0.0),
                                                                                        ("X_max", 20.0),
                                                                                        ("Y_min", -0.0015),
                                                                                        ("Y_max", 0.0015),
                                                                                        ("XaxisDrawnAtBottomOfGraph", 0),
                                                                                        ("XaxisLabelString", "Time (sec)"),
                                                                                        ("YaxisLabelString", "Y-units (units)"),
                                                                                        ("ShowLegendFlag", 1)])

    if USE_PLOTTER_FLAG == 1:
        try:
            MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class(MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_setup_dict)
            PLOTTER_OPEN_FLAG = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject, exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_SpatialPrecision333_FLAG == 1 and SpatialPrecision333_OPEN_FLAG != 1:
        print("Failed to open PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class.")
        #ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_EntryListWithBlinking_FLAG == 1 and EntryListWithBlinking_OPEN_FLAG != 1:
        print("Failed to open EntryListWithBlinking_ReubenPython2and3Class.")
        #ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MyPrint_FLAG == 1 and MyPrint_OPEN_FLAG != 1:
        print("Failed to open MyPrint_ReubenPython2and3ClassObject.")
        #ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_PLOTTER_FLAG == 1 and PLOTTER_OPEN_FLAG != 1:
        print("Failed to open MyPlotterPureTkinterClass_Object.")
        #ExitProgram_Callback()
    #################################################
    #################################################

    ####################################################
    ####################################################
    ####################################################
    print("Starting main loop 'test_program_for_PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class.")
    StartingTime_MainLoopThread = getPreciseSecondsTimeStampString()

    while(EXIT_PROGRAM_FLAG == 0):

        ###################################################
        ####################################################
        CurrentTime_MainLoopThread = getPreciseSecondsTimeStampString() - StartingTime_MainLoopThread
        ###################################################
        ####################################################

        #################################################### GET's
        ####################################################
        if SpatialPrecision333_OPEN_FLAG == 1:

            SpatialPrecision333_MostRecentDict = PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3ClassObject.GetMostRecentDataDict()

            if "Time" in SpatialPrecision333_MostRecentDict:
                SpatialPrecision333_MostRecentDict_Quaternions_DirectFromDataEventHandler = SpatialPrecision333_MostRecentDict["Quaternions_DirectFromDataEventHandler"]
                SpatialPrecision333_MostRecentDict_RollPitchYaw_AbtXYZ_Dict = SpatialPrecision333_MostRecentDict["RollPitchYaw_AbtXYZ_Dict"]
                SpatialPrecision333_MostRecentDict_RollPitchYaw_Rate_AbtXYZ_Dict = SpatialPrecision333_MostRecentDict["RollPitchYaw_Rate_AbtXYZ_Dict"]
                SpatialPrecision333_MostRecentDict_DataStreamingFrequency_CalculatedFromMainThread = SpatialPrecision333_MostRecentDict["DataStreamingFrequency_CalculatedFromMainThread"]
                SpatialPrecision333_MostRecentDict_DataStreamingFrequency_TimestampFromPhidget_AlgorithmData_Quaternions = SpatialPrecision333_MostRecentDict["DataStreamingFrequency_TimestampFromPhidget_AlgorithmData_Quaternions"]
                SpatialPrecision333_MostRecentDict_Time = SpatialPrecision333_MostRecentDict["Time"]

                #print("SpatialPrecision333_MostRecentDict_Time: " + str(SpatialPrecision333_MostRecentDict_Time))
        ####################################################
        ####################################################

        ####################################################
        ####################################################

        ################################################### GET's
        if EntryListWithBlinking_OPEN_FLAG == 1:

            EntryListWithBlinking_MostRecentDict = EntryListWithBlinking_ReubenPython2and3ClassObject.GetMostRecentDataDict()

            if "DataUpdateNumber" in EntryListWithBlinking_MostRecentDict and EntryListWithBlinking_MostRecentDict["DataUpdateNumber"] != EntryListWithBlinking_MostRecentDict_DataUpdateNumber_last:
                EntryListWithBlinking_MostRecentDict_DataUpdateNumber = EntryListWithBlinking_MostRecentDict["DataUpdateNumber"]

                AHRS_Parameters_angularVelocityThreshold = EntryListWithBlinking_MostRecentDict["AHRS_Parameters_angularVelocityThreshold"]
                AHRS_Parameters_angularVelocityDeltaThreshold = EntryListWithBlinking_MostRecentDict["AHRS_Parameters_angularVelocityDeltaThreshold"]
                AHRS_Parameters_accelerationThreshold = EntryListWithBlinking_MostRecentDict["AHRS_Parameters_accelerationThreshold"]
                AHRS_Parameters_magTime = EntryListWithBlinking_MostRecentDict["AHRS_Parameters_magTime"]
                AHRS_Parameters_accelTime = EntryListWithBlinking_MostRecentDict["AHRS_Parameters_accelTime"]
                AHRS_Parameters_biasTime = EntryListWithBlinking_MostRecentDict["AHRS_Parameters_biasTime"]

                if SpatialPrecision333_OPEN_FLAG == 1:
                    PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3ClassObject.SetAHRSParameters_MyFunction(AHRS_Parameters_angularVelocityThreshold,
                                                                                                                          AHRS_Parameters_angularVelocityDeltaThreshold,
                                                                                                                          AHRS_Parameters_accelerationThreshold,
                                                                                                                          AHRS_Parameters_magTime,
                                                                                                                          AHRS_Parameters_accelTime,
                                                                                                                          AHRS_Parameters_biasTime)
                
                print("EntryListWithBlinking_MostRecentDict: " + str(EntryListWithBlinking_MostRecentDict))
                #print("DataUpdateNumber = " + str(EntryListWithBlinking_MostRecentDict_DataUpdateNumber) + ", EntryListWithBlinking_MostRecentDict: " + str(EntryListWithBlinking_MostRecentDict))
        ###################################################

        ###################################################
        EntryListWithBlinking_MostRecentDict_DataUpdateNumber_last = EntryListWithBlinking_MostRecentDict_DataUpdateNumber
        ###################################################

        ####################################################
        ####################################################

        ####################################################
        ####################################################
        if PLOTTER_OPEN_FLAG == 1:

            ####################################################
            MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.GetMostRecentDataDict()

            if "StandAlonePlottingProcess_ReadyForWritingFlag" in MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict:
                MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict["StandAlonePlottingProcess_ReadyForWritingFlag"]

                if MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag == 1:
                    if CurrentTime_MainLoopThread - LastTime_MainLoopThread_PLOTTER >= 0.030:
                        #print([SpatialPrecision333_MostRecentDict_Time]*3)
                        #print(SpatialPrecision333_MostRecentDict_RollPitchYaw_AbtXYZ_Dict["RollPitchYaw_AbtXYZ_List_Degrees"])
                        #MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExternalAddPointOrListOfPointsToPlot(["Roll", "Pitch", "Yaw"], [SpatialPrecision333_MostRecentDict_Time]*3, SpatialPrecision333_MostRecentDict_RollPitchYaw_AbtXYZ_Dict["RollPitchYaw_AbtXYZ_List_Degrees"])
                        #MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExternalAddPointOrListOfPointsToPlot(["Roll", "Pitch", "Yaw"], [SpatialPrecision333_MostRecentDict_Time]*3, SpatialPrecision333_MostRecentDict_RollPitchYaw_Rate_AbtXYZ_Dict["RollPitchYaw_Rate_AbtXYZ_List_DegreesPerSecond"])
                        MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExternalAddPointOrListOfPointsToPlot(["Pitch"], [SpatialPrecision333_MostRecentDict_Time]*1, [SpatialPrecision333_MostRecentDict_RollPitchYaw_AbtXYZ_Dict["RollPitchYaw_AbtXYZ_List_Degrees"][1]])


                        LastTime_MainLoopThread_PLOTTER = CurrentTime_MainLoopThread
            ####################################################

        ####################################################
        ####################################################

        ####################################################
        ####################################################
        UpdateFrequencyCalculation()
        time.sleep(0.001)
        ####################################################
        ####################################################

    ####################################################
    ####################################################
    ####################################################

    ################################################# THIS IS THE EXIT ROUTINE!
    #################################################
    print("Exiting main program 'test_program_for_PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class.")

    #################################################
    if SpatialPrecision333_OPEN_FLAG == 1:
        PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    if EntryListWithBlinking_OPEN_FLAG == 1:
        EntryListWithBlinking_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    if MyPrint_OPEN_FLAG == 1:
        MyPrint_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    if PLOTTER_OPEN_FLAG == 1:
        MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    #################################################

##########################################################################################################
##########################################################################################################