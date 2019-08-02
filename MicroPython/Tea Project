#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase


holder = Motor(Port.A)

touch2 = TouchSensor(Port.S2)
touch3 = TouchSensor(Port.S3)

list = [x for x in range(0,500)]

def tea(): #function to lower/raise teabag for 7ms multiplied by max of list
    if touch2.pressed():
        for x in list:
            if touch3.pressed():
                break
            if x%2==0:
                holder.run(-200)
                wait(700)
                holder.stop()
            if x%2 !=0:
                holder.run(200)
                wait(700)
                holder.stop()  
          
                    
while True:
    tea()
    
          
