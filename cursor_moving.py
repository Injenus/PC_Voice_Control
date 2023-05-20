import pyautogui
import time
import subprocess
import tkinter as tk

isInforming = False
# Путь к exe приложения
exe_pathes = ["C:\Program Files\Stellarium\stellarium.exe"]


def get_display_size():
    display_width, display_height = pyautogui.size()
    return display_width, display_height


width, height = get_display_size()

print("Ширина дисплея:", width)
print("Высота дисплея:", height)


def move_cursor(x, y, delay=0.001):
    pyautogui.moveTo(x, y)
    time.sleep(delay)


def click_left(delay=0.001):
    pyautogui.click()
    time.sleep(delay)


def double_click_left(delay=0.001):
    pyautogui.doubleClick()
    time.sleep(delay)


def launch_application(shortcut_path, delay=0.001):
    subprocess.Popen(shortcut_path)
    time.sleep(delay)


def hybernation(isOk=False, isWarn=True, delay=0):
    print("HYBERNATION")
    delay = int(delay)
    move_cursor(25, height - 25)
    click_left()
    move_cursor(25, height - 80)
    click_left()
    move_cursor(50, height - 225)
    click_left()
    for i in range(delay):
        info = '{}...'.format(delay - i)
        print(info)
        if isWarn:
            open_terminal_and_print_info(info)
        time.sleep(1)
    if isOk:
        click_left()


def sleep_mode(isOk=False, isWarn=False, delay=5):
    print("SLEEP")
    delay = int(delay)
    move_cursor(25, height - 25)
    click_left()
    move_cursor(25, height - 80)
    click_left()
    move_cursor(50, height - 268)
    click_left()
    for i in range(delay):
        info = '. . . {} . . .'.format(delay - i)
        print(info)
        if isWarn:
            open_terminal_and_print_info(info)
        time.sleep(1)
    if isOk:
        click_left()


def open_terminal_and_print_info(info):
    global isInforming
    if isInforming:
        # subprocess.call(['cmd', '/c', 'echo', info])
        subprocess.Popen(['cmd', '/c', 'start', 'cmd', '/k', 'echo', info])
    else:
        # Запускаем новый процесс в терминале
        subprocess.Popen(['cmd', '/c', 'start', 'cmd', '/k', 'echo', info])
        isInforming = True


import webbrowser

def open_new_tab(url):
    webbrowser.open_new_tab(url)

# Пример использования
url = 'https://www.example.com'
#open_new_tab(url)

def lock(isOk=False, isWarn=False, delay=0):
    print("LOCK")
    delay = int(delay)
    move_cursor(25, height - 25)
    click_left()
    move_cursor(25, height - 620)
    click_left()
    move_cursor(50, height - 725)
    click_left()
    for i in range(delay):
        info = '. . . {} . . .'.format(delay - i)
        print(info)
        if isWarn:
            open_terminal_and_print_info(info)
        time.sleep(1)
    if isOk:
        click_left()
lock()