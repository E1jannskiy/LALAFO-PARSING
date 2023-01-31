from django.test import TestCase

# Create your tests here.

# 1. Найти API сайта используя Dev Tools(подсказка - network)
#     2. Узнать id нескольких категорий:
#        1. Продажа авто
#        2. Аренда квартир
#        3. Продажа квартир
#     3. Написать скрипт для парсинга этих категорий с каждой категории по 20шт объявлений (итого получится 60 объявлений)
#     4. Поля которые нужно спарсить:
#        1. заголовок
#        2. описание
#        3. цена
#        4. город
#        5. категория
#        6. фотки(обязательно все!)
#    7. телефон
#    8. автор
# 5. Записать все объявления в подходящий питоновский объект и в json файл
# 6. Создать джанго проект "Объявления". Подключить PostgreSQL в качестве базы данных
# 7. Спроектировать и создать модели с вышеперечисленными полями
# 8. Написать вьюшку для создания объявления
# 9. Дополнить скрипт парсинга, чтобы после стягивания данных из lalafo он записывал эти данные в базу данных нашего проекта
# 10. Замерить скорость работы скрипта при общем количестве объявлений в 1000шт. Найти способ ускорить скрипт(подсказка - асинхронный питон) и переделать!
    