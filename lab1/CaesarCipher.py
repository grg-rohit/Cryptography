def ceaserCyEn(plaintext, key):
    encrypt=""
    for char in plaintext:
        if char.isalpha():
            base=ord('A') if char.isupper() else ord('a')
            
            #find the position of each character
            enc_char = chr((ord(char)-base+key)%26+base)
            encrypt += enc_char
        else:
            encrypt+=char
    return encrypt

def ceaserCyDe(cipherText, key):
    return ceaserCyEn(cipherText, -key)

no = "Rohit Gurung"
key = 10

cipherText = ceaserCyEn(no, key)
print("Encrypted Text: "+cipherText)

print("Decrypted Text: "+ceaserCyDe(cipherText, key))


