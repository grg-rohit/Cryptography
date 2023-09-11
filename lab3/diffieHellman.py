import random

# Shared prime number and base (publicly known)
p = 23  # A prime number
g = 5   # A primitive root modulo p

# Alice's private key (secret)
a_private = random.randint(1, p - 1)

# Bob's private key (secret)
b_private = random.randint(1, p - 1)

# Calculate public keys for Alice and Bob
A = (g ** a_private) % p
B = (g ** b_private) % p

# Simulate the exchange of public keys over an insecure channel

# Calculate shared secret key for Alice and Bob
jame_shared_secret = (B ** a_private) % p
bond_shared_secret = (A ** b_private) % p

# Both Alice and Bob now have the same shared secret key
print(f"Jame's shared secret key: {jame_shared_secret}")
print(f"Bond's shared secret key: {bond_shared_secret}")
