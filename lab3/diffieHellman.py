import random

# Shared prime number and base (publicly known)
p = 23  # A prime number
g = 5   # A primitive root modulo p

# Jamess's private key (secret)
a_private = random.randint(1, p - 1)

# Bond's private key (secret)
b_private = random.randint(1, p - 1)

# Calculate public keys for James and Bond
A = (g ** a_private) % p
B = (g ** b_private) % p

# Simulate the exchange of public keys over an insecure channel

# Calculate shared secret key for James and Bond
James_shared_secret = (B ** a_private) % p
bond_shared_secret = (A ** b_private) % p

# Both James and Bond now have the same shared secret key
print(f"James's shared secret key: {James_shared_secret}")
print(f"Bond's shared secret key: {bond_shared_secret}")
