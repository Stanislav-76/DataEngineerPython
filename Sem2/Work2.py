import sys

# Создайте в переменной data список значений разных типов перечислив их через запятую внутри квадратных скобок.
# Для каждого элемента в цикле выведите:
#  порядковый номер начиная с единицы
#  значение
#  адрес в памяти
#  размер в памяти
#  хэш объекта
#  результат проверки на целое число только если он положительный
#  результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.


data = [42, 73.0, 'Hello world!', True, 42, 'Hello world!', 256, 2 ** 8, 1, 'Привет, мир!']
for i, item in enumerate(data, start=1):
    check_int = 'Похоже на целое число' if isinstance(item, int) else ''
    check_str = 'Это строка' if isinstance(item, str) else ''
    print(f'{i}. Объект {item}\nАдрес: {id(item)}\tРазмер: {sys.getsizeof(item)}'
          f'\tХэш: {hash(item)} {check_int}{check_str}', end='\n')
