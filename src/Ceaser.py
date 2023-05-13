def encrypt(plain, key):
    cipher = ''
    plain = plain.lower()
    for c in plain:
        if c.isalpha():
            cipher += chr((ord(c) + int(key) - ord('a')) % 26 + ord('A'))
        else:
            cipher += c
    return cipher


def decrypt(cipher, key):
    plain = ''
    cipher = cipher.lower()
    for c in cipher:
        if c.isalpha():
            plain += chr((ord(c) - int(key) - ord('a') + 26) % 26 + ord('a'))
        else:
            plain += c
    return plain
