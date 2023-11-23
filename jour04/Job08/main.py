def sum_of_even_numbers(lst):
    somme_paires = 0
    for i in lst:
        if i % 2 == 0:
            somme_paires += i
    return somme_paires
L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

result = sum_of_even_numbers(L)
print(result)