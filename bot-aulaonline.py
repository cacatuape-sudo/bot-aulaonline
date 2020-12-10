import pyautogui
import time
import threading 
  
def prh():
  for i in range(1):
    pyautogui.leftClick(1257,617) 
    time.sleep(10)
    pyautogui.leftClick(1708,124) 
    time.sleep(1.3)
    pyautogui.write('Bom Dia')
    pyautogui.press('enter')
    time.sleep(8)
    pyautogui.leftClick(200,44)

def seh():
  for i in range(1):
    pyautogui.leftClick(1257,617) 
    time.sleep(10)
    pyautogui.leftClick(1708,124) 
    time.sleep(1.3)
    pyautogui.write('Bom Dia')
    pyautogui.press('enter')
    time.sleep(8)
    pyautogui.leftClick(200,44)


def teh():
  for i in range(1):
    pyautogui.leftClick(1257,617) 
    time.sleep(10)
    pyautogui.leftClick(1708,124) 
    time.sleep(1.3)
    pyautogui.write('Bom Dia')
    pyautogui.press('enter')
    time.sleep(8)
    pyautogui.leftClick(200,44)

def qah():
  for i in range(1):
    pyautogui.leftClick(1257,617) 
    time.sleep(10)
    pyautogui.leftClick(1708,124) 
    time.sleep(1.3)
    pyautogui.write('Bom Dia')
    pyautogui.press('enter')
    time.sleep(8)
    pyautogui.leftClick(200,44)
 

def qih():
  for i in range(1):
    pyautogui.leftClick(1257,617) 
    time.sleep(10)
    pyautogui.leftClick(1708,124) 
    time.sleep(1.3)
    pyautogui.write('Bom Dia')
    pyautogui.press('enter')
    time.sleep(8)
    pyautogui.leftClick(200,44)

def sxh():
  for i in range(1):
    pyautogui.leftClick(1257,617) 
    time.sleep(10)
    pyautogui.leftClick(1708,124) 
    time.sleep(1.3)
    pyautogui.write('Bom Dia')
    pyautogui.press('enter')
    time.sleep(8)
    pyautogui.leftClick(200,44)
                  

t1 = threading.Thread(target=prh)  
t2 = threading.Thread(target=seh)  
t3 = threading.Thread(target=teh)  
t4 = threading.Thread(target=qah)  
t5 = threading.Thread(target=qih)  
t6 = threading.Thread(target=sxh)  

t1.start()
time.sleep(6.1)
t2.start()
time.sleep(6.1)
t3.start()
time.sleep(6.1)
t4.start()
time.sleep(6.1)
t5.start()
time.sleep(6.1)
t6.start()

