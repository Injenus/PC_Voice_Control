import pyautogui
import time
import subprocess
import webbrowser
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

microphone_index = 1


def mic_index():
    return microphone_index


def get_display_size():
    display_width, display_height = pyautogui.size()
    return display_width, display_height


width, height = get_display_size()

print("Ширина дисплея:", width)
print("Высота дисплея:", height)


### ФУНКЦИИ ЭМУЛЯЦИИ ############################
def move_cursor(x, y, delay=0.001):
    pyautogui.moveTo(x, y)
    time.sleep(delay)


def click_left(delay=0.001):
    pyautogui.click()
    time.sleep(delay)


def double_click_left(delay=0.001):
    pyautogui.doubleClick()
    time.sleep(delay)


def press_keys(keys):
    pyautogui.hotkey(*keys)


def launch_application(shortcut_path, delay=0.001):
    subprocess.Popen(shortcut_path)
    time.sleep(delay)


def open_terminal_and_print_info(info):
    global isInforming, process
    if isInforming:
        process = subprocess.Popen(
            ['cmd', '/c', 'start', 'cmd', '/k', 'echo', info])
    else:
        # Запускаем новый процесс в терминале
        process = subprocess.Popen(
            ['cmd', '/c', 'start', 'cmd', '/k', 'echo', info])
        isInforming = True


def open_new_tab(url):
    webbrowser.open_new_tab(url)


#############   ФУКНЦИИ УПАРВЛЕНИЯ    ####################
def check():
    pass


def mute():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMute(1, None)


def unmute():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMute(0, None)


def louder(delta=2):
    try:
        # Получение объекта устройства вывода по умолчанию
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL,
                                     None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        # Получение текущей громкости
        current_volume = volume.GetMasterVolumeLevel()
        # Изменение громкости (увел на delta децибел)
        volume.SetMasterVolumeLevel(current_volume + delta, None)
    except Exception:
        pass


def quiter(delta=3.5):
    try:
        # Получение объекта устройства вывода по умолчанию
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL,
                                     None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        # Получение текущей громкости
        current_volume = volume.GetMasterVolumeLevel()
        # Изменение громкости (уменьшение на  delta децибел)
        volume.SetMasterVolumeLevel(current_volume - delta, None)
    except Exception:
        pass


def lock(isOk=True, isWarn=False, delay=0):
    print("LOCK")
    delay = int(delay)
    for i in range(delay):
        info = '. . . {} . . .'.format(delay - i)
        print(info)
        if isWarn and i % 5 == 0:
            open_terminal_and_print_info(info)
        time.sleep(1)
    # move_cursor(25, height - 25)
    # click_left()
    press_keys(['win'])
    move_cursor(25, height - 620)
    click_left()
    move_cursor(50, height - 725)
    click_left()
    if isOk:
        click_left()


def pause():
    press_keys(['space'])


def stellarium():
    launch_application('C:\Program Files\Stellarium\stellarium.exe')


def photoshop():
    launch_application(
        "C:\Program Files (x86)\Adobe\Adobe Photoshop CS6\Photoshop.exe")


def pycharm():
    launch_application(
        "C:\Program Files\JetBrains\PyCharm Community Edition 2020.2.1\\bin\pycharm64.exe")


def consultant():
    open_new_tab('https://chat.openai.com/')


def youtube():
    open_new_tab('https://www.youtube.com/')


def ozon():
    open_new_tab('https://www.ozon.ru/my/orderlist')
