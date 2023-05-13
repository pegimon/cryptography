def encrypt(plain, key):
    cipher = ''
    plain = plain.lower()
    for c in plain:
        cipher += chr((ord(c) + int(key) - ord('a')) % 26 + ord('A'))
    return cipher


def decrypt(cipher, key):
    plain = ''
    cipher = cipher.lower()
    for c in cipher:
        plain += chr((ord(c) - int(key) - ord('a') + 26) % 26 + ord('a'))
    return plain
