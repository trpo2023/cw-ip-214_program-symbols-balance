**Техническое задание: Программа проверки баланса скобок в программе на языке C**

**1. Функциональность проекта:**
   - Программа предназначена для проверки баланса скобок в исходном коде программы на языке C.
   - Задачи продукта включают в себя выявление несоответствий открытых и закрытых скобок, а также определение их расположения в коде.
   - Программа должна поддерживать различные типы скобок, такие как круглые "()", квадратные "[]", и фигурные "{}".
   - Программа должна предоставлять информацию о том, где именно в коде обнаружены ошибки и какие именно скобки вызывают проблемы.

**2. Формат входных данных:**
   - Входные данные представляют собой текстовый файл с исходным кодом программы на языке C.
   - Файл должен иметь расширение ".c".
   
**3. Интерфейс приложения:**
   - Приложение работает в интерактивном режиме в командной строке.
   - Пользователь запускает программу и вводит путь к файлу с исходным кодом.
   - После анализа кода, программа выводит сообщения о балансе скобок и местоположении ошибок.
   - Программа также может предоставить возможность сохранить результаты анализа в файл.

**4. Аргументы командной строки:**
   - Программа принимает один обязательный аргумент командной строки - путь к файлу с исходным кодом (полный или относительный).
   - Пример использования: `balance_checker.exe /path/to/source_code.c`

**5. Взаимодействие с внешними источниками данных:**
   - Программа не использует внешние источники данных, конфигурационные файлы или базы данных.
   - Все необходимые данные для анализа баланса скобок берутся из входного файла с исходным кодом.

**6. Дополнительные требования:**
   - Приложение должно обрабатывать ошибки и неожиданные ситуации и информировать пользователя об ошибках, если таковые возникнут.
   - Результат анализа должен быть четким и понятным, с указанием номеров строк, в которых найдены проблемы.

**7. Требования к выводу:**
   - Программа должна выдавать информативные сообщения об обнаруженных ошибках в балансе скобок, указывая тип скобок (круглые, квадратные, фигурные) и номер строки, где ошибка обнаружена.
   - Пример сообщения: "Ошибка в строке 10: Не согласованные фигурные скобки {}."
