"""
A program a pénzfeldobást modellezi. Kérdezze meg a felhasználótól a választását (fej vagy írás), majd adjon tájékoztatást, hogy eltalálta-e!
"""
import random
print("enter heads or tails")
coin = input()
num = random.randint(1,2)
if num == 1 and coin == "heads":
    print("you've won")
elif num == 2 and coin == "tails":
    print("you've won")
else :
    print("you've lost")