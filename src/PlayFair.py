filler = 'x'


def pre_arrange_string(plain):
    for i in range(0, len(plain), 2):
        if i + 1 == len(plain):
            plain += filler
        if plain[i] == plain[i + 1]:
            plain = plain[:i + 1] + filler + plain[i + 1:]
    if len(plain) % 2 == 1:
        plain += filler
    return plain


def remove_filler(plain):
    newPlain = ''
    for i in range(len(plain)):
        if plain[i] != filler:
            newPlain += plain[i]
    return newPlain


class Playfair:
    def __init__(self):
        self.__matrix = []
        self.__set = set()

    def encrypt(self, plain, key):
        self.__matrix = []
        self.__set = set()
        key = key.lower()
        self.matrix_init(key)
        cipher = ''
        plain = pre_arrange_string(plain)
        for i in range(0, len(plain), 2):
            e1 = self.search_matrix(plain[i])
            e2 = self.search_matrix(plain[i + 1])
            if e1[0] == e2[0]:
                cipher += self.__matrix[e1[0]][(e1[1] + 1) % 5]
                cipher += self.__matrix[e2[0]][(e2[1] + 1) % 5]
            elif e1[1] == e2[1]:
                cipher += self.__matrix[(e1[0] + 1) % 5][e1[1]]
                cipher += self.__matrix[(e2[0] + 1) % 5][e2[1]]
            else:
                cipher += self.__matrix[e1[0]][e2[1]]
                cipher += self.__matrix[e2[0]][e1[1]]
        return cipher

    def decrypt(self, cipher, key):
        self.__matrix = []
        self.__set = set()
        self.matrix_init(key)
        plain = ''
        cipher = cipher.lower()
        for i in range(0, len(cipher), 2):
            e1 = self.search_matrix(cipher[i])
            e2 = self.search_matrix(cipher[i + 1])
            if e1[0] == e2[0]:
                plain += self.__matrix[e1[0]][(e1[1] - 1 + 5) % 5]
                plain += self.__matrix[e2[0]][(e2[1] - 1 + 5) % 5]
            elif e1[1] == e2[1]:
                plain += self.__matrix[(e1[0] - 1 + 5) % 5][e1[1]]
                plain += self.__matrix[(e2[0] - 1 + 5) % 5][e2[1]]
            else:
                plain += self.__matrix[e1[0]][e2[1]]
                plain += self.__matrix[e2[0]][e1[1]]
        plain = remove_filler(plain)
        return plain

    def matrix_init(self, key):
        arr = []
        for c in key:
            if c not in self.__set:
                self.__set.add(c)
                if c in {'i', 'j'}:
                    self.__set.add('i')
                    self.__set.add('j')
                    arr.append('i')
                else:
                    arr.append(c)
            if len(arr) == 5:
                self.__matrix.append(arr)
                arr = []
        for c in range(ord('a'), ord('z') + 1):
            c = chr(c)
            if c not in self.__set:
                self.__set.add(c)
                if c in {'i', 'j'}:
                    self.__set.add('i')
                    self.__set.add('j')
                    arr.append('i')
                else:
                    arr.append(c)
            if len(arr) == 5:
                self.__matrix.append(arr)
                arr = []
        print(self.__matrix)

    def search_matrix(self, target):
        for i in range(5):
            for j in range(5):
                if self.__matrix[i][j] == target:
                    return i, j
