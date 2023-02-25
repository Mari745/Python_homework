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

list=[0, -1, 5, 2, 3]
a=0
for i in range(1,len(list)):
    if list[i] > list[i-1]:
        a += 1
print(a)
