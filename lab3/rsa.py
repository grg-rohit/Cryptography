import random

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Function to calculate the greatest common divisor (GCD)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to find the modular multiplicative inverse
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Generate large prime numbers p and q
while True:
    p = random.randint(100, 500)
    if is_prime(p):
        break

while True:
    q = random.randint(100, 500)
    if is_prime(q) and q != p:
        break

# Calculate n and totient (phi)
n = p * q
phi = (p - 1) * (q - 1)

# Choose a public key exponent (e)
e = random.randint(1, phi)
while gcd(e, phi) != 1:
    e = random.randint(1, phi)

# Calculate the private key exponent (d)
d = mod_inverse(e, phi)


def encrypt(plain_text, public_key):
    n, e = public_key
    cipher_text = [(ord(char) ** e) % n for char in plain_text]
    return cipher_text

# Decryption function
def decrypt(cipher_text, private_key):
    n, d = private_key
    plain_text = ''.join([chr((char ** d) % n) for char in cipher_text])
    return plain_text

# Test the RSA encryption and decryption
message = "Hellow"
print("Original message:", message)

public_key = (n, e)
private_key = (n, d)

encrypted_message = encrypt(message, public_key)
print("Encrypted message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, private_key)
print("Decrypted message:", decrypted_message)