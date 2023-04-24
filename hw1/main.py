from sympy import symbols, Eq, solve
import math
import random

# Задача 2: Найдите сумму цифр трехзначного числа.

print("Please enter 3-digit number: ")
number = int(input())
if number > 99 and number < 1000:
    firstNumber = (int)(number/100)
    secondNumber = (int)((number-firstNumber*100)/10)
    thirdNumber = (int)(number % 10)
    print("Result is: ",  firstNumber + secondNumber + thirdNumber)
else:
    print("Needed 3-digit number")


""" Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе? """


print("Please enter number of cranes: ")
cranes = int(input())

x = symbols('x')
equation = Eq(x*2 + (x+x)*2, cranes)
sol = solve(equation)

petrCranes = math.floor(sol[0])
sergCranes = petrCranes
kateCranes = petrCranes*4

shortfall = cranes - petrCranes - sergCranes - kateCranes
if shortfall != 0:
    list = [petrCranes, sergCranes+1, kateCranes+2]
    for x in range(0, shortfall):
        randomChild = random.choice(list)
        index = list.index(randomChild)
        if index == 0:
            petrCranes += 1
        if index == 1:
            sergCranes += 1
        if index == 2:
            kateCranes += 1


print("Peter made:", petrCranes, " Sergey made:",
      sergCranes, " Kate made:", kateCranes)


""" Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером,
 где сумма первых трех цифр равна сумме последних трех.Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета. """


print("Please enter ticket's number: ")
ticket = int(input())

if ticket > 100000 and ticket < 999999:
    listOfDigits = [int(x) for x in str(ticket)]
    print(listOfDigits)
    fNumber = listOfDigits[0]
    sNumber = listOfDigits[1]
    thNumber = listOfDigits[2]
    fourthNumer = listOfDigits[3]
    fifthNumber = listOfDigits[4]
    sixNumber = listOfDigits[5]

    firstHalf = fNumber+sNumber+thNumber
    secondHalf = fourthNumer+fifthNumber+sixNumber

    if firstHalf == secondHalf:
        print("Congratulations! You're lucky")
    else:
        print("Well... Try again next time")

else:
    print("It doesn't look like a ticket")


""" 
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
 если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника). """


print("Please enter horizontal side: ")
n = int(input())
print("Please enter vertical side: ")
m = int(input())
print("Please enter number of slices: ")
slices = int(input())


if m*n > slices:
    if m >= n:
        if m > slices:
            canSeparate = True
        else:
            canSeparate = False
    else:
        if n > slices:
            canSeparate = True
        else:
            canSeparate = False
else:
    canSeparate = False

if canSeparate:
    print("You can do it")
else:
    print("Sorry. It's impossible")
