'''
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
'''

total_sec = int(input('Введите количество секунд: '))
hour = total_sec // 3600
min = total_sec // 60
sec = total_sec % 60
print(f"Время составляет {hour}:{min}:{sec}")
