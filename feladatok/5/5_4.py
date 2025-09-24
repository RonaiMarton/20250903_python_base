"""
Írj egy programot, amely a felhasználó által meghatározott alkalommal írja ki a bekért szöveget!
"""
want = False
while want == False :
    anwear = input("do you want to print the text? (y/n)")
    if anwear == "y":
        print("this is the text")
        want = True