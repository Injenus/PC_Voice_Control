<!-- Оглавление -->
- [RUS](#rus-голосовое-управление-компьютером-без-интернета)
- [ENG](#eng-offline-voice-control-for-computer)

# (RUS) Голосовое управление компьютером без интернета

Этот проект представляет собой программу для голосового управления компьютером без необходимости подключения к интернету. Программа использует микрофон системы по умолчанию для распознавания команд.

## Возможности

- Программа включает прослушивание при отправке сигнала "1" в выбранный COM-порт (если прослушивание не предполагается, следует отправлять "0").
- После активации прослушивания, программа ожидает команды для выполнения.
- Прослушивание автоматически выключается через заданное время (по умолчанию - 6 секунд), если команда не была получена.
- Команды активируются только при полном совпадении с фразами, указанными в текстовых файлов (.txt), находящихся в папке "commands".
- Функции управления командами хранятся в файле "pcvc_control". Имена функций соответствуют именам команд-файлов (.txt).
- Для добавления новой команды необходимо создать соответствующий текстовый файл (.txt) и добавить соответствующую функцию в конец файла "pcvc_control".
- Используется русский язык, чтобы использовать другой, выберите соответствующую модель vosk.

## Индикация и завершение работы
Если вызваны "опасные" команды (например, переход в гибернацию или режим сна), то встроенный светодиод Arduino (плата исполянет роль отправки данных в COM-порт) начнёт мигать. По умолчанию, выполнение "опасных" команд происходит с задержкой в несколько секунд, что позволяет перехватить их выполнение (быстро шевелите мышкой, должно помочь :sweat_smile:). 

Во время работы программы, в системном трее появляется зелёный значок с изображением микрофона. Вы можете завершить работу программы следующими способами:

- Отправьте голосовую команду "выход".
- Щелкните правой кнопкой мыши на значке программы в трее и выберите "Exit" в контекстном меню.

# (ENG) Offline Voice Control for Computer

This project is a program for voice control of a computer without the need for an internet connection. The program utilizes the system's default microphone for command recognition.

## Features

- The program starts listening when a signal of "1" is sent to the selected COM port (send "0" to deactivate listening).
- Once the listening is activated, the program waits for commands to execute.
- The listening automatically turns off after a specified time (default is 6 seconds) if no command is received.
- Commands are triggered only when they match exactly with the phrases specified in the text files (.txt) located in the "commands" folder.
- Command handling functions are stored in the "pcvc_control" file. The function names correspond to the command file names (.txt).
- To add a new command, create a corresponding text file (.txt) and add the corresponding function at the end of the "pcvc_control" file.
- The Russian language is used, to use another language, select the corresponding Vosk model.

## Indication and Termination

If "dangerous" commands are invoked (e.g., hibernation or sleep mode), the built-in Arduino LED (which acts as a data sender to the COM port) will start blinking. By default, the execution of "dangerous" commands is delayed by a few seconds, allowing interception (quickly move the mouse, it should help :sweat_smile:).

During program operation, a green icon with a microphone image appears in the system tray. You can terminate the program in the following ways:

- Send the voice command "exit".
- Right-click on the program icon in the tray and select "Exit" from the context menu.

