nom = "PC" 
prix_unitaire = 800
quantite_stock = 1500
print(f": {prix_unitaire} euros")
print(f": {quantite_stock}")
2

print(f"pc :  {nom}")
print(f"prix_initaire : {prix_unitaire} euros")
print(f"quantité_stock : {quantite_stock}")

quantite_acheter = int(input("combien de produits achertez-vous?"))
quantite_stock -= quantite_acheter

prix_unitaire *=1.80 # augmrentation de 10%

print(f"\nNom du produit : {nom}")
print(f"Prix unitaire : {prix_unitaire} euros")
print(f"Quantité en stock : {quantite_stock}")