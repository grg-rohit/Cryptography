
#Sbox 1 in DES
def sbox1(input_bits):
    sbox = (
        # S-box 1
        (14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7),
        (0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8),
        (4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0),
        (15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13)
    )

    row = int(input_bits[0] * 2 + input_bits[5])
    col = int("".join(map(str, input_bits[1:5])), 2)

    output_value = sbox[row][col]
    output_bits = format(output_value, '04b')

    return [int(bit) for bit in output_bits]

# Example input: 6 bits
input_bits = [1, 0, 0, 1, 1, 1]

output_bits = sbox1(input_bits)
print("Input bits:", input_bits)

#Sbox 1 in DES
def sbox1(input_bits):
    sbox = (
        # S-box 1
        (14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7),
        (0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8),
        (4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0),
        (15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13)
    )

    row = int(input_bits[0] * 2 + input_bits[5])
    col = int("".join(map(str, input_bits[1:5])), 2)

    output_value = sbox[row][col]
    output_bits = format(output_value, '04b')

    return [int(bit) for bit in output_bits]

# Example input: 6 bits
input_bits = [1, 0, 0, 1, 1, 1]

output_bits = sbox1(input_bits)
print("Input bits:", input_bits)

print("Output bits:", output_bits)