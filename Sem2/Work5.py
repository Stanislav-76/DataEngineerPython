# Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
# Используйте комплексные числа для извлечения квадратного корня.

a = float(input('Введите a: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))

d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    result = f'У уравнения два корня: {x1 = } и {x2 = }'
elif d == 0:
    x = -b / (2 * a)
    result = f'У уравнения один корень: {x = }'
else:
    d = complex(d, 0)
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    result = f'У уравнения два комплексных корня: {x1 = } и {x2 = }'
    print(result)
