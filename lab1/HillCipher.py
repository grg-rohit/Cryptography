import numpy as np

def create_alphabet_matrix(word):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    matrix = []

    for letter in word:
        if letter in alphabet:
            value = ord(letter) - ord('a')
            matrix.append(value)

    # Pad with zeros if needed to have a multiple of 3 elements
    while len(matrix) % 3 != 0:
        matrix.append(0)

    # Reshape the matrix to be 3x2 using column-major order
    num_rows = len(matrix) // 3
    matrix = [matrix[i:i+num_rows] for i in range(0, len(matrix), num_rows)]

    return matrix
#converting my name into a matrix
word = 'rohit'

matrix = create_alphabet_matrix(word)
# Convert the list of lists to a NumPy array
numpy_array = np.array(matrix)

print(numpy_array)

#conver matrix to alphabets
def matrix_to_alphabets(matrix):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rows, cols = matrix.shape
    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            letter = alphabet[matrix[i, j]]
            row.append(letter)
        result.append(row)

    return result

#Inverse of matrix driver function
def inverse_2x2_mod(matrix):
    a, b = matrix[0, 0], matrix[0, 1]
    c, d = matrix[1, 0], matrix[1, 1]

    det = (a * d - b * c) % 26

    for i in range(1, 26):
        if (det * i) % 26 == 1:
            det_inv = i
            break

    inv_matrix = np.array([[d, -b], [-c, a]]) * det_inv
    inv_matrix = inv_matrix % 26

    return inv_matrix

#Inverse matrix
matro = np.array([[13, 3], [12, 3]])
inv_matrix = inverse_2x2_mod(matro)
print("Inverse Matrix (mod 26):\n", inv_matrix)

def multiply_matrices(matrix1, matrix2):
    result = np.dot(matrix1, matrix2) % 26
    return result

encrypt_matrix = multiply_matrices(numpy_array, matro)
print(encrypt_matrix)

decrypt_matrix = multiply_matrices(encrypt_matrix, inverse_2x2_mod(matro))
print(decrypt_matrix)

encrypted_texts = matrix_to_alphabets(encrypt_matrix)
decrypted_texts = matrix_to_alphabets(decrypt_matrix)

print(encrypted_texts)
print(decrypted_texts)