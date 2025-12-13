# Pandas with Cheikh Roumaissa,roumaissacheikh506-tech/Cheikh-M1-Biochimie-13-12-2025.py
# For biology Master 01 Biochimie Tlemcen...13/12/2025
# Membres de projet:-Cheikh Roumaissa 
#                  - Dif amina
#                  -Brahimi Fatima Zohra
#                  -Chikhi Rania Salsebil
#                  -Dahmani Fatima Zohra
#                  -Mohammedi Sihem 

import pandas as pd

# Données: Séquences ADN, Longueur, Pourcentage de GG
data={
   "Séquence":["ATGCGTACGTA","GCTAGCTAGGCC","ATGCGCGTAAGT","TACGATCGTA","ATGAAAGGCTT","CGTACGTAGC","TTAACCGGAT"], 
   "Longueur":[12,12,12,10,11,10,10],
   "Pourcentage_GC":[50,66.67,58.33,40,45.45,60,50]
} 

# 1)Création d'un DataFrame(tableau pandas) 
df=pd.DataFrame(data) 
print("****************création et affichage***************") 

# Affichage de tableau
print("Tableau des séquences ADN: ") 
print(df,"\n\n") 

# Opération sur les tableau: 
print("****************opération****************") 


# 1) sélectionner et afficher  la colonne "Longueur"
Longeur=df["Longeur"]
print(Longeur,"\n\n")


# 2) Filter les séquences dont la longueur est supérieure à 10
print("****************Filtrage dont la longueur****************")
#filtre les séquences dont la longueur est supérieure à 10
filtered_df =df[df["Longueur"]>10]
print(filtred_df)
print(df,"/n/n")


# 3) Calcule la moyenne du pourcentage de GC
print ("*************calcule de la moyenne *************")
# calculer la moyenne du pourcentage de GC 
average_GC = df["Pourcentage_GC"].mean()
print(f"Pourcentage moyen de GC : {average_GC:.3F}%")
print(df,"/n/n")


# 4) Ajouter une nouvelle colonne avec des calculs
print("***********Ajoute d'une nouvelle colonne***********")
# Ajouter une nouvelle colonne"catégorie GC"
df["Catégorie_GC"] = df["Pourcentage_GC"]. apply(lambda x: "Riche"if x> 55 else ("Moyen" if 45 <x< 55 else "Faible")
print(df,"\n\n")


# 5)Ajouter une colonne comptant les 'G' 
df["Nombre_G"] = df["Séquence"].str.count("G")
print ("===== Nombre de G ajoutés =====")
print(df,"\n\n")


# 6)Calculer l'écart-type de pourcentage_GC et de longueur ecarttype_gc=df["pourcentage GC"].
std()
ecarttype-long=df["Longueur"].print ("* PÉcartiprintPan type *****de
pourcentagert # Pa de pourcentage_GC:",# Pandas _gc)
print ("Écart type de longueur :",ecarttype_long)
print (df,"\n\n")


# 7) Sauvegarde et chargement des données avec pandas 
#Sauvegarder le DataFrame dans un fichier csv 
df.to_csv("tableau _sésuence.csv",index=False)


# 8) Sauvegarder le DataFrame dans un fichier CSV 
print ("*************  SAUVEGARDE DU FICHIER CSV *************")
 Sauvegarder le DataFrame dans un fichier csv
 Pa_fichier ="CheikhRoumaissa_M1_ Biochimie" df.# _csv("CheikhRoumaissa_M1_Biochimie.csv",index=False)
print(f"Le tableau final à été sauvegardé dans le fichier :{"CheikhRoumaissa_M1_Biochimie"} 
fichier"}")
print("\n\n") 

