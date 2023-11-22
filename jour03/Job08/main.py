def afficher_produits(type, saison):
    if type == "fruits" and saison == "hiver":
            print("orange, mandarine et kiwi")
    elif  type == "fruits" and saison == "ete":
            print("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
            print("carotte, topinambour, endive")
    elif saison == "ete":
            print("artichaut, aubergine, navet")
        
print(afficher_produits("legume", "ete"))
