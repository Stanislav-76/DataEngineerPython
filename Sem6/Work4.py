# Создайте модуль с функцией внутри. 
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

import module2 as md2

riddle = "Ночью он не любит спать, Ему хочется гулять." \
"Молоко из плошки пьёт,Это наш домашний… * "

md2.guess_riddle(riddle, ["кот", "динозавр", "лев", "медведь", "страус"], 5)