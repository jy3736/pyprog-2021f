# --- 前進 ---
def forward(spd=150):
    return setWheels(spd, spd)

# --- 旋轉(左) ---
def rotateR(spd=50):
    return setWheels(spd, 0)

# --- 旋轉(右) ---
def rotateL(spd=50):
    return setWheels(0, spd)

# --- 停止 ---
def stop():
    # 填入你的程式答案

# --- 原地旋轉(左/右) ---
# spd =  -255 ~ 255
def rotate(spd=50):
    # 填入你的程式答案

# --- 靠(左/右)前進 ---
def forwardBL(spd=150, bias=0.1):
    # 填入你的程式答案

# --- 走迷宮演算法 ---
def algorithm():
    global car
    if car.status != "GAME_ALIVE":
        return "RESET"
    if car.F_sensor<15:
        if car.L_sensor>car.R_sensor:
            return rotateL()
        else:
            return rotateR()
    return forward(255)

#----------------------------------------------------------
# 請不要修改以下程式，除非你知道你在做什麼!
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