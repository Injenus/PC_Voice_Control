import keyboard

def detect_key_combination():
    combination = keyboard.read_hotkey(suppress=True)
    combination_names = keyboard.get_hotkey_name(combination)
    return combination_names

# Пример вызова функции для определения комбинации нажатых клавиш
combination = detect_key_combination()
print("Обнаружена комбинация клавиш:", combination)
print(type(combination))
