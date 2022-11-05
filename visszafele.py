nev = input("Helló, add meg a neved, és kiírom visszafelé!\n")
hossz = len(nev)
print("A szöveg hossza: ",hossz)
cv = hossz - 1
while (cv >= 0):
    print(nev[cv],end='')
    cv -= 1
