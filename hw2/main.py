import numpy as np
from sympy import symbols, Eq, solve, sympify


""" Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть """


print("Please enter number of coins")
coins = int(input())
listCoins = np.random.randint(0, 2, coins)
print(*listCoins)

heads = 0
tails = 0

for i in listCoins:
   if i == 0: heads +=1
   else: tails +=1

print("The minimum number of coins you need to flip is - ", end = " ")
if heads>tails: print(tails, "tails")
else: print(heads, "heads")





""" Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа. """


print("Please enter sum of numbers: ")
sum = int(input())
print("Please enter product of numbers:")
multip = int(input())

x = symbols('x')
y = symbols('x')
xEquation = Eq(x + multip/x, sum)
sol = solve(xEquation)
yEquation = Eq(sol[0]*y, multip)
solve(yEquation)


if sympify(sol[0]).is_integer and sympify(sol[1]).is_integer:
   if sol[0] and sol[1] <=1000:
      print("The first number is", sol[0], "and the second one is", sol[1])
   else: print("Correct numbers are more than 1000")
else: print("Impossible for Kate to find an answer with given numbers")







# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.



print("Please enter max value for powers of 2")
exponent = int(input())
result = 1

for i in range(1, exponent+1):
   result*=2
   if(i!=exponent):
      print(result, end = ", ")
   else:
      print(result, end = ".")
