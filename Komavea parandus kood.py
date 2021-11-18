def paranda_komavead(lause):
    lause = lause.replace(" sest ", ", sest ")
    lause = lause.replace(" et ", ", et ")
    lause = lause.replace(" aga ", ", aga ")
    lause = lause.replace(" kuid ", ", kuid ")
    print(lause)

paranda_komavead("Ei sest et ei aga ei kuid ei")
paranda_komavead("Jah et jah aga jah kuid jah sest jah")