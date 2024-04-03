#!/usr/bin/env python3

import os
import threading
from argparse import ArgumentParser
from queue import Empty, Queue
from time import sleep

import cv2
import numpy as np
import openvino as ov
# from openvino.inference_engine import IECore

from iotdemo import FactoryController, MotionDetector, ColorDetector

FORCE_STOP = False


def thread_cam1(q:Queue)->None:
    # TODO: MotionDetector
    motion_detect = MotionDetector()
    motion_detect.load_preset(path="/home/ubuntu17/workdir/smart-factory/resources/motion.cfg")

    # TODO: Load and initialize OpenVINO
    core = ov.Core()
    model = core.read_model(model='/home/ubuntu17/workdir/smart-factory/resources/model.xml')
    compiled_model = core.compile_model(model=model, device_name='CPU')
    input_layer = compiled_model.input(0)
    output_layer = compiled_model.output(0)
    # TODO: HW2 Open video clip resources/conveyor.mp4 instead of camera device.
    file_path = './resources/conveyor.mp4'
    cap = cv2.VideoCapture(file_path)
    while not FORCE_STOP:
        sleep(0.03)
        ret, frame = cap.read()
        if not ret:
            print("cam1 ret Error")
            break

        # TODO: HW2 Enqueue "VIDEO:Cam1 live", frame info
        q.put(("VIDEO:Cam1 Live", frame))
        # TODO: Motion detect
        detected_frame = motion_detect.detect(frame)
        if detected_frame is None:
            continue


        # TODO: Enqueue "VIDEO:Cam1 detected", detected info.
        q.put(("VIDEO:Cam1 Detected", detected_frame))
        detected_frame = cv2.cvtColor(detected_frame, cv2.COLOR_BGR2RGB)
        #detected_frame = np.expand_dims(detected_frame, 0)
                
        input_image = np.expand_dims(detected_frame.transpose(2, 0, 1), 0)

        # abnormal detect
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # reshaped = detected[:, :, [2, 1, 0]]
        # np_data = np.moveaxis(reshaped, -1, 0)
        # preprocessed_numpy = [((np_data / 255.0) - 0.5) * 2]
        # batch_tensor = np.stack(preprocessed_numpy, axis=0)

        # TODO: Inference OpenVINO
        predict = compiled_model(input_image)[output_layer]
        x_ratio, circle_ratio = predict[0]
        # TODO: Calculate ratios
        # print(f"X = {x_ratio:.2f}%, Circle = {circle_ratio:.2f}%")
        print(f"X = {x_ratio*100:.2f}, Circle = {circle_ratio*100:.2f}*")
        # TODO: in queue for moving the actuator 1
        if x_ratio > circle_ratio:
            q.put(("PUSH", 1))
        
    cap.release()
    q.put(('DONE', None))
    exit()


def thread_cam2(q:Queue)->None:
    # TODO: MotionDetector
    motion_detect = MotionDetector()
    motion_detect.load_preset(path="/home/ubuntu17/workdir/smart-factory/resources/motion.cfg")

    # TODO: ColorDetector
    color_detect = ColorDetector()
    color_detect.load_preset(path="/home/ubuntu17/workdir/smart-factory/resources/color.cfg")
    # TODO: HW2 Open "resources/conveyor.mp4" video clip
    file_path = '/home/ubuntu17/workdir/smart-factory/resources/conveyor.mp4'
    cap = cv2.VideoCapture(file_path)
    while not FORCE_STOP:
        sleep(0.03)
        ret, frame = cap.read()
        if not ret:
            print("cam2 ret error")

        # TODO: HW2 Enqueue "VIDEO:Cam2 live", frame info
        q.put(("VIDEO:Cam2 Live", frame))
        # TODO: Detect motion
        detected_frame = motion_detect.detect(frame)
        if detected_frame is None:
            continue

        # TODO: Enqueue "VIDEO:Cam2 detected", detected info.
        q.put(("VIDEO:Cam2 detected", detected_frame))
        # TODO: Detect color
        predict = color_detect.detect(detected_frame)
        name, ratio = predict[0]
        # TODO: Compute ratio
        print(f"{name}: {ratio*100:.2f}%")

        # TODO: Enqueue to handle actuator 2
        if name == 'blue':
            q.put(("PUSH, 2"))
    cap.release()
    q.put(('DONE', None))
    exit()


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
    frame_queue = Queue()
    # TODO: HW2 Create thread_cam1 and thread_cam2 threads and start them.
    t1 = threading.Thread(target=thread_cam1, args=(frame_queue,))
    t2 = threading.Thread(target=thread_cam2, args=(frame_queue,)) 
    t1.start()
    t2.start()
    with FactoryController(args.device) as ctrl:
        while not FORCE_STOP:
            
            if cv2.waitKey(10) & 0xff == ord('q'):
                break

            # TODO: HW2 get an item from the queue. You might need to properly handle exceptions.
            # de-queue name and data
            try:
                data = frame_queue.get_nowait()
            except Empty:
                continue
            cam_id, frame = data
 
   

            # TODO: HW2 show videos with titles of 'Cam1 live' and 'Cam2 live' respectively.
            if cam_id[11:] == "Live":
                imshow(cam_id[6:], frame)

            # TODO: Control actuator, name == 'PUSH'
            elif cam_id == "PUSH":
                ctrl.push_actuator(frame)
            #name = f'Cam{cam_id} Live'
            elif cam_id == 'DONE':
                FORCE_STOP = True

            frame_queue.task_done()
    
    t1.join()
    t2.join()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    try:
        main()
    except Exception:
        os._exit()
