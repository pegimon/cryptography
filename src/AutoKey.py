def encrypt(plain, key):
    key += plain
    key = key[0: len(plain)]
    plain = plain.lower()
    cipher = ''
    for c, c1 in zip(plain, key):
        cipher += chr((ord(c) + ord(c1) - 2 * ord('a')) % 26 + ord('a'))
    return cipher


def decrypt(cipher, key):
    cipher = cipher.lower()
    plain = ''
    for i in range(len(cipher)):
        dec_char = chr((ord(cipher[i]) - ord(key[i]) + 26) % 26 + ord('a'))
        plain += dec_char
        key += dec_char
    return plain
