'''
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''

month_list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
season = ['зима', 'весна', 'лето', 'осень']

month_dict = dict()                      # словарь месяцев с ключами по порядковому номеру
for i in range(len(month_list)):
    month_dict.setdefault(i+1)
    month_dict[i+1] = month_list[i]
# print(month_dict)

season_dict = dict()                     # словарь сезонов с ключом по названию сезона
for i in range(len(season)):
    season_dict.setdefault(season[i])    # создан словарь сезонов
    season_dict[season[i]] = list()       # в словаре сезонов каждый сезон это будет список месяцев
    for m in range(3):
        season_dict[season[i]].append(month_list[(m - 1) + (3 * i)])  # к каждому сезону в словаре сезонов добавляем список месяцев
# print(season_dict)

while True:
    num = int(input('Введите номер месяца: '))
    answer = ''
    for i in range(4):
        if month_list[num - 1] in season_dict[season[i]]:
            answer = season[i]
    print(f"Месяц № {num} - это {month_list[num - 1]}, и это {answer}.")
    more = input('Нажмите Enter, если хотите проверить еще раз, или введите любой символ, чтобы закончить. ')
    if more != '':
        break