folytatja = True
while folytatja :
    print("Vidd ki a szemetet")
    valasz = input("Mondjam mégegyszer? (i/n)")
    if valasz == "n" or valasz == "nem":
        folytatja = False
    elif valasz == "igen":
        print(" i vagy n betűt használj csak")
print(">>Program vége<<")