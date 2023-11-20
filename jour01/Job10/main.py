montant_initial = 10000  # en euros
taux_rendement = 0.05  # 5% de rendement annuel


gain_annuel = montant_initial * taux_rendement
print(f"Gain annuel : {gain_annuel} euros")


montant_initial += 5000  # augmenter le capital de 5000 euros
taux_rendement += 0.02  # augmenter le taux de rendement de 2%

# Calculer et afficher à nouveau le gain
gain_annuel = montant_initial * taux_rendement
print(f"Gain annuel après augmentation du capital et du taux de rendement : {gain_annuel} euros")

# Retirer 10% du montant total et diminuer le rendement de 1%
montant_initial -= montant_initial * 0.10  
taux_rendement -= 0.01  

# Calculer et afficher le montant final de l'investissement
montant_final = montant_initial + montant_initial * taux_rendement
print(f"Montant final de l'investissement après retrait : {montant_final} euros")