# AIS
Лабораторные работы по дисциплине "Системы искусственного интеллекта" 3 курс ПИиКТ

## Лабораторная 1 ##
### Задание: ###

Составить базу знаний на языке Пролог, которая будет содержать генеалогическое дерево
семьи с указанием родственных отношений (например, папа, бабушка и т.д.), опираясь на два
первичных факта: родитель и супруг.

Что должно быть в отчёте:

1. Задание.

2. Картинка с родословным деревом

3. База знаний должна состоять не менее чем из 50 фактов и не менее чем 10 правил.

4. Результаты проверки фактов и правил на примерах.

## Лабораторная 2 ##

##### Правило выбора варианта задания.
Дату рождения подвергнуть следующей свертке: (ДД + ММ) mod 10 + 1 = номер варианта.

Мой вариант: ((31 + 07) mod 10) + 1 = 9

Исходный пункт | Пункт назначения
------|------
Брест | Казань

### Цель

Исследование алгоритмов решения задач методом поиска.

### Описание предметной области

 Имеется транспортная сеть, связывающая города СНГ. Сеть представлена в виде таблицы связей между городами. Связи являются двусторонними, т.е. допускают движение в обоих направлениях. Необходимо проложить маршрут из одной заданной точки в другую.

### Этап 1 Неинформированный поиск

На этом этапе известна только
топология связей между городами. Выполнить:


1. поиск в ширину;


2. поиск глубину;


3. поиск с ограничением глубины;


4. поиск с итеративным углублением;


5. двунаправленный поиск.


Отобразить движение по дереву на его графе с указанием сложности каждого вида поиска. Сделать выводы.


### Этап 2 Информированный поиск

Воспользовавшись информацией о
протяженности связей от текущего узла, выполнить:


1. жадный поиск по первому наилучшему соответствию;


2. затем, использую информацию о расстоянии до цели по прямой от каждого узла, выполнить поиск методом минимизации суммарной оценки А*.


Отобразить на графе выбранный маршрут и сравнить его сложность с неинформированным поиском. Сделать выводы.

Правило выбора варианта задания. Дату рождения подвергнуть следующей свертке: (ДД + ММ) mod 10 + 1 = номер варианта.




Таблица связей между городами:


Город 1 | Город 2 | Расстояние, км
------- | --------| -----
Вильнюс | Брест | 531
Витебск | Брест | 638
Витебск | Вильюс | 360 
Воронеж | Витебск | 869 
Воронеж | Волгоград | 581
Волгоград | Витебск | 1455
Витебск | Ниж.Новгород | 911
Вильнюс | Даугавпилс | 211
Калининград | Брест | 699
Калиниград  |Вильнюс | 333
Каунас | Вильнюс | 102 
Киев | Вильнюс | 734
Киев | Житомир | 131
Житомир | Донецк | 863
Житомир | Волгоград | 1493
Кишинев | Киев | 467
Кишинев | Донецк | 812
С.Петербург | Витебск | 602
С.Петербург | Калининград | 739
С.Петербург | Рига | 641
Москва | Казань | 815
Москва | Ниж.Новгород | 411
Москва | Минск | 690
Москва | Донецк | 1084
Москва | С.Петербург | 664
Мурманск | С.Петербург | 1412
Мурманск | Минск | 2238
Орел | Витебск | 522
Орел | Донецк | 709
Орел | Москва | 368
Одесса | Киев | 487
Рига | Каунас | 267
Таллинн | Рига | 308
Харьков | Киев | 471
Харьков | Симферополь | 639
Ярославль | Воронеж | 739
Ярославль | Минск | 940
Уфа | Казань | 525
Уфа | Самара | 461

