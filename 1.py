
import csv
#открытие файла
with open('game.csv', encoding='utf-8') as f:
    reader = list(csv.reader(f))
    game_new = []
    #перебор строк файла
    for row in reader:
        #поиск нужного игрока
        if 'Avery' in row[1]:
            game_new.append(f'У персонажа {row[1]} в игре {row[0]} нашлась ошибка с кодом: {row[-2]}. Дата фиксации: {row[-1]}')
    for row in reader:
        if 'Avery' in row[1]:
            game = row[0]
            break
#создание строки для первого файла
st = ''
for i in game_new:
    st += i+'\n'
    #запись первого файла
with open('game_new.txt', mode='w', encoding='utf-8') as f:
    f.write(st)
    #запись второго файла
with open('avery.txt', mode='w', encoding='utf-8') as f:
    f.write(game)