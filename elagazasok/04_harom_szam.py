"""
4️ Három szám közül a legnagyobb
Kérj be három egész számot, és írd ki, melyik a legnagyobb.

"""
print("Enter 3 numbers")

szam1 = float(input())
szam2 = float(input())
szam3 = float(input())


if szam1 > szam2 and szam1 > szam3 :
    print(f"{szam1} is the biggest number")
elif szam2 > szam1 and szam2 > szam3 :
    print(f"{szam2} is the biggest number")
elif szam1 == szam2 == szam3 :
    print("all 3 numbers are equal")
else :
    print(f"{szam3} is the biggest number")