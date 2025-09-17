# szam = int(input("Enter a number"))
# if szam < 0 :
#     print("Negative")
# elif szam > 0 :
#     print("Pozitive")
# else :
#     print("Nulla")
print("Enter a number")
szam = int(input())

if szam % 2 == 0 and szam != 0 :
    print("Páros")
elif szam == 0 : 
    print("Nulla")
else : print("Páratlan")