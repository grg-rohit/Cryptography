def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    key_length = len(key)
    
    for i in range(len(plain_text)):
        char = plain_text[i]
        key_char = key[i % key_length]
        
        if char.isalpha():
            shift = ord(key_char.lower()) - ord('a')
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted_char = char
        
        encrypted_text += encrypted_char
    
    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    key_length = len(key)
    
    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        key_char = key[i % key_length]
        
        if char.isalpha():
            shift = ord(key_char.lower()) - ord('a')
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            decrypted_char = char
        
        decrypted_text += decrypted_char
    
    return decrypted_text

if __name__ == '__main__':
    plain_text = "Rohit"
    key = "KEY"
    
    encrypted_text = vigenere_encrypt(plain_text, key)
    print("Encrypted:", encrypted_text)
    
    decrypted_text = vigenere_decrypt(encrypted_text, key)
    print("Decrypted:", decrypted_text)
