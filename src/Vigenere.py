def encrypt(plain, key):
    times = len(plain) // len(key)
    key += key * (times + 1)
    key = key[0: len(plain)]
    plain = plain.lower()
    cipher = ''
    for c, c1 in zip(plain, key):
        cipher += chr((ord(c) + ord(c1) - 2 * ord('a')) % 26 + ord('a'))
    return cipher


def decrypt(cipher, key):
    times = len(cipher) // len(key)
    key += key * (times + 1)
    key = key[0: len(cipher)]
    cipher = cipher.lower()
    plain = ''
    for c, c1 in zip(cipher, key):
        plain += chr((ord(c) - ord(c1) + 26) % 26 + ord('a'))
    return plain
