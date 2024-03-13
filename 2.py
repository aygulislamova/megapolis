import csv
#открытие файла
with open('game.csv', encoding='utf-8') as f:
    reader = list(csv.reader(f))[1:]
    #перебор строк файла
    pers = {}
    for row in reader:
        pers[row[1]] =  + 1
print(pers)


