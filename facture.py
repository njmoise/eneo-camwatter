
location=[300,390]
unite=[92,293]
def afficherfacture(nom):
    print("  ==========  " ,nom,  "  ==========  ","\n")
    print("consommation:",nindex,"-",aindex,"=",consommation,"\n")
    print("montant ht:",consommation,"x",unite[choixfacture],"=",montantht,"\n")
    print("tva:",montantht,"x","0.1925","=",tva,"\n")
    print("location compteur:",location[choixfacture],"\n")
    print("total:",montantht,"+",tva,"+",location[choixfacture],"=",total,"\n")

def calculerfacture(aindex,nindex,unite,location,nom):
    global consommation
    consommation=nindex-aindex
    global montantht
    montantht=consommation*unite
    global tva 
    tva=montantht*0.1925
    if tva%1!=0:
        tva=(tva//1)+1
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

entrerindex()
while nindex<aindex:
    print("vous avez fait une erreur le nouvel index doit être plus grand que l'ancien veuillez recommencé!!!")
    choisirfacture()
choisirfacture()
while choixfacture==0 or choixfacture==1:
    if choixfacture==0:
        calculerfacture(aindex,nindex,unite[choixfacture],location[choixfacture],"ENEO")
        print("  ==========  ","SUIVANT","  ==========  ")
        entrerindex()
        choisirfacture()
    elif choixfacture==1:
        calculerfacture(aindex,nindex,unite[choixfacture],location[choixfacture],"CAMWATTER")
        print("  ==========  ","SUIVANT","  ==========  ")
        entrerindex()
        choisirfacture()
    else:
        print("reéssayer encore, la valeur saisi n'est pas connu.")
        entrerindex()
        choisirfacture()

