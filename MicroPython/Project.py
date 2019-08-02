#!/usr/bin/env pybricks-micropython

#This project is to drive around a robot

#Note There was only 2 TouchSensors/buttons 

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from threading import Thread

left = Motor(Port.B)
right = Motor(Port.C)
robot = DriveBase(left, right, 56, 114)

sensorU = UltrasonicSensor(Port.S1)
sensorD = UltrasonicSensor(Port.S4)

touch2 = TouchSensor(Port.S2)
touch3 = TouchSensor(Port.S3)



def func1(): #commands to drive left/right/forward and to stop given obstruction or drop (e.g. a cliff or step)
    while touch3.pressed() and touch2.pressed():       
        if sensorU.distance() < 50:
            robot.stop()
            brick.sound.file(SoundFile.ERROR, 90)
            break
        if sensorD.distance() > 150:
            robot.stop()
            brick.sound.file(SoundFile.ERROR, 90)
            break
        robot.drive(100,0)    
    while touch2.pressed() and touch3.pressed()==0:
        if sensorU.distance() < 50:
            robot.stop()
            brick.sound.file(SoundFile.ERROR, 90)
            break
        if sensorD.distance() > 150:
            robot.stop()
            brick.sound.file(SoundFile.ERROR, 90)
            break
        left.run(100)          
    while touch3.pressed() and touch2.pressed()==0:
        if sensorU.distance() < 50:
            robot.stop()
            brick.sound.file(SoundFile.ERROR, 90)
            break
        if sensorD.distance() > 150:
            robot.stop()
            brick.sound.file(SoundFile.ERROR, 90)
            break
        right.run(100)       
    robot.stop()


def func2():               
    if sensorU.distance() < 50 or sensorD.distance() > 150: #robot will reverse if stop condition of func1 was met
        while touch3.pressed() and touch2.pressed():
            robot.drive(-100,0) 
    else:
        func1()



while True:
    func2()
