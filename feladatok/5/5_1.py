"""
Írj egy programot, amely kiírja a páros számokat 1 és 10 között!
"""
num = 0
while num % 2 == 0 and num <= 10:
    print(num)
    num = num + 2
print("these are the even numbers from 1 to 10")