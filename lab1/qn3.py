def vigenere_cipher(text, keyword, mode='encrypt'):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key_repeated = (keyword * (len(text) // len(keyword) + 1))[:len(text)]
    result = ''

    for i in range(len(text)):
        if text[i].upper() not in alphabet:
            result += text[i]
        else:
            text_index = alphabet.index(text[i].upper())
            key_index = alphabet.index(key_repeated[i].upper())
            if mode == 'encrypt':
                encrypted_index = (text_index + key_index) % 26
            elif mode == 'decrypt':
                encrypted_index = (text_index - key_index) % 26
            else:
                raise ValueError("Invalid mode. Use 'encrypt' or 'decrypt'.")
            result += alphabet[encrypted_index] if text[i].isupper() else alphabet[encrypted_index].lower()

    return result

# Example usage:
plaintext = "HELLO"
keyword = "KEY"
encrypted_text = vigenere_cipher(plaintext, keyword, mode='encrypt')
decrypted_text = vigenere_cipher(encrypted_text, keyword, mode='decrypt')

print("Plaintext:", plaintext)
print("Encrypted:", encrypted_text)
print
