#!/usr/bin/env python3

import os
import threading
from argparse import ArgumentParser
from queue import Empty, Queue
from time import sleep

import cv2
import numpy as np


from iotdemo import FactoryController

FORCE_STOP = False

parser = ArgumentParser(prog='python3 factory.py',
                        description="Factory tool")

parser.add_argument("-d",
                    "--device",
                    default=None,
                    type=str,
                    help="Arduino port")
args = parser.parse_args()

red_count=1
orange_count=1
green_count=1
conveyor_count=1

with FactoryController(args.device) as ctrl:
    
    while not FORCE_STOP:
            key= input()             
            
            if key == '3':
                red_count +=1
                if red_count %2 == 0:
                    ctrl.red =True
                else :
                    ctrl.red = False
            if key == '4':
                orange_count +=1
                if orange_count %2 == 0:
                    ctrl.orange =True
                else :
                    ctrl.orange = False
            if key == '5':
                green_count +=1
                if green_count %2 == 0:
                    ctrl.green =True
                else :
                    ctrl.green = False
            if key == '6':
                conveyor_count +=1
                if conveyor_count %2 == 0:
                    ctrl.conveyor =True
                else :
                    ctrl.conveyor = False
            if key == '7':
                    ctrl.push_actuator1 =1

            if key == '8':
                    ctrl.push_actuator1 =2

            if key == 'q':
                FORCE_STOP = True

