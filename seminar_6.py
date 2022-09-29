# Таблица умножения/сложения/деления

# def operation_table(func, row=9, columns=9):
#      for i in range(row):
#          for j in range(columns):
#             print(f'{func(i + 1, j + 1)}', end=' \t')
# print()


# operation_table(lambda x, y: x * y, 5)



# Задача на ритм 

# def viny_song(song):
# vowels = ["а", "я", "у", "ю", "о", "е", "ё", "э", "и", "ы"]
# lst = [len(list(filter(lambda x: x in vowels,i))) for i in song.split()]
# return ('Пам парам','Парам пам-пам')[len(set(lst)) == 1]
