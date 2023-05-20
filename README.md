# Голосовое управление компьютером без интернета

Этот проект представляет собой программу для голосового управления компьютером без необходимости подключения к интернету. Программа использует микрофон системы по умолчанию для распознавания команд.

## Возможности

- Программа включает прослушивание при отправке сигнала "1" в выбранный COM-порт (если прослушивание не предполагается, следует отправлять "0").
- После активации прослушивания, программа ожидает команды для выполнения.
- Прослушивание автоматически выключается через заданное время (по умолчанию - 6 секунд), если команда не была получена.
- Команды активируются только при полном совпадении с фразами, указанными в текстовых файлов (.txt), находящихся в папке "commands".
- Функции управления командами хранятся в файле "pcvc_control". Имена функций соответствуют именам команд-файлов (.txt).
- Для добавления новой команды необходимо создать соответствующий текстовый файл (.txt) и добавить соответствующую функцию в конец файла "pcvc_control".

## Индикация и завершение работы
Если вызваны "опасные" команды (например, переход в гибернацию или режим сна), то встроенный светодиод Arduino (плата исполянет роль отправки данных в COM-порт) начнёт мигать. По умолчанию, выполнение "опасных" команд происходит с задержкой в несколько секунд, что позволяет перехватить их выполнение (быстро шевелите мышкой, должно помочь :sweat_smile:). 

Во время работы программы, в системном трее появляется зелёный значок с изображением микрофона. Вы можете завершить работу программы следующими способами:

- Отправьте голосовую команду "выход".
- Щелкните правой кнопкой мыши на значке программы в трее и выберите "Exit" в контекстном меню.
