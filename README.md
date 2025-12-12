# Pandas with Cheikh Roumaissa
# For biology Master 01 Biochimie Tlemcen...13/12/2025
# Membres de projet:-Cheikh Roumaissa 
#                  - Dif amina
#                  -Brahimi Fatima Zohra
#                  -Chikhi Rania Salsebil
#                  -Dahmani Fatima Zohra
#                  -Mohammedi Sihem 

import pendas as pd

# Données: Séquences ADN, Longueur, Pourcentage de GG
data={
   "Séquence":["ATGCGTACGTA"," GCTAGCTAGGCC", "ATGCGCGTAAGT"," TACGATCGTA", "ATGAAAGGCTT"," CGTACGTAGC", "TTAACCGGAT"] 
   " Longueur ":[ 12,12,12,10,11,10,10]
   " Pourcentage GC":[50,66.67,58.33,40,45.45,60,50]
} 

# 1)Création d'un DataFrame(tableau pandas) 
df=pd.DataFrame(data) 
print("****************création et affichage***************") 

# Affichage de tableau
print("Tableau des séquences ADN: ") 
print(df,"\n\n") 

# Opération sur les tableau: 
print("****************opération****************") 


# 1) sélectionner de la colonne "Longeur"
Longueur=df["Longueur"]
print(longeur,"\n\n")


# 2) Filter les séquences dont la longueur est supérieure à 10
print("****************Filtrage dont la longeur****************")
#filtre les séquences dont la longueur supérieure à 10
filter-df=df[df["longueur"]>10]
print (filtered_df,"\n\n")


# 3) Calcule la moyenne du pourcentage de GC
print ("*************calcule de la moyenne *************")
# calculer la moyenne du pourcentage de GC 
average _ GC =df["pourcentage GC"].mean()
print(df"pourcentage moyenne de GC:{average_GC:.3F}%","\n\n")


# 4) Ajouter une nouvelle colonne avec des calculs
print("***********Ajoute d'une nouvelle colonne***********")
# Ajouter une nouvelle colonne"catégorie GC"
df["Pourcentage GC"].apply(lambda x:"Riche"if x>55 else "Moyen"if 45<x<55 else "Faible")
print(df,"\n\n")
   

# 5)Ajouter une colonne comptant les 'G' 
df["Nombre de G"]=df["Séquence"].str.count("G")
print ("===== Nombre de G ajoutés =====")
print(df,"\n\n")


# 6)Calculer l'écart-type de pourcentage GC et de longueur écarttype_gc=df["pourcentage GC"].
std()
écarttype-long=df["Longueur"].std()
std-long=
df["Longueur "] std() round(3)
print("Écart-type de %GC :",std_gc)
print ("Écart-type de la longueur:",std_long)
print ("\n")

# 8) Sauvegarder le DataFrame dans un fichier CSV 
print ("*************  SAUVEGARDE DU FICHIER CSV *************")
 Sauvegarder le DataFrame dans un fichier csv
nom_fichier ="CheikhRoumaissa_M1 Biochimie" df.to_csv("CheikhRoumaissa_M1 Biochimie.csv",index=False)
Print(f"Le tableau final à été sauvegardé dans le fichier :{CheikhRoumaissa_M1 Biochimie"}")
Print("\n\n") 

