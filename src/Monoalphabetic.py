def encrypt(plain, key):
    cipher = ''
    plain = plain.lower()
    for c in plain:
        if ord(c) - ord('a') > len(key):
            raise Exception("invalid key: characters in plain text can't be encrypted by the key.")
        cipher += key[ord(c) - ord('a')]
    return cipher


def decrypt(cipher, key):
    plain = ''
    cipher = cipher.lower()
    key = key.lower()
    for c in cipher:
        plain += chr(ord('a') + key.find(c))
    return plain
