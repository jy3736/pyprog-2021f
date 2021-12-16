import os, pickle

ROOT = os.path.dirname(__file__)
ROOT = '.' if (ROOT=='') else ROOT

MF = f"{ROOT}\\model.pickle"
print(f"\nLoading model file... {MF}\n")

with open(MF, 'rb') as f:
    model = pickle.load(f)

def algorithm():
    global car, model
    if car.status != "GAME_ALIVE":
        return "RESET"
    sensors = [[car.L_sensor, car.L_T_sensor, car.F_sensor, car.R_T_sensor, car.R_sensor]]
    l, r = model.predict(sensors)[0]                
    return setWheels(l,r)
        
#----------------------------------------------------------
# Please do not modify any of the following codes 
#----------------------------------------------------------
class D2O(object):    
    def __init__(self, my_dict): 
        for key in my_dict:
            setattr(self, key, my_dict[key])

def setWheels(l,r):
    return [{'left_PWM':l, 'right_PWM':r},]

class MLPlay:
    def __init__(self, player):
        pass

    def update(self, scene_info):
        global car
        car = D2O(scene_info)
        return algorithm()
 
    def reset(self):
        print("Game Reset!")
