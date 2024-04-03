#!/usr/bin/env python3

import os
import threading
from argparse import ArgumentParser
from queue import Empty, Queue
from time import sleep

import cv2
import numpy as np
# from openvino.inference_engine import IECore

from iotdemo import FactoryController

FORCE_STOP = False


def thread_cam1(qMotion:Queue) -> None:
    # TODO: MotionDetector

    # TODO: Load and initialize OpenVINO

    # TODO: HW2 Open video clip resources/conveyor.mp4 instead of camera device.
    cap = cv2.VideoCapture("./resources/conveyor.mp4")
    
    while not FORCE_STOP:
        sleep(0.03)
        _, frame = cap.read()
        if frame is None:
            break

        # TODO: HW2 Enqueue "VIDEO:Cam1 live", frame info
        qMotion.put( ("VIDEO:Cam1 live", frame) )
        # TODO: Motion detect

        # TODO: Enqueue "VIDEO:Cam1 detected", detected info.
        # qMotion.put( ("VIDEO:Cam1 detected", detected) )
        
        # abnormal detect
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # reshaped = detected[:, :, [2, 1, 0]]
        # np_data = np.moveaxis(reshaped, -1, 0)
        # preprocessed_numpy = [((np_data / 255.0) - 0.5) * 2]
        # batch_tensor = np.stack(preprocessed_numpy, axis=0)

        # TODO: Inference OpenVINO

        # TODO: Calculate ratios
        # print(f"X = {x_ratio:.2f}%, Circle = {circle_ratio:.2f}%")

        # TODO: in queue for moving the actuator 1

    cap.release()
    qMotion.put(('DONE', None))
    exit()
    

def thread_cam2(qColor:Queue) -> None:
    # TODO: MotionDetector

    # TODO: ColorDetector

    # TODO: HW2 Open "resources/conveyor.mp4" video clip
    
    cap = cv2.VideoCapture("./resources/conveyor.mp4")

    while not FORCE_STOP:
        sleep(0.03)
        _, frame = cap.read()
        if frame is None:
            break

        # TODO: HW2 Enqueue "VIDEO:Cam2 live", frame info
        qColor.put( ("VIDEO:Cam2 live", frame) )
        # TODO: Detect motion

        # TODO: Enqueue "VIDEO:Cam2 detected", detected info.
        # qColor.put( ("VIDEO:Cam2 detected", detected) )
        # TODO: Detect color

        # TODO: Compute ratio
        # print(f"{name}: {ratio:.2f}%")

        # TODO: Enqueue to handle actuator 2

    cap.release()
    qColor.put(('DONE', None))
    exit()


def imshow(title, frame, pos=None):
    cv2.namedWindow(title)
    if pos:
        cv2.moveWindow(title, pos[0], pos[1])
    cv2.imshow(title, frame)


def main():
    global FORCE_STOP
    
    FORCE_STOP = False

    parser = ArgumentParser(prog='python3 factory.py',
                            description="Factory tool")

    parser.add_argument("-d",
                        "--device",
                        default=None,
                        type=str,
                        help="Arduino port")
    
    args = parser.parse_args()

    # TODO: HW2 Create a Queue
    q = Queue()
    # TODO: HW2 Create thread_cam1 and thread_cam2 threads and start them.

    Motion = threading.Thread(target=thread_cam1, args=(q, ))
    Color = threading.Thread(target=thread_cam2, args=(q, ))
    
    Motion.start()
    Color.start()
    
    with FactoryController(args.device) as ctrl:
        while not FORCE_STOP:
            if cv2.waitKey(10) & 0xff == ord('q'):
                break
                        
            # TODO: HW2 get an item from the queue. You might need to properly handle exceptions.
            
            try:
                data = q.get_nowait()
            except Empty:
                continue
            
            # de-queue name and data
            
            name, value = data
            
            # TODO: HW2 show videos with titles of 'Cam1 live' and 'Cam2 live' respectively.
            
            if "live" in name:
                imshow(name[-9:], value)

            # TODO: Control actuator, name == 'PUSH'

            elif name == "PUSH":
                pass            
            
            elif name == 'DONE':
                FORCE_STOP = True

            q.task_done()

    Motion.join()
    Color.join()

    cv2.destroyAllWindows()


if __name__ == '__main__':
    try:
        main()
    except Exception:
        os._exit(0)
