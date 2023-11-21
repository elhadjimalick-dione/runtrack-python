alphabet = "abcdefghijklmnopqrstuvwxyz"
o = 0
    
for i in range(1, 16):
    current_chars = alphabet[:i+o]
    o += 1
    print(current_chars)
