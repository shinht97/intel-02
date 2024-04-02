#!/usr/bin/env python3

import os
import threading
from argparse import ArgumentParser
from queue import Empty, Queue
from time import sleep

import cv2
import numpy as np
#from openvino.inference_engine import IECore
from iotdemo import FactoryController

global FORCE_STOP

FORCE_STOP = False

parser = ArgumentParser(add_help=False)
parser.add_argument("-d", "--device")
parser = ArgumentParser(prog='python3 factory.py',
                            description="Factory tool")

parser.add_argument("-d",
                    "--device",
                    default=None,
                    type=str,
                    help="Arduino port")

args = parser.parse_args()        

with FactoryController(args.device) as ctrl:
    while not FORCE_STOP:
        key = input()
        intkey = int(key)
        ardu_dictionary = {
            '1' : 'ctrl.system_start()',
            '2' : 'ctrl.system_stop()',
            '3' : 'ctrl.red',
            '4' : 'ctrl.green',
            '5' : 'ctrl.orange',
            '6' : 'ctrl.conveyor',
            '7' : 'ctrl.push_actuator(1)',
            '8' : 'ctrl.push_actuator(2)',
            '0' : 'ctrl.close()'
            }
        
        if key == '0':
            print(f"{ardu_dictionary[key]}")
            exec(f'{ardu_dictionary[key]}')
        if key == '3':
            print(f"{ardu_dictionary[key]}=False")
            exec(f'{ardu_dictionary[key]}=False')
        if key == '4':
            print(f"{ardu_dictionary[key]}=False")
            exec(f'{ardu_dictionary[key]}=False')        
        if key == '5':
            print(f"{ardu_dictionary[key]}=False")
            exec(f'{ardu_dictionary[key]}=False')        

            
            