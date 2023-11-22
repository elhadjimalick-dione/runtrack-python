def verifier_pair_impair(nombre):
    
    if not isinstance(nombre, int) or nombre < 0:
        return "Le nombre doit être un entier positif."

    # pair ou impair
    if nombre % 2 == 0:
        return f"{nombre} est un nombre pair."
    else:
        return f"{nombre} est un nombre impair."

print(verifier_pair_impair(7))
print(verifier_pair_impair(2))
print(verifier_pair_impair(1))
print(verifier_pair_impair(-5))
print(verifier_pair_impair(10.3))