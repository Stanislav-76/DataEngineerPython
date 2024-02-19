# Пользователь вводит строку текста. 
# Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним. 
# Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке. 
# Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.

text = input('Введите несколько слов: ')

result_1 = {}
for char in set(text):
    result_1[char] = text.count(char)
    
result_2 = {}
for char in text:
    if char in result_2:
        result_2[char] += 1
    else:
        result_2[char] = 1
        
print(f'{result_1 = }\n{result_2 = }')
