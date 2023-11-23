# fonction pour arrondir un nombre
def custom_round(num):
    integer_part = int(num)
    decimal_part = num - integer_part
    if decimal_part >= 0.5:
        return integer_part + 1
    else:
        return integer_part
numbers = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
# Arrondir 
rounded_numbers = [custom_round(num) for num in numbers]

# Tri sans utiliser la fonction sort
n = len(rounded_numbers)
for i in range(n):
    for j in range(0, n-i-1):
        if rounded_numbers[j] > rounded_numbers[j+1]:
             # Échanger les éléments
            rounded_numbers[j], rounded_numbers[j+1] = rounded_numbers[j+1], rounded_numbers[j]

print(rounded_numbers)