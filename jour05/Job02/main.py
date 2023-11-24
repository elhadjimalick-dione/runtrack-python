def draw_rectangle(width, height):
    if width < 2 or height < 2:
        print("Les dimensions doivent être supérieures ou égales à 2.")
        return

    for i in range(height):
        line = "|" + " " * (width - 2) + "|"

        if i == 0 or i == height - 1:
            line = "|" + "-" * (width - 2) + "|"

        print(line)

draw_rectangle(10, 3)