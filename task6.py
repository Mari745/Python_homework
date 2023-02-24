n=int(input("Введите количество монет:"))
countA = countB = 0
for i in range(n):
    x=int(input("Орел(1) или Решка(0)?"))
    if x == 1:
        countA += 1
    else:
        countB += 1
if countA < countB:
    print('Переверните {countA} монет с орла на решку')
else:
    print('Переверните {countB} монет с решки на орла')




