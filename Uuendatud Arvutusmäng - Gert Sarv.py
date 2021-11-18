from random import randint
num = randint(1,10)
numm = randint(1,10)
nummm = randint(1,2)
tehevalik = ""
õigevastus = ()
if nummm == 1:
    tehevalik = "x"
else:
    tehevalik = "+"

if tehevalik == "x":   
    õigevastus = int(num*numm)
else:
    õigevastus = int(num+numm)
    
vastus = int(input("Kui palju on " + str(num) + tehevalik + str(numm) + "? "))
vale = 0
while vastus != õigevastus:
    print("Vale vastus. Proovi uuesti. >:(")
    num = randint(1,10)
    numm = randint(1,10)
    nummm = randint(1,2)
    if nummm == 1:
        tehevalik = "x"
    else:
        tehevalik = "+"
    vastus = int(input("Kui palju on " + str(num) + tehevalik + str(numm) + "? "))
    if vastus != õigevastus:
        vale += 1
     
    if tehevalik == "x":   
        õigevastus = int(num*numm)
    else:
        õigevastus = int(num+numm)
    
else:
    if vale == 0:
        print("Õige. Hästi tehtud! :)")
    else:
        print("Õige!" + " Vastasid " + str(vale) + " korda valesti. :)")
