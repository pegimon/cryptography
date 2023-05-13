def encrypt(plain, key):
    cipher = ''
    plain = plain.lower()
    for c in plain:
        if ord(c) - ord('a') > len(key):
            raise Exception("invalid key: characters in plain text can't be encrypted by the key.")
        if c.isalpha():
            cipher += key[ord(c) - ord('a')]
        else:
            cipher += c
    return cipher


def decrypt(cipher, key):
    plain = ''
    cipher = cipher.lower()
    key = key.lower()
    for c in cipher:
        if c.isalpha():
            plain += chr(ord('a') + key.find(c))
        else:
            plain += c
    return plain
