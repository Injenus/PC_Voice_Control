import time
import sys
import pystray
from PIL import Image
import threading
import signal


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
    menu = (pystray.MenuItem("Item", on_clicked),)
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


def exit():
    # Завершаем программу
    exit_program(icon, None)
    # Останавливаем поток и выходим из программы
    tray_thread.join()

while running:
    time.sleep(2)
    print('smth')

exit()