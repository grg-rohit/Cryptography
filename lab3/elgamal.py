import random

# Function to find the modular multiplicative inverse
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Generate ElGamal key pair
def generate_keypair(p, g):
    private_key = random.randint(2, p - 2)
    public_key = pow(g, private_key, p)
    return (public_key, private_key)

# Encrypt a message
def encrypt(public_key, g, p, message):
    k = random.randint(2, p - 2)
    c1 = pow(g, k, p)
    s = pow(public_key, k, p)
    c2 = [(s * ord(char)) % p for char in message]
    return (c1, c2)

# Decrypt a message
def decrypt(private_key, p, c1, c2):
    s = pow(c1, private_key, p)
    message = ''.join([chr((char * mod_inverse(s, p)) % p) for char in c2])
    return message

# Main program
if __name__ == '__main__':
    p = 23  # Replace with a known prime number
    g = 5   # A known primitive root modulo p
    public_key, private_key = generate_keypair(p, g)

    print("ElGamal Cryptographic System")
    print("Public Key (p, g, public_key):", (p, g, public_key))
    print("Private Key (private_key):", private_key)

    while True:
        print("\nOptions:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            message = input("Enter a message to encrypt: ")
            c1, c2 = encrypt(public_key, g, p, message)
            print("Encrypted Message:")
            print("C1:", c1)
            print("C2:", c2)
        elif choice == '2':
            c1 = int(input("Enter C1: "))
            c2 = [int(char) for char in input("Enter C2 (comma-separated): ").split(',')]
            decrypted_message = decrypt(private_key, p, c1, c2)
            print("Decrypted Message:", decrypted_message)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")
