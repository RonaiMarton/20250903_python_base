"""
Thonny fejlesztői környezetben készíts egy rövid programot, amely
kommentként tartalmazza a program funkciójának leírását,
konstansként tárolja PI értékét,
egy másik változóban tárolja egy kör sugarának nagyságát (cm-ben megadva),
kiszámolja és a képernyőre kiírja a kör kerületét és területét!
"""
def circle(r):
    pi = 3.14
    area = r * r * pi
    circumference = 2 * r * pi
    ar_ci = f"the area is {area} and the circumference is {circumference}" 
    return ar_ci

print(circle(5))
