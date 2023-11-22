def determiner_type_developpeur(langage):
    if langage == "JavaScript":
        print("Tu es un développeur web")
    elif langage == "python":
        print("Tu es un développeur IA")
    elif langage == "java":
        print("Tu es un développeur logiciel")
    elif langage == "reactjs":
        print("Tu es un développeur mobile")

langage_utilisateur = input("Entrez votre langage de programmation : ")
determiner_type_developpeur(langage_utilisateur)