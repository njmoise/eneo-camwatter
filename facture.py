
nom=["ENEO/SOCADEL","CAMWATTER"]

def calculerfacture(aindex,nindex,choixfacture,nom): 
    global location
    global consommation
    consommation=nindex-aindex
    consommation=round(consommation,2)
    global punite 
    match choixfacture:
        case 0:
            location=300
            if consommation<=110:
                punite=50
            elif consommation<=400:
                punite=79
            elif consommation<=800:
                punite=92
            else:
                punite=99
        case 1:
            location=390
            if consommation<10:
                punite=293
            else :
                punite=364   
    global montantht
    montantht=consommation*punite
    montantht=round(montantht,2)
    global tva 
    tva=montantht*0.1925
    tva=round(tva,2)
    global total 
    total=montantht+tva+location
    if total%25!=0:
        total=(total//25+1)*25
    return afficherfacture(nom)

def choisirfacture():
    print("  ==========  ","MENU","  ==========  ")
    print("0 •ENEO")
    print("1 •CAMWATTER")
    global choixfacture
    choixfacture=int(input("[0 / 1 ]??? "))

def entrerindex():
    global nindex ,aindex
    nindex=float(input("veillez saisir le nouvelle index: "))
    aindex=float(input("veillez saisir l'ancien index: "))
    while (aindex>nindex or nindex<0 or aindex<0):
        print("vous avez fait une erreur le nouvel index doit être plus grand que l'ancien veuillez recommencé!!!")
        entrerindex()

def afficherfacture(nom):
    print("  ==========  " ,nom,  "  ==========  ","\n")
    print("consommation:",nindex,"-",aindex,"=",consommation,"\n",sep="\t")
    print("montant ht:",consommation,"x",punite,"=",montantht,"\n",sep="\t")
    print("taxe ajouté:",montantht,"x","0.1925","=",tva,"\n" ,sep="\t")
    print("location :",location,"\n",sep="\t")
    print("total à payé:",montantht,"+",tva,"+",location,"=",total,"\n",sep="\t")

entrerindex()
choisirfacture()
while True:
    if choixfacture==0 or choixfacture==1:
        calculerfacture(aindex,nindex,choixfacture,nom[choixfacture])
        print("  ==========  ","SUIVANT","  ==========  ")
        entrerindex()
        choisirfacture()
    else:
        print("reéssayer encore, la valeur saisi n'est pas connue.")
        entrerindex()
        choisirfacture()
