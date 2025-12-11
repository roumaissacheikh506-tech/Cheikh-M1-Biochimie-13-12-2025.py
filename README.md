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

# 1-Création d'un DataFrame(tableau pendas) 
df=pd.DataFrame(data) 
print("****************creation et affichage***************") 

#Affichage de tableau
print("Tableau des séquences ADN: ") 
print(df," \n\n") 

#Opération sur les tableau: 
print("****************operation****************") 





