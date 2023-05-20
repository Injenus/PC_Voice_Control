import json, pyaudio
from vosk import Model, KaldiRecognizer
from Levenshtein import distance as lev
import os
import pyautogui
import time
import subprocess
import webbrowser
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import serial
import sys
import pystray
from PIL import Image
import threading
import signal
from pcvc_control import *

lang_model = 'D:\\PyProjects\\robotic_arm\\vosk-model-small-ru-0.22'
rate = 16000 if "small" in lang_model else 8000
model = Model(lang_model)
rec = KaldiRecognizer(model, rate)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=rate, input=True,
                frames_per_buffer=8000)
stream.start_stream()
isLive = True

port = 'COM7'
baudrate = 115200
ser = serial.Serial(port, baudrate)
voice_data = 0


# Функция, при щелчке на значке в трее
def on_clicked(icon, item):
    print("Значок в трее был щелкнут")
    global running
    running = False


running = True
icon = None


def create_tray_icon():
    global running, icon
    image = Image.open("image.png")
    menu = (pystray.MenuItem("Exit", on_clicked),)
    icon = pystray.Icon("name", image, "PC VC", menu)
    icon.run()


def exit_program(icon, item):
    if icon is not None:
        icon.stop()
    sys.exit(0)


# Регистрируем функцию exit_program для выполнения перед закрытием программы
signal.signal(signal.SIGTERM, exit_program)
signal.signal(signal.SIGINT, exit_program)

# Создаем отдельный поток для создания значка в трее
tray_thread = threading.Thread(target=create_tray_icon)
tray_thread.start()

isInforming = False
time_init = 0
interval = 6


####################################

def read_files_in_folder(folder_path):
    files = os.listdir(folder_path)
    data_dict = {}

    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path) and file_name.endswith('.txt'):
            name_without_extension = os.path.splitext(file_name)[0]
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                data_dict[name_without_extension] = [line.strip() for line in
                                                     lines]

    return data_dict


folder_path = 'commands'
commands_dict = read_files_in_folder(folder_path)
print(commands_dict)


####  ФУНКЦИИ  УПРАВЛЕНИЯ ############################
### остальные функции в модуле pcvc_control
def exit():
    # Завершаем программу
    exit_program(icon, None)
    # Останавливаем поток и выходим из программы
    tray_thread.join()
    sys.exit(0)

def hibernation(isOk=True, isWarn=False, delay=25):
    ser.write(b'1')
    print("HIBERNATION")
    delay = int(delay)
    for i in range(delay):
        info = '{}...'.format(delay - i)
        print(info)
        if isWarn and i % 5 == 0:
            open_terminal_and_print_info(info)
        time.sleep(1)
    # move_cursor(25, height - 25)
    # click_left()
    press_keys(['win'])
    move_cursor(25, height - 80)
    click_left()
    move_cursor(50, height - 225)
    click_left()
    ser.write(b'1')
    if isOk:
        click_left()


def sleep_mode(isOk=True, isWarn=False, delay=15):
    ser.write(b'1')
    print("SLEEP")
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
    move_cursor(25, height - 80)
    click_left()
    move_cursor(50, height - 268)
    click_left()
    ser.write(b'1')
    if isOk:
        click_left()

############################################
def listen():
    global time_init, interval
    while isLive:
        if time.time() - time_init < interval:
            data = stream.read(4000, exception_on_overflow=False)
            if (rec.AcceptWaveform(data)) and (len(data) > 0):
                answer = json.loads(rec.Result())
                if answer['text']:
                    yield answer['text']
        else:
            yield []


def get_substr(string, length=4):
    substrings = []
    for i in range(len(string) - length + 1):
        substring = string[i:i + length]
        substrings.append(substring)
    return substrings


def has_duplicates(list1, list2):
    # Преобразовываем списки строк в множества строк для быстрого поиска
    set1 = set(list1)
    set2 = set(list2)
    # Ищем пересечение множеств, чтобы найти одинаковые строки
    common_strings = set1.intersection(set2)
    # Если пересечение не пустое, то есть общие строки, возвращаем True
    if common_strings:
        print("# ", common_strings)
        return (True, len(common_strings) / (min(len(list1), len(list2)) - 2))
    # Если пересечение пустое, то общих строк нет, возвращаем False
    else:
        return (False, 0)


def select_command(comm, set, func):
    # try:
    #     lst_comm = get_substr(comm)
    #     while len(comm) < 4:
    #         comm += '_'
    #     print(comm)
    #     l_text = len(comm)
    #     for key in set:
    #         lst_key = get_substr(key)
    #         l_key = len(key)
    #         isHas, otn_num_dup = has_duplicates(lst_comm, lst_key)
    #         lev_d = lev(comm, key) / min(l_key, l_text)
    #         if lev_d == 0:
    #             func()
    #             print('### ', lev_d)
    #             return 1
    #         if lev_d <= 0.1 and isHas:
    #             func()
    #             print('### ', lev_d, isHas)
    #             return 1
    #         # elif otn_num_dup >= 2 / 3 and lev_d < 1:
    #         #     func()
    #         #     print('### ', lev_d, isHas, otn_num_dup)
    #         #     return 1
    #         else:
    #             # print('# smth wrong')
    #             # print('# ', lev_d, isHas, otn_num_dup)
    #             print(lev_d, isHas, otn_num_dup, key)
    #             pass
    #     else:
    #         return False
    # except Exception:
    #     print('HZ#ERROR')
    #     # initial_position()
    #     return False

    try:
        for key in set:
            # print(key)
            if comm == key:
                return True
        else:
            # print('Точных совпадений не найдено...')
            return False
    except Exception:
        print("### ОШИБКА ПРИ ОПРЕДЕЛЕНИИ КОМАНДЫ:", set)


def audio_cntrl():
    global isLive, isInforming
    isLive = True
    for text in listen():
        print(text)
        # Обход словаря и вызов функций по ключам
        for key, value in commands_dict.items():
            if callable(eval(key)):
                function = eval(key)
                # function() #непосредственный вызов функции
                if select_command(text, value, function):
                    print("ВЫПОЛНЯЕТСЯ:", key)
                    function()
                    isLive = False
                    isInforming = False
                    break
                else:
                    print("НЕ ПОДХОДИТ:", key)
        print('none')
        isLive = False
        return 0
    else:
        print('E_N_D')
        isLive = False
        return 0


comdata = 0
while running:
    ser.flushInput()
    try:
        comdata = int(ser.readline().strip().decode('utf-8'))
    except Exception:
        comdata = comdata
    if comdata:
        print('Listen...')
        time_init = time.time()
        audio_cntrl()
        print('Done')
        comdata = 0
exit()
