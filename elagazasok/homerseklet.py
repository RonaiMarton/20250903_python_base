"""
Hőmérséklet tanács
Kérj be egy hőmérsékletet Celsiusban, és adj tanácsot:
0 alatt: „Nagyon hideg, öltözz melegen!”


0–20: „Hűvös, kabát ajánlott.”


21–30: „Kellemes idő.”


30 felett: „Forróság, igyál sok vizet!”
"""
print("enter the temperature")
temp = int(input())
if temp < 20 :
    print("It is cold, dress warmly")
elif 21 <= temp <= 30 :
    print("Nice weather")
else : 
    print("Drink a lot of water")
