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

def fib(n):
    if n>0:
        if n in [1,2]:
            return 1
        return fib(n-1)+fib(n-2)
    else:
        if n in [-1]:
            return 1
        return fib(n+1)-fib(n+2)
list =[]
for i in range(-10,-1):
    list.append(fib(i))
print(list)    

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