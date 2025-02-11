#!/usr/bin/python3

charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

def encrypt(message, shift, charset):
    encrypted = []
    charset_len = len(charset)
    for char in message:
        if char in charset:  
            new_index = (charset.index(char) + shift) % charset_len
            encrypted.append(charset[new_index])
        else:  
            encrypted.append(char)
    return ''.join(encrypted)

shift = ??

message = "SAMPLE_MESSAGE"

ciphertext = encrypt(message, shift, charset)

print("Encrypted message:", ciphertext)
