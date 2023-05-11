###########################

PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class

Wrapper (including ability to hook to Tkinter GUI) to read spatial data from 3-axis accelerometer, 3-axis gyro, and 3-axis magnetometer.
Outputs the sensor's orientation (calculated via IMU or AHRS algorithm) in quaternions and Euler angles, as well as the raw sensor data.

#####
From Phidgets' website:
"This spatial board has a 3-axis accelerometer, gyroscope and compass with high resolution readings at low magnitudes.
The PhidgetSpatial Precision 3/3/3 combines the functionality of a 3-axis compass, a 3-axis gyroscope,
and a 3-axis accelerometer all in one convenient package. You can use the Spatial channel to use all three sensors with
the AHRS or IMU algorithms to get motion data in quaternions for accurate spatial tracking. Or, you can use the data
from each of these sensors separately to measure tilt, vibration or rotation of an object. This PhidgetSpatial also
features a temperature stabilization circuit to warm the sensors to a constant 50°C to minimize temperature effects.
Features:

    3-axis accelerometer (+/-16g),
    3-axis gyroscope (+/-2000deg/s),
    3-axis magnetometer (+/-8G),
    Accurate timestamp for plotting or advanced calculations,
    Built-in support for AHRS and IMU algorithms,
    Built-in heater for temperature stabilization up to 50degC,
    Versatile connection via USB or VINT"

PhidgetSpatial Precision 3/3/3
ID: MOT0110_0
https://www.phidgets.com/?tier=3&catid=10&pcid=8&prodid=1205
#####

#####
Code also supports older/discontinued models ID: MOT0109_0 and ID: 1044_1B.
#####

Reuben Brewer, Ph.D.

reuben.brewer@gmail.com

www.reubotics.com

Apache 2 License

Software Revision G, 05/10/2023

Verified working on: 
Python 2.7, 3.8.
Windows 8.1, 10 64-bit
Raspberry Pi Buster 
(does not work on Mac)

*NOTE THAT YOU MUST INSTALL BOTH THE Phidget22 LIBRARY AS WELL AS THE PYTHON MODULE.*

###########################

########################### Python module installation instructions, all OS's

PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class, ListOfModuleDependencies: ['future.builtins', 'LowPassFilter_ReubenPython2and3Class', 'numpy', 'Phidget22', 'scipy.spatial.transform', 'ZeroAndSnapshotData_ReubenPython2and3Class']
PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class, ListOfModuleDependencies_TestProgram: ['MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class', 'MyPrint_ReubenPython2and3Class']
PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class, ListOfModuleDependencies_NestedLayers: ['EntryListWithBlinking_ReubenPython2and3Class', 'future.builtins', 'LowPassFilter_ReubenPython2and3Class', 'numpy', 'pexpect', 'psutil']
PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class, ListOfModuleDependencies_All:['EntryListWithBlinking_ReubenPython2and3Class', 'future.builtins', 'LowPassFilter_ReubenPython2and3Class', 'MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class', 'MyPrint_ReubenPython2and3Class', 'numpy', 'pexpect', 'Phidget22', 'psutil', 'scipy.spatial.transform', 'ZeroAndSnapshotData_ReubenPython2and3Class']

https://pypi.org/project/Phidget22/#files

To install the Python module using pip:
pip install Phidget22       (with "sudo" if on Linux/Raspberry Pi)

To install the Python module from the downloaded .tar.gz file, enter downloaded folder and type "python setup.py install"

###########################

########################### Library/driver installation instructions, Windows

https://www.phidgets.com/docs/OS_-_Windows

###########################

########################### Library/driver installation instructions, Linux (other than Raspberry Pi)

https://www.phidgets.com/docs/OS_-_Linux#Quick_Downloads

###########################

########################### Library/driver installation instructions, Raspberry Pi (models 2 and above)

https://www.phidgets.com/education/learn/getting-started-kit-tutorial/install-libraries/

curl -fsSL https://www.phidgets.com/downloads/setup_linux | sudo -E bash -
sudo apt-get install -y libphidget22
 
###########################