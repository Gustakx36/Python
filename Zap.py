import time
import pyautogui

#pyautogui.click(x=1074, y=617) #abrir opera
#pyautogui.click(x=962, y=695) #abrir zap
#pyautogui.click(x=462, y=682) #tela de digit
pyautogui.click(x=201, y=767) #digitar

for i in range(14):
    pyautogui.moveTo(x=1079, y=626)
    pyautogui.click(x=1079, y=626) #abrir opera

    pyautogui.moveTo(x=962, y=695)
    pyautogui.click(x=962, y=695) #abrir zap

    pyautogui.moveTo(x=847, y=463)
    pyautogui.click(x=847, y=463) #tela de digit



time.sleep(5)
x = pyautogui.position()#
print(x)
