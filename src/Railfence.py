def encrypt(plain, key):
    cipher = ""
    matrix = []
    idx = 0
    for i in range(int(key)):
        matrix.append([])
    for c in plain:
        matrix[idx].append(c)
        idx = (idx + 1) % int(key)
    for i in matrix:
        for j in i:
            cipher += j
    return cipher


def decrypt(cipher, key):
    plain = ""
    matrix = []
    idx = 0
    counter = 0
    for i in range(int(key)):
        matrix.append([])
    for c in cipher:
        if counter >= len(cipher):
            idx += 1
            counter = idx
        counter += int(key)
        matrix[idx].append(c)
    for rowElement in range((len(cipher) // key) + 1):
        for row in matrix:
            if rowElement < len(row):
                plain += row[rowElement]
    return plain
