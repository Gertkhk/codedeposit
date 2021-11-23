failinimi = input("Mis faili tahate parandada? ")
uusnimi = input("Mis tahate uue faili nimeks? ")

def paranda_komavead(lause):
    lause = lause.replace(" sest ", ", sest ")
    lause = lause.replace(" et ", ", et ")
    lause = lause.replace(" aga ", ", aga ")
    lause = lause.replace(" kuid ", ", kuid ")
    return lause

fail = open(failinimi)
uusfail = open(uusnimi, "w", encoding="UTF-8")
for a in fail:
    uus_lause = paranda_komavead(a)
    uusfail.write(uus_lause)
    
fail.close()    
uusfail.close()




y = paranda_komavead("Ei sest et ei aga ei kuid ei")
x = paranda_komavead("Jah et jah aga jah kuid jah sest jah")