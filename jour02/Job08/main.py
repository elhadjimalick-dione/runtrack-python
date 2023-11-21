def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def triangle_type(a, b, c):
    if a == b == c:
        return "Équilatéral"
    elif a == b or b == c or a == c:
        if a + b == c or a + c == b or b + c == a:
            return "Rectangle et Isocèle"
        else:
            return "Isocèle"
    elif a + b == c or a + c == b or b + c == a:
        return "Rectangle"
    else:
        return "Quelconque"

a = int(input("Entrez la longueur a : "))
b = int(input("Entrez la longueur b : "))
c = int(input("Entrez la longueur c : "))


if is_triangle(a, b, c):
    print("Les longueurs peuvent former un triangle.")
    triangle_type_result = triangle_type(a, b, c)
    print("Le triangle est de type :", triangle_type_result)
else:
    print("Les longueurs ne peuvent pas former un triangle.")