import pyaudio


def list_microphones():
    audio = pyaudio.PyAudio()
    info = audio.get_host_api_info_by_index(0)
    num_devices = info.get('deviceCount')

    print("Доступные микрофоны:")
    for i in range(num_devices):
        device_info = audio.get_device_info_by_host_api_device_index(0, i)
        device_name = device_info.get('name')
        print(f"Индекс: {i}, Имя: {device_name}")

    audio.terminate()


# Вызываем функцию для вывода индексов доступных микрофонов
list_microphones()
