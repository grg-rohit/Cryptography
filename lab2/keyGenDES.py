<<<<<<< HEAD
def generate_round_keys(key):
    # Permutation choice 1 (PC-1)
    pc1 = [
        57, 49, 41, 33, 25, 17, 9, 1,
        58, 50, 42, 34, 26, 18, 10, 2,
        59, 51, 43, 35, 27, 19, 11, 3,
        60, 52, 44, 36, 63, 55, 47, 39,
        31, 23, 15, 7, 62, 54, 46, 38,
        30, 22, 14, 6, 61, 53, 45, 37,
        29, 21, 13, 5, 28, 20, 12, 4
    ]

    # Left and right halves of the key
    left_key = key[:28]
    right_key = key[28:]

    round_keys = []

    for round_num in range(1, 17):
        # Key schedule rotation amounts
        rotations = 1 if round_num in {1, 2, 9, 16} else 2

        # Perform key rotation
        left_key = left_key[rotations:] + left_key[:rotations]
        right_key = right_key[rotations:] + right_key[:rotations]

        # Combine left and right halves
        combined_key = left_key + right_key

        # Permutation choice 2 (PC-2) to generate subkey
        pc2 = [
            14, 17, 11, 24, 1, 5, 3, 28,
            15, 6, 21, 10, 23, 19, 12, 4,
            26, 8, 16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55, 30, 40,
            51, 45, 33, 48, 44, 49, 39, 56,
            34, 53, 46, 42, 50, 36, 29, 32
        ]

        subkey = [combined_key[i - 1] for i in pc2]
        round_keys.append(subkey)

    return round_keys

# Example 64-bit key
key = [
    1,1,0,0,1,1,0,1,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,0,1,0,1,0,1,0,1,1,1,1,0,0,0,0,1,0,1,0,1,0,1,0
]

# Generate round keys
round_keys = generate_round_keys(key)

# Print the generated round keys
for i, subkey in enumerate(round_keys):
=======
def generate_round_keys(key):
    # Permutation choice 1 (PC-1)
    pc1 = [
        57, 49, 41, 33, 25, 17, 9, 1,
        58, 50, 42, 34, 26, 18, 10, 2,
        59, 51, 43, 35, 27, 19, 11, 3,
        60, 52, 44, 36, 63, 55, 47, 39,
        31, 23, 15, 7, 62, 54, 46, 38,
        30, 22, 14, 6, 61, 53, 45, 37,
        29, 21, 13, 5, 28, 20, 12, 4
    ]

    # Left and right halves of the key
    left_key = key[:28]
    right_key = key[28:]

    round_keys = []

    for round_num in range(1, 17):
        # Key schedule rotation amounts
        rotations = 1 if round_num in {1, 2, 9, 16} else 2

        # Perform key rotation
        left_key = left_key[rotations:] + left_key[:rotations]
        right_key = right_key[rotations:] + right_key[:rotations]

        # Combine left and right halves
        combined_key = left_key + right_key

        # Permutation choice 2 (PC-2) to generate subkey
        pc2 = [
            14, 17, 11, 24, 1, 5, 3, 28,
            15, 6, 21, 10, 23, 19, 12, 4,
            26, 8, 16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55, 30, 40,
            51, 45, 33, 48, 44, 49, 39, 56,
            34, 53, 46, 42, 50, 36, 29, 32
        ]

        subkey = [combined_key[i - 1] for i in pc2]
        round_keys.append(subkey)

    return round_keys

# Example 64-bit key
key = [
    1,1,0,0,1,1,0,1,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,0,1,0,1,0,1,0,1,1,1,1,0,0,0,0,1,0,1,0,1,0,1,0
]

# Generate round keys
round_keys = generate_round_keys(key)

# Print the generated round keys
for i, subkey in enumerate(round_keys):
>>>>>>> 253d83e907da27ab318871f0f4c9e73e01aba6a7
    print(f"Round {i+1} Subkey:", subkey)