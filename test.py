# 1. Напишите программу которая на вход принимает 2 числа, 
# и проверяет является ли одно число квадратом другого

n = int(input("число 1: "))
m = int(input("число 2: "))

if n == m ** 2 or m == n ** 2:
    print("yes")
else:
    print("no")

