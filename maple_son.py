import pyautogui as pag
import time
from threading import Thread
import keyboard
import random

def coord():
    XY = []
    x,y = pag.position()
    XY.append(x)
    XY.append(y)
    print(XY)
    return XY

def click(coord):
    #pag.moveTo(x=coord[0], y=coord[1], duration=0.1)
    pag.doubleClick(x=coord[0], y=coord[1])
    time.sleep(random.uniform(0.1, 0.11))
    return

XY = []

pauseVal = False;

def stop():
    global pauseVal
    while True:
        if keyboard.is_pressed('F2'):
            keyboard.press_and_release('F2')
            keyboard.press_and_release('F2')
            keyboard.press_and_release('F2')
            keyboard.press_and_release('F2')
            time.sleep(0.1)
            pauseVal = not pauseVal
            print('정지상태 : ', pauseVal)
        time.sleep(0.05)

def f():
    global XY
    while(1):
        if(keyboard.is_pressed('c')):
            XY.append(coord())
            print('좌표설정:', XY)
            time.sleep(1)
        time.sleep(0.1)
    return

def begin():
    while(1):
        if keyboard.is_pressed('F1'):
            print("동작")
            for i in range(102):
                print(i,'번')
                click(XY[0])
                time.sleep(0.01)
                click(XY[0])
                time.sleep(0.01)
                click(XY[0])
                keyboard.press_and_release('Enter')
                keyboard.press_and_release('Enter')
                time.sleep(random.uniform(0.1, 0.15))
                keyboard.press_and_release('Enter')
                keyboard.press_and_release('Enter')
                time.sleep(random.uniform(0.4, 0.5))
                keyboard.press_and_release('Tab')
                time.sleep(random.uniform(0.1, 0.15))

                if pauseVal==True:
                    while(1):
                        time.sleep(0.1)
                        if pauseVal!=True:
                            break;
        time.sleep(0.03)


fth = Thread(target=f)
fth.start()

st = Thread(target=begin)
st.start()

stop = Thread(target=stop)
stop.start()

print("사용법")
print("좌표추가: c")
print("실행 F1, 일시정지 F2")