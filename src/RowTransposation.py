def encrypt(plain, key):
    cipher = ''
    matrix = [[]]
    idx = 0
    for c in plain:
        if len(matrix[idx]) >= len(key):
            matrix.append([])
            idx += 1
        matrix[idx].append(c)
    while len(matrix[idx]) < len(key):
        matrix[idx].append(chr(ord('z') - (len(key) - len(matrix[idx]) - 1)))
    output = [[] for _ in range(len(key))]
    col = 0
    for num in key:
        for row in range(len(matrix)):
            output[int(num) - 1].append(matrix[row][col])
        col += 1
    for i in output:
        for j in i:
            cipher += j
    return cipher


def decrypt(cipher, key):
    pass
