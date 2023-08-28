#Initial and Final Permutation Box demonstration

def permute(input_bits, permutation_box):
    return ''.join(input_bits[i - 1] for i in permutation_box)

# Random 64-bit input plaintext (as binary string)
input_bits = "1101010101101100110011110001111010100101001111100010110101110000"

# Initial Permutation (IP) Box
initial_permutation_box = (
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
)

# Final Permutation (FP) Box
final_permutation_box = (
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
)

# Applying Initial Permutation
permuted_bits = permute(input_bits, initial_permutation_box)
print("Permuted Bits after Initial Permutation:", permuted_bits)

# Applying Final Permutation
encrypted_output = permute(permuted_bits, final_permutation_box)
print("Encrypted Output after Final Permutation:", encrypted_output)
