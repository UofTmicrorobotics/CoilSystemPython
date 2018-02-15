# CoilSystemPython

A Python3-based program for the coil system

## Usage

open terminal and cd to the target directory

python3 main.py

## Program Structure
To have a better understanding of the program, I would recommend you first have a look at "fieldManager.py".

After that, open the GUI and "callbacks.py" to follow the signal flow and event handler (pyqtSlot).

Go through "vision.py" to see how images are processed, and "objectDetection.py" to see how objects are detected and stored in instances of Agent class.

Read "subthread.py" in the end because it uses all the above-mentioned classes to do some complex stuff. E.g. Apply a rotational field with time-varying frequency/magnitude based on the position of the object detected.
	
```
main.py

callbacks.py
│
│   
└───syntax.py [highlight the keywords in GUI editor_vision]
|
└───fieldManager.py [send commands to s826; store XYZ field strength]
│   	|   s826.py [control s826 I/O]
│  
│
└───visoin.py [capture frames; apply filters; detect objects]
│       │   filterlib.py [define filters]
│       │   objectDetection.py [define object detection algorithms]
│
│
└───subthread.py [run multithreading tasks]

```
## Dependencies

1. opencv

pip3 install opencv-python

pip3 install opencv-contrib-python

2. pyqt5

pip3 install pyqt5

3. pydc1394

https://github.com/jordens/pydc1394

## GUI Designer

qt-designer is used.

sudo apt-get install qt4-designer

## USB camera or Firewire Camera

Can specify the camera in vision.py
