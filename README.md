
#Cheikh Roumaissa
#Master 01 Biochimie.... 13/12/2025
#Membres de projet:-Cheikh Roumaissa 
#                  - Dif amina
#                  -Brahimi Fatima Zohra
#                  -Chikhi Rania Salsebil
#                  -Dahmani Fatima Zohra
#                  -Mohammedi Sihem 

import pendas as pd

#Données: Séquences ADN, Longueur, Pourcentage de GG
data={
   "Séquence":["ATGCGTACGTA"," GCTAGCTAGGCC", "ATGCGCGTAAGT"," TACGATCGTA", "ATGAAAGGCTT"," CGTACGTAGC", "TTAACCGGAT"] 
   " Longueur ":[ 12,12,12,10,11,10,10]
   " Pourcentage GC":[50,66.67,58.33,40,45.45,60,50]
} 

# 1)Création d'un DataFrame(tableau pendas) 
df=pd.DataFrame(data) 
print("****************creation et affichage***************") 

#Affichage de tableau
print("Tableau des séquences ADN: ") 
print(df," \n\n") 

#Opération sur les tableau: 
print("****************operation****************") 

# 2) Afficher et sélectionner uniquement la colonne Longeur 
print("Colonne Longeur:")
print(df["Longeur"])
print(df,"\n\n")

# 3) Filter les séquences avec la longueur est supérieure à 10
print("****************Filtrage avec longeur****************")
#filtre les séquences avec la longueur supérieure à 10
filter df=df[df["longueur"]>10]
print (filtered_df,"n/n")

# 4) Calcule la moyenne du pourcentage de GC
print ("*************calcule la moyenne du pourcentage de GC*************")
# calculer la moyenne du pourcentage de GC avec 3 chiffres après la virgule 
average _ GC =df["pourcentage GC"].mean()
print(df"pourcentage moyenne GC:{average_GC:.3F}%")
print(df,"n/n")


# 5) Ajouter catégorie GC

print("============== CATEGORISATION DU GC ==============")

def categorie_gc(gc):
    if gc > 55:
        return "Riche"
    elif 45 <= gc <= 55:
        return "Moyen"
    else:
        return "Faible"

df["Catégorie_GC"] = df["Pourcentage_GC"].apply(categorie_gc)
print(df)
print("\n")


# 6)ajouter une colonne comptant les G 
df["nombre de G"]=df["sequence"].str.count("G")
print (("====6) Nombre de G ajoutés=====")
print|df;"\n"|


# 7)Calcule écart-type
std-gc=
df["Pourcentageurcentage-GC"] std() round(3)
std-long=
df["Longueur "] std() round(3)
