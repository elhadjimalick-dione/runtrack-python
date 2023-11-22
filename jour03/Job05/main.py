def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
    #éviter la division par zéro
        if num2 != 0:
            return num1 / num2
        
    elif operator == '%':
    #vérification pour éviter le modulo par zéro
        if num2 != 0:
            return num1 % num2
    
resultat = calcule(15, "+", 8)
resultat = calcule(15, "-", 8)
resultat = calcule(15, "*", 8)
resultat = calcule(15, "/", 8)
print(resultat)