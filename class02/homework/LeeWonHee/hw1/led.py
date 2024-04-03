#!/usr/bin/env python3
import os
import threading
from argparse import ArgumentParser
from queue import Empty, Queue
from time import sleep

import cv2
import numpy as np
from openvino.inference_engine import IECore
from iotdemo import FactoryController

global FORCE_STOP

FORCE_STOP = False

parser = ArgumentParser(add_help=False)
parser.add_argument("-d",
                    "--device",
                    default=None,
                    type=str,
                    help="Arduino port")
args = parser.parse_args()
#queue = Queue()

with FactoryController(args.device) as ctrl:
    while not FORCE_STOP:
        #ctrl.system_start()
        key = input()
        intkey = int(key)
        ardu_dictionary = {
            '1':'ctrl.system_start()', 
            '2':'ctrl.system_stop()',
            '3':'ctrl.red',
            '4':'ctrl.green', 
            '5':'ctrl.orange', 
            '6':'ctrl.conveyor',
            '7':'ctrl.push_actuator(1)', 
            '8':'ctrl.push_actuator(2)',
            '0':'ctrl.close()'}
        
        if key is '0':
            print(f'{ardu_dictionary[key]}')
            exec(f'{ardu_dictionary[key]}')           

        for ii in range (1, 9):
            iistr = str(ii)
        
        if intkey > 0 and intkey < 3:
            for ii in range(1,3):
                iistr = str(ii)
                if key == iistr:
                    print(f'{ardu_dictionary[iistr]}')
                    exec(f'{ardu_dictionary[iistr]}')
        elif intkey > 2 and intkey < 7:
            for ii in range(3,7):
                iistr = str(ii)
                if key == iistr:
                    print(f'{ardu_dictionary[iistr]}=True')
                    exec(f'{ardu_dictionary[iistr]}=False')
                else:
                    print(f'{ardu_dictionary[iistr]}=False')
                    exec(f'{ardu_dictionary[iistr]}=True')
        elif intkey > 6 and intkey < 9:
            for ii in range(7,9):
                iistr = str(ii)
                if key == iistr:
                    print(f'{ardu_dictionary[iistr]}')
                    exec(f'{ardu_dictionary[iistr]}')