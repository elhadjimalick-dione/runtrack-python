def draw_triangle(height):
    if height < 1:
        print("La hauteur doit être supérieure ou égale à 1.")
        return

    for i in range(height):
        spaces = " " * (height - i - 1)

        if i == 0:
            print(spaces + "_")
        elif 0 < i < height - 1:
            print(spaces + "/" + " " * (2 * i - 1) + "\\")
        elif i == height - 1:
            print(spaces + "/" + "_" * (2 * i - 1) + "\\")

hauteur = int(input("Entrez la hauteur du triangle : "))
draw_triangle(hauteur)