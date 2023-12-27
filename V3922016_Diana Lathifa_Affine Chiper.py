#!/usr/bin/env python
# coding: utf-8

# In[1]:


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def encrypt(plaintext, key_a, key_b):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                ciphertext += chr((key_a * (ord(char) - ord('A')) + key_b) % 26 + ord('A'))
            else:
                ciphertext += chr((key_a * (ord(char) - ord('a')) + key_b) % 26 + ord('a'))
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, key_a, key_b):
    plaintext = ""
    mod_inv = mod_inverse(key_a, 26)
    if mod_inv is None:
        raise ValueError("Invalid key: key_a and 26 are not coprime")

    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                plaintext += chr((mod_inv * (ord(char) - ord('A') - key_b)) % 26 + ord('A'))
            else:
                plaintext += chr((mod_inv * (ord(char) - ord('a') - key_b)) % 26 + ord('a'))
        else:
            plaintext += char
    return plaintext

# Contoh penggunaan
plaintext = "Diana Lathifa"
key_a = 9
key_b = 17

# Enkripsi
encrypted_text = encrypt(plaintext, key_a, key_b)
print(f"Plaintext: {plaintext}")
print(f"Encrypted Text: {encrypted_text}")

# Dekripsi
decrypted_text = decrypt(encrypted_text, key_a, key_b)
print(f"Decrypted Text: {decrypted_text}")


# In[ ]:




