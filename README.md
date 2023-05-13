# Cryptography library

this repo is based on introduction course to cryptography in my college so  i decided to share my work and add more algorithms with some documentations.

## block ciphers
### ceaser cipher

- this algorithm is the simplest and is easy to be attacked by brute force just trying all 26 possibilities. 
- the main idea is to shift the ascii value of the characters by the key.
- ![ceaser image](https://media.geeksforgeeks.org/wp-content/uploads/ceaserCipher.png)

### monoalphabetic

- instead of just shifting characters we can substitute them.
- the key works as an index of every character substitution so it should have all the characters.
- ![monoalphabetic image](https://i.ytimg.com/vi/Dz1RW_W2zGI/maxresdefault.jpg)

### playfair

- things become a bit complex so focus.
- the main idea is having a 5x5 matrix and substitute every character with another character in the matrix but in special way!
- the key should be a string.
- first step is initializing the matrix we will encrypt with.
- we put every character in the key so that we don't make any repetition (eg. bool -> b|o|l|...).
- then we but all the remaining characters in the matrix considering i and j as the same character.
- the way we encrypt is if the characters in the same row then we encrypt them to the characters beside them and if the character at the end of the row we substitute it with the first character.
- if they were in the same column we substitute them with the characters under them.
- if they were in different row and column then we substitute them with the inverse square(eg. ch1[0][1] , ch2[1][2] -> cipher1[0][2], cipher2[1][1]).
- ![playfiar image](https://media.geeksforgeeks.org/wp-content/uploads/20190818175428/encryption-of-instruments.png)