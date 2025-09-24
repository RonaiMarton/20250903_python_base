"""
B csoport:
Készítsünk programot, amely segíti a burkoló mesterek munkáját.
A szükséges csempe mennyiségének a kiszámításához a program kérje be a terület szélességét és a magasságát centiméterben,
valamint, hogy hány darab csempét vásároltunk már, majd számolja ki a területét (a*b), és
hogy a 20cm*20cm méretű csempék esetén hány darabra van szükség a munka elvégzéséhez (a plusz 10%-ot az illesztések miatt illik rászámolnunk).
A program azt is állapítsa meg, és közölje a felhasználóval, hogy kell-e még vásárolnunk csempét!
"""
"""
def area(szélesség, hossz):
    print("Írja be a felület szélességét és a hosszát")
    szélesség = input()
    hossz = input()
    terület = szélesség * hossz
    return terület

def anyag(csempe):
    print("Írja be mennyi csempét vett eddig")
    csempe = input()
    csempe_terulet = (20 * 20 * csempe) * 1,1
    return csempe_terulet
"""
print("Írja be a felület szélességét, hosszát és a csempék számát")
szélesség = int(input())
hossz = int(input())
csempe = int(input())
terület = szélesség * hossz
össz_csempe = terület / 400 * 1.1
kell_csempe = össz_csempe - csempe


if össz_csempe == csempe or össz_csempe < csempe :
    print("Elegendő csempéje van")
else :
    print(f"Nincs elegendő csempéje, {kell_csempe} csempe kell még")
