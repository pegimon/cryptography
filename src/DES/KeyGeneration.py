class KeyGenerator:
    __PC1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
             63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
    __PC2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47,
             55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
    __LS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    def __init__(self, key):
        self.key = bin(int(key, 16))[2:].zfill(64)

    def generate_keys(self):
        keys = []
        key0 = ''
        for e in self.__PC1:
            key0 += self.key[e - 1]
        c = []
        d = []
        c.append('')
        d.append('')
        c[0], d[0] = key0[:28], key0[28:]
        for i in range(16):
            c.append(c[i][self.__LS[i]:] + c[i][:self.__LS[i]])
            d.append(d[i][self.__LS[i]:] + d[i][:self.__LS[i]])
            keyi = c[i + 1] + d[i + 1]
            key1_48 = ''
            for e in self.__PC2:
                key1_48 += keyi[e - 1]
            keys.append(key1_48)
        return keys
