key = "KEY"

encrypted_text = vigenere_encrypt(plain_text, key)
print("Encrypted:", encrypted_text)

decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)