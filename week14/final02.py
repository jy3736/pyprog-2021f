# --- 前進/停止/後退 ---
def moving(spd=150):
    '''
    前進 : spd = 1 ~ 255
    後退 : spd = -1 ~ -255
    停止 : spd = 0
    '''
    # 填入你的程式答案

# --- 原地旋轉(左/右) ---
def rotate(spd=50):
    '''
    原地旋轉(左) : spd = 1 ~ 255
    原地旋轉(右) : spd = -1 ~ -255
    停止 : spd = 0
    '''
    # 填入你的程式答案

# --- 左右輪差轉彎(左/右) ---
def turn(spd=50, diff=0.5):
    '''
    輪差轉彎(左) : spd = 1 ~ 255
    輪差轉彎(右) : spd = -1 ~ -255
    左右輪差比例 : diff = 0.0 ~ 1.0
    停止 : spd = 0
    '''
    # 填入你的程式答案

# 使用上面3個通用型函數，重新實現期末考題 1 中所有自走車移動控制函數。

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