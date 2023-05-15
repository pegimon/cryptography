def encrypt(plain, key):
    cipher = ""
    matrix = []
    idx = 0
    up_down = True
    for i in range(int(key)):
        matrix.append([])
    for c in plain:
        matrix[idx].append(c)
        if idx >= key - 1:
            up_down = False
        elif idx <= 0:
            up_down = True
        if up_down:
            idx += 1
        else:
            idx -= 1
    for i in matrix:
        for j in i:
            cipher += j
    return cipher

#
# def decrypt(cipher, key):
#     plain = ""
#     matrix = []
#     arr = []
#     idx = 0
#     counter = 0
#     for i in range(int(key)):
#         matrix.append([])
#         arr.append(0)
#     for c in cipher:
#         if counter >= len(cipher):
#             idx += 1
#             counter = idx
#         counter += 2 * int(key) - 2
#         matrix[idx].append(c)
#     idx = 0
#     up_down = True
#     while len(plain) < len(cipher):
#         plain += matrix[idx][arr[idx]]
#         arr[idx] += 1
#         if idx >= key - 1:
#             up_down = False
#         elif idx <= 0:
#             up_down = True
#         if up_down:
#             idx += 1
#         else:
#             idx -= 1
#     return plain
