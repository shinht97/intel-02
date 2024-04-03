#!/usr/bin/env python3

import os
import threading
from argparse import ArgumentParser
from queue import Empty, Queue
from time import sleep
import keyboard

import cv2
import numpy as np
# from openvino.inference_engine import IECore

# from iotdemo import FactoryController

FORCE_STOP = False


def thread_cam1(q:Queue)->None:
    # TODO: MotionDetector

    # TODO: Load and initialize OpenVINO

    # TODO: HW2 Open video clip resources/conveyor.mp4 instead of camera device.
    #video_path = './videos/미친듯한 운과 실력 미국은 어떻게 최강대국이 되었나.mp4'
    video_path = 'resources/conveyor.mp4'
    cap = cv2.VideoCapture(video_path)

# 비디오 캡처 객체가 올바르게 초기화되었는지 확인
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()

  
    while not FORCE_STOP:
        sleep(0.03)
        _, frame = cap.read()
        if frame is None:
            break

        # TODO: HW2 Enqueue "VIDEO:Cam1 live", frame info
        q.put(("video1", frame))

        # TODO: Motion detect

        # TODO: Enqueue "VIDEO:Cam1 detected", detected info.

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
    q.put(('DONE', None))
    


def thread_cam2(q:Queue)->None:
     
    # TODO: MotionDetector

    # TODO: ColorDetector

    # TODO: HW2 Open "resources/conveyor.mp4" video clip

    video_path = 'resources/conveyor.mp4'

    cap = cv2.VideoCapture(video_path)

    # 비디오 캡처 객체가 올바르게 초기화되었는지 확인
    if not cap.isOpened():

        print("Error: Could not open video.")
        exit()

    
    while not FORCE_STOP:
        sleep(0.03)
        _, frame = cap.read()
        if frame is None:
            break
        
        # TODO: HW2 Enqueue "VIDEO:Cam2 live", frame info
        q.put(("video2", frame))

        # TODO: Detect motion

        # TODO: Enqueue "VIDEO:Cam2 detected", detected info.

        # TODO: Detect color

        # TODO: Compute ratio
        # print(f"{name}: {ratio:.2f}%")

        # TODO: Enqueue to handle actuator 2

    q.put(('DONE', None))
    cap.release()


def imshow(title, frame, pos=None):
    cv2.namedWindow(title)
    if pos:
        cv2.moveWindow(title, pos[0], pos[1])
    cv2.imshow(title, frame)
    







def main():
    global FORCE_STOP



    parser = ArgumentParser(prog='python3 factory.py',
                            description="Factory tool")

    parser.add_argument("-d",
                        "--device",
                        default=None,
                        type=str,
                        help="Arduino port")
    args = parser.parse_args()

    # TODO: HW2 Create a Queue

    # TODO: HW2 Create thread_cam1 and thread_cam2 threads and start them.

    q = Queue() 

    t1 = threading.Thread(target=thread_cam1,args=(q,))
    t2 = threading.Thread(target=thread_cam2,args=(q,))
    
    t1.start()
    t2.start()
    

    while not FORCE_STOP:
        
            # TODO: HW2 get an item from the queue. You might need to properly handle exceptions.
            # de-queue name and data
            # TODO: HW2 show videos with titles of 'Cam1 live' and 'Cam2 live' respectively.
            # TODO: Control actuator, name == 'PUSH'
            
        try:
            data = q.get_nowait()
        except Empty:
            continue
        # if name == 'DONE':
        #     FORCE_STOP = True
        name, value = data  
        result=imshow(name, value)
        if cv2.waitKey(5) == ord('q'):
            FORCE_STOP =True
        

        q.task_done()

    t1.join(timeout=1)
    t2.join(timeout=1)
    
    cv2.destroyAllWindows()


if __name__ == '__main__':
    try:
        main()
    except Exception:
        os._exit()
