try:
    N = int(input("Veuillez saisir un entier supérieur à zéro (N) : "))
    if N <= 0:
        print("Veuillez saisir un entier supérieur à zéro.")
    else: 
         for i in range(1, N + 1):
           for j in range(1, 11):
            print(f"{i} * {j} = {i * j}")
    
except ValueError:
    print("Veuillez entrer un entier supérieur à zéro.")