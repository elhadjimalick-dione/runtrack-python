def distance_to_toilettes(marches, hauteur_marche):
    nombre_de_jours = 7
    nombre_de_toilettes_par_jour = 5
    distance_par_allee_retour = marches * hauteur_marche * 2  

    distance_par_jour = distance_par_allee_retour * nombre_de_toilettes_par_jour
    distance_par_semaine = distance_par_jour * nombre_de_jours / 100  # Convertir en mètres

    return distance_par_semaine


marches = 20
hauteur_marche = 15

resultat = distance_to_toilettes(marches, hauteur_marche)
print(f'Pour {marches} marches de {hauteur_marche} cm, le gardien parcourt {resultat:.2f} m par semaine.')