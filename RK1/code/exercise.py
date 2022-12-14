"""
1) Необходимо создать два класса данных в соответствии с Вашим вариантом
предметной области, которые связаны отношениями один-ко-многим и
многие-ко-многим.

Пример классов данных для предметной области Сотрудник-Отдел:
(1) Класс «Сотрудник», содержащий поля:
- ID записи о сотруднике;
- Фамилия сотрудника;
- Зарплата (количественный признак);
- ID записи об отделе. (для реализации связи один-ко-многим)
(2) Класс «Отдел», содержащий поля:
- ID записи об отделе;
- Наименование отдела.
(3) (Для реализации связи многие-ко-многим) Класс «Сотрудники отдела»,
содержащий поля:
- ID записи о сотруднике;
- ID записи об отделе.


2) Необходимо создать списки объектов классов, содержащих тестовые данные
(3-5 записей), таким образом, чтобы первичные и вторичные ключи
соответствующих записей были связаны по идентификаторам.


3) Необходимо разработать запросы в соответствии с Вашим вариантом. Запросы
сформулированы в терминах классов «Сотрудник» и «Отдел», которые используются
в примере. Вам нужно перенести эти требования в Ваш вариант предметной области.
При разработке запросов необходимо по возможности использовать функциональные
возможности языка Python (list/dict comprehensions, функции высших порядков).
Для реализации запроса №2 введите в класс, находящийся на стороне связи
«много», произвольный количественный признак, например, «зарплата сотрудника».

Результатом рубежного контроля является документ в формате PDF, который
содержит текст программы и результаты ее выполнения.


                Вариант 17 ДИРИЖЕР(сотрудник)-ОРКЕСТР(отдел):
1) «Отдел» и «Сотрудник» связаны соотношением один-ко-многим. Выведите список
всех сотрудников, у которых фамилия заканчивается на «ов», и названия их
отделов.

2) «Отдел» и «Сотрудник» связаны соотношением один-ко-многим. Выведите список
отделов со средней зарплатой сотрудников в каждом отделе, отсортированный по
средней зарплате (отдельной функции вычисления среднего значения в Python нет,
нужно использовать комбинацию функций вычисления суммы и количества значений).

3) «Отдел» и «Сотрудник» связаны соотношением многие-ко-многим. Выведите список
всех отделов, у которых название начинается с буквы «А» (заменил на "Р"), и список работающих
в них сотрудников.

"""