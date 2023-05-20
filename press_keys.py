import pyautogui
import time

def press_keys(keys):
    pyautogui.hotkey(*keys)


# Пример вызова функции для эмуляции комбинации клавиш "Ctrl" + "C"
press_keys(['win'])
### ff