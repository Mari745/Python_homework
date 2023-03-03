#Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# a = int(input())
# if a == 0:
#     print(0)
# else:
#     fib_prev,fib_next = 0,1
#     n = 1
#     while fib_next <= a:
#         if fib_next == a:
#             print(n)
#             break
#         fib_prev,fib_next = fib_next,fib_prev+fib_next
#         n+=1
#     else:
#         print(-1)

#найти количество уникальных чисел

#list=[1,1,2,0,-1,3,4,4]
#print(len(set(list)))


# list=[1,2,3,4,5]
# list_2 = (list[len(list)- 2:]+list[ : 3])
# print(list_2)

# dictionary=[{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] 
# list=[]
# for a in dictionary:
#     for item in a:
#         list.append(a[item])
#     print(set(list))



# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером) 

# Input: [0, -1, 5, 2, 3]

# Output: 2 

# Пояснение: (-1 < 5, 2 < 3)

# list=[0, -1, 5, 2, 3]
# a=0
# for i in range(1,len(list)):
#     if list[i] > list[i-1]:
#         a += 1
# print(a)

# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4

# Output: 1 3 3 3 1
# def SwapMark(arr):
#     max=arr[0]
#     min=arr[0]
#     for i in range (1,len(arr)):
#         if max<arr[i]:
#             max=arr[i]
#         if min>arr[i]:
#             min=arr[i] 
#     for i in range (len(arr)):
#         if arr[i]==max:
#             arr[i]=min           
#     print(arr)
# arr=[1,2,3,4,5,4,3,2,2]
# SwapMark(arr)

# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

# Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)


# Input: 5

# Output: yes
# def Chek(number):
#     for i in range(2,number):
#         if number%i==0:
#             return(f"Число{number} не простое,так как делится на {i}")
    
#         return(f"Число простое")    
# number=int(input("Ввeдите число: "))
# res=Chek(number)
# print(res)   

# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

# Input:    2 -> 3 4
# Output: 4 3         
# def pos(number):
    
#     if number == 0:
#         return " "
#     x=int(input("Введите число: "))
#     return pos(number-1)+str(x)
# number = int(input("Введите количество элементов: "))
# print(pos(number))

# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

# def fib(n):
#     if n>0:
#         if n in [1,2]:
#             return 1
#         return fib(n-1)+fib(n-2)
#     else:
#         if n in [-1]:
#             return 1
#         return fib(n+1)-fib(n+2)
# list =[]
# for i in range(-10,-1):
#     list.append(fib(i))
# print(list)    

# def fib(n):
#     if n > 0:
#         if n in [1,2]:
#             return 1
#         return fib(n-1) + fib(n-2)
#     else:
#         if n in [-1]:
#             return 1
#         return fib(n+2) - fib(n+1)
# list = []
# for i in range(-10,-1):
#     list.append(fib(i))
# print(list)

# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. 
# Пользователь вводит  число N - количество элементов в первом массиве, затем N чисел - элементы массива.
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива
# Ввод: 					Вывод:
# 7					3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1			(каждое число вводится с новой строки)
# list1=[3, 1, 3,4, 2, 4, 12]
# list2=[4, 15, 43, 1, 15, 1]

# for i in range (len(list1)):
    
#         if list1[i] not in list2:
#             print(list1[i])          

# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. 
# Сначала вводится число N — количество элементов в массиве  Далее записаны N чисел — элементы массива.
# Массив состоит из целых чисел. 

# Ввод: 			Ввод:
# 5				5
# 1 2 3 4 5			1 5 1 5 1

# Вывод:			Вывод:
# 0				2
				
# (каждое число вводится с новой строки)

# import random
# list1 = []
# for i in range(1,10):
#     i = random.randint(1,10)
#     list1.append(i)
# print(list1)
# count = 0
# for i in range(1, len(list1)-1):
#     if list1[i-1] < list1[i] > list1[i+1]:
#         count += 1
# print(count)

# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.
# Ввод:			Вывод:
# 1 2 3 2 3			2

# list=[1,2,3,2,3]
# count=0
# for i in range(len(list)-1):
#     j=i+1
#     while j<len(list):
#         if list[i]==list[j]:
#             count+=1
#         j+=1
# print(count)

# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. 
# Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. 
# Программа получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
# Ввод:			Вывод:
# 300			220 284
        
# def sumDel(number):
#     sum = 0
#     for i in range(1, number):
#         if number % i == 0:
#             sum = sum + i
#     return sum
# number1 = 1
# number2 = 1
# numberK = int(input('Введите число: '))
# for i in range(2, numberK):
#     for j in range(i+1, numberK):
#         number1 = i
#         number2 = j
#         if sumDel(number1) == number2 and sumDel(number2) == number1:
#             print(f'{number1} и {number2}')