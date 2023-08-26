def construct_playfair_square(keyword):
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    keyword = keyword.upper().replace('J', 'I')
    key_set = set()
    playfair_square = []

    # Construct the keyword set
    for letter in keyword:
        if letter not in key_set:
            key_set.add(letter)

    # Construct the first row of the Playfair square using the keyword
    for letter in keyword:
        playfair_square.append(letter)

    # Construct the rest of the Playfair square using the remaining alphabet
    for letter in alphabet:
        if letter not in key_set:
            playfair_square.append(letter)

    return playfair_square

def preprocess_text(text):
    # Remove non-alphabetic characters and convert to uppercase
    text = ''.join(char.upper() for char in text if char.isalpha())
    # Replace 'J' with 'I'
    text = text.replace('J', 'I')
    # Separate repeated letters with 'X'
    text = ''.join(a if a != b else a + 'X' for a, b in zip(text, text[1:] + 'X'))
    return text

def find_letter_position(playfair_square, letter):
    position = playfair_square.index(letter)
    row = position // 5
    col = position % 5
    return row, col

def encrypt_playfair(plaintext, keyword):
    playfair_square = construct_playfair_square(keyword)
    plaintext = preprocess_text(plaintext)
    encrypted_text = ''

    for i in range(0, len(plaintext), 2):
        char1 = plaintext[i]
        char2 = plaintext[i + 1]

        row1, col1 = find_letter_position(playfair_square, char1)
        row2, col2 = find_letter_position(playfair_square, char2)

        if row1 == row2:
            col1 = (col1 + 1) % 5
            col2 = (col2 + 1) % 5
        elif col1 == col2:
            row1 = (row1 + 1) % 5
            row2 = (row2 + 1) % 5
        else:
            col1, col2 = col2, col1

        encrypted_text += playfair_square[row1 * 5 + col1]
        encrypted_text += playfair_square[row2 * 5 + col2]

    return encrypted_text

# Example usage:
plaintext = "Rohit"
keyword = "KEY"
encrypted_text = encrypt_playfair(plaintext, keyword)

print("Plaintext:", plaintext)
print("Keyword:", keyword)
print("Encrypted:", encrypted_text)
