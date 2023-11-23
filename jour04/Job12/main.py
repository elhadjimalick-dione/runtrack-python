def tri_bulles(liste):
    n = 0
    for i in liste:
        n += 1

    i = 0
    while i < n:

        j = 0
        while j < n-i-1:
            
            if liste[j] > liste[j+1]:
                
                temp = liste[j]
                liste[j] = liste[j+1]
                liste[j+1] = temp
            j += 1
        i += 1

ma_liste = [64, 34, 25, 12, 22, 11, 90]
tri_bulles(ma_liste)

print("Liste triée :", ma_liste)
