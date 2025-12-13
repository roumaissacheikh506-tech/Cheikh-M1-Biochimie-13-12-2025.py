#Pendas with Cheikh Roumaissa,roumaissacheikh506-tech/Cheikh-M1-Biochimie-13-12-2025.py
# For biology Master 01 Biochimie Tlemcen...13/12/2025
# Membres de projet:-Cheikh Roumaissa 
#                  - Dif amina
#                  -Brahimi Fatima Zohra
#                  -Chikhi Rania Salsebil
#                  -Dahmani Fatima Zohra
#                  -Mohammedi Sihem

import pandas as pd

# Données: Séquences ADN,Longueur,Pourcentage de GG
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


# 2) sélectionner la colonne"Longueur" 
Longueur=df["Longueur"] 
print(Longueur," \n\n") 


# 3) Filter les séquences dont la Longueur supérieure à 10
print("****************Filtrage dont la Longueur****************")
#filtre les séquences dont la Longueur est supérieure à 10
filtred_df=df[df["Longueur"]>10]
print(filtred_df,"\n\n")


# 4) calculer la moyenne du pourcentage de GC
print("*************calculer de la moyenne*************")
#calculer la moyenne du pourcentage de GC
average_gc = df["Pourcentage_GC"].mean()
print(f"pourcentage moyenne de GC:{average_gc:.3f}%","\n\n")


# 5)Ajouter une nouvelle colonne avec des calculs
print("***********Ajoute d'une nouvelle colonne***********")
# Ajouter une nouvelle colonne "catégorie GC"
df["Catégorie_GC"] =df["Pourcentage_GC"].apply(lambda x: "Riche" if x > 55 else ("Moyen" if 45 <= x <= 55  else "Faible"))
print(df,"\n\n")


# 6)Ajouter une colonne comptant les 'G' 
df["Nombre_G"] = df["Séquence"].str.count("G")
print ("===== Nombre de G ajoutés =====")
print(df,"\n\n")


# 7)Calculer l'écart type de pourcentage_GC et de longueur
ecarttype_gc = df["Pourcentage_GC"].std()
ecarttype_long = df["Longueur"].std()

print("*****Ecart type*****")
print ("Ecart type de pourcentage_GC:",ecarttype_gc)
print("Ecart type de longueur:",ecarttype_long)
print (df,"\n\n")


# 8) Sauvegarde et chargement des données avec pandas 
#Sauvegarder le DataFrame dans un fichier csv 
df.to_csv("tableau_sequence.csv",index =False)

