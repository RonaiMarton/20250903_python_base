"""
Készíts egy rövid programot, amely 1 és 3 között generál véletlenszámot, majd összehasonlítja ezt a felhasználó által megadott, szintén ebbe a tartományba eső számmal!
Az összehasonlítás eredményéről tájékoztassa a felhasználót!

"""
import random
szam = random.randint(1,3)
print("enter a number between 1 and 3")
num = int(input())
if num > szam :
    print(f"{num} is bigger than {szam}")
elif num == szam :
    print(f"{num} is equal to {szam}")
else :
    print(f"{num} is smaller than {szam}")