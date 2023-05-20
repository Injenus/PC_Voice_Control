from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import time
# Получение объекта устройства вывода по умолчанию
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Получение текущей громкости
current_volume = volume.GetMasterVolumeLevel()

# Изменение громкости (уменьшение на 1.0 децибел)
volume.SetMasterVolumeLevel(current_volume + 1.0, None)

def mute_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMute(1, None)

def unmute_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMute(0, None)

# Пример использования функций:
mute_volume()  # Отключение звука
# Выполните здесь нужные действия, при которых звук должен быть отключен
time.sleep(10)
unmute_volume()  # Включение звука на прежней громкости