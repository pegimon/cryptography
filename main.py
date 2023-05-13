from src import Monoalphabetic, Ceaser
from src.PlayFair import Playfair

if __name__ == '__main__':
    print(Ceaser.encrypt("ABC", 2))
    print(Ceaser.decrypt('bcd', 1))
    print(Monoalphabetic.encrypt("bba", 'BCA'))
    print(Monoalphabetic.decrypt('CCB', 'bca'))
    p = Playfair()
    cipher = p.encrypt("ball", "monarchy")
    print(p.decrypt(cipher, "monarchy"))
