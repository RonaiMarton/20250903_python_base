"""
1️ Páros vagy páratlan?
Kérj be egy egész számot, és írd ki, hogy páros-e vagy páratlan.
2️ Pozitív, negatív vagy nulla
Kérj be egy számot, és állapítsd meg, hogy pozitív, negatív vagy nulla.
3️ Jegyosztályozás
Kérj be egy pontszámot 0–100 között, és írd ki az érdemjegyet:
0–49: Elégtelen


50–64: Elégséges


65–79: Közepes


80–89: Jó


90–100: Jeles

"""
print("Enter your score")
score = int(input())
if score <= 49 and score >= 0: 
    print("Elégséges")
elif score >= 50 and score <= 64 :
    prin("Elégséges")
elif score >= 65 and score <= 79 :
    print("Közepes")
elif score >= 80 and score <= 89 :
    print("Jó")
elif score > 100 or score < 0:
    print("Please enter a valid score")
    score
else : 
    print("Jeles")