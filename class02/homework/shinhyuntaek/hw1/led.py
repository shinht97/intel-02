import os
from argparse import ArgumentParser
from time import sleep

from iotdemo import FactoryController

FORCE_STOP = False

def main():
    global FORCE_STOP
    
    FORCE_STOP = False
    
    on_list = ["3"]
    
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
            ardu_diction = {
                '1' : "ctrl.system_start()",
                '2' : "ctrl.system_stop()",
                '3' : "ctrl.red",
                '4' : "ctrl.orange",
                '5' : "ctrl.green",
                '6' : "ctrl.conveyor",
                '7' : "ctrl.push_actuator(1)",
                '8' : "ctrl.push_actuator(2)",
                '0' : 'ctril.close()'
            }
            
            if key in [str(i) for i in range(0, 9)]:
                print(f"{ardu_diction[key]}")

                if key in ["3", "4", "5"]: 
                    exec(f"{ardu_diction[key]} = {key in on_list}")
                    
                    if key in on_list:
                        on_list.remove(key)
                    else:
                        on_list.append(key)
                        
                elif key in ["7", "8"]:
                    exec(f"{ardu_diction[key]}")


    
if __name__ == "__main__":
    main()