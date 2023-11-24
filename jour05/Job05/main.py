def chiffrement_cesar(message, decalage):
    resultat = ""
    for lettre in message:
        if not lettre.isalpha():
            # Si le caractère n'est pas une lettre, le laisse inchangé
            resultat += lettre
            continue

        majuscule = lettre.isupper()
        # Applique le décalage en prenant en compte le dépassement
        lettre_decalee = chr((ord(lettre) - ord('A' if majuscule else 'a') + decalage) % 26 + ord('A' if majuscule else 'a'))
        resultat += lettre_decalee

    return resultat

message_original = "Bonjour, Jules César!"
decalage = 3
message_chiffre = chiffrement_cesar(message_original, decalage)
print("Message original:", message_original)
print("Message chiffré:", message_chiffre)