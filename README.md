# Cryptography library

this repo is based on introduction course to cryptography in my college so  i decided to share my work and add more algorithms with some documentations.

## block ciphers
### ceaser cipher

- this algorithm is the simplest and is easy to be attacked by brute force just trying all 26 possibilities. 
- the main idea is to shift the ascii value of the characters by the key.
- ex: ('abc' key = 3) -> ('cde')

### monoalphabetic

- instead of just shifting characters we can substitute them.
- the key works as an index of every character substitution so it should have all the characters.
