def arrondir_notes(liste_notes):
    notes_arrondies = []

    for note in liste_notes:
        if note < 40:
            notes_arrondies.append(note)
        elif (note % 5) >= 3:
            notes_arrondies.append((note // 5 + 1) * 5)

    return notes_arrondies


notes_eleves = [37, 82, 56, 91, 68]
notes_arrondies = arrondir_notes(notes_eleves)
print(notes_arrondies)