def forward(spd=150):
    return setWheels(spd, spd)

def rotateR(spd=30):
    return setWheels(spd, -spd)

def rotateL(spd=30):
    return setWheels(-spd, spd)

def algorithm():
    global car
    if car.status != "GAME_ALIVE":
        return "RESET"
    if KB==0:
        return forward(0)
    elif KB==1:
        return forward(100)
    elif KB==2:
        return forward(-100)
    elif KB==3:
        return rotateL()
    elif KB==4:
        return rotateR()
    return forward(0)
        
#----------------------------------------------------------
# Please do not modify any of the following codes 
#----------------------------------------------------------
from pynput import keyboard
 
KB = 0

def on_press(k):
    global KB
    if k == keyboard.Key.up:
        KB = 1
    elif k == keyboard.Key.down:
        KB = 2
    elif k == keyboard.Key.left:
        KB = 3
    elif k == keyboard.Key.right:
        KB = 4    
    elif k == keyboard.Key.shift_l:
        KB = 5    
    elif k == keyboard.Key.ctrl_l:
        KB = 6    

def on_release(k):
    global KB, car
    if KB == 5:
        carInfo()
    KB = 0

listener = keyboard.Listener(on_press=on_press,on_release=on_release)
listener.start()

print(f"   自走車位置   角度    左  左前    前  右前    右")
print("-"*50)

def carInfo():
    print(f"({car.x:5.1f}, {car.y:5.1f})",end=' ')
    print(f"{car.angle:5.1f}",end=' ')
    print(f"{car.L_sensor:5.1f}",end=' ')
    print(f"{car.L_T_sensor:5.1f}",end=' ')
    print(f"{car.F_sensor:5.1f}",end=' ')
    print(f"{car.R_T_sensor:5.1f}",end=' ')
    print(f"{car.R_sensor:5.1f}")

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
