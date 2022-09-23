# 1. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
#  За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# from random import randint

# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x


# def p_print(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

# player1 = input("Введите имя первого игрока: ")
# player2 = input("Введите имя второго игрока: ")
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0,2) # флаг очередности
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")

# counter1 = 0 
# counter2 = 0

# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = input_dat(player2)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)

# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")



# # 2. Создайте программу для игры в ""Крестики-нолики"".


# def position():
#     run = int(input("Введите номер строки "))
#     while run < 1 or run > 3:
#          print("введите корректный номер от 1 до 3")
        
#     column = int(input("Введите номер столбца "))
#     while 3 < column < 0:
#          print("введите корректный номер от 1 до 3")
        
#     return run, column


# def check(array):
#     if array[0][0] == array[1][0] == array[2][0] != '*':
#         return f'выиграл {array[0][0]}'
#     elif array[0][1] == array[1][1] == array[2][1] != '*':
#         return f'выиграл {array[0][1]}'
#     elif array[0][2] == array[1][2] == array[2][2] != '*':
#         return f'выиграл {array[0][2]}'
#     elif array[0][0] == array[0][1] == array[0][2] != '*':
#         return f'выиграл {array[0][0]}'
#     elif array[1][0] == array[1][1] == array[1][2] != '*':
#         return f'выиграл {array[1][0]}'
#     elif array[2][0] == array[2][1] == array[2][2] != '*':
#         return f'выиграл {array[2][0]}'
#     elif array[0][0] == array[1][1] == array[2][2] != '*':
#         return f'выиграл {array[0][0]}'
#     elif array[0][2] == array[1][1] == array[2][0] != '*':
#         return f'выиграл {array[0][2]}'
#     return None

    
# array = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

# i = 0
# flag = True
# value = 'X'
# while i < 9 and flag:
#     print('\n'.join(['\t'.join(i) for i in array]))
#     if i % 2 == 0:
#         print("ходят крестики ")
#         value = 'X'
#     else:
#         print("ходят нолики ")
#         value = '0'
#     run, column = position()

#     if array[run - 1][column-1] != '*':
#         print("эта позиция занята ")
#         run, column = position()

#     array[run-1][column-1] = value
#     resalt = check(array)
#     if resalt:
#        print(resalt)
#        flag = False
#     i += 1


        
# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# data = 'sssssrfuuuu'
# seq = []
# r = None
# for d in data:
#     if d != r:
#         seq.append(d)
#         seq.append(str(1))
#         r = d
#     else:
#         seq[-1] = str(int(seq[-1]) + 1)
# print("".join(seq))


