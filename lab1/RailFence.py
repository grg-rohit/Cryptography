def encrypt_rail_fence(plaintext, rails):
    # Create an empty list for each rail
    fence = [[] for _ in range(rails)]

    # Fill the fence with the plaintext characters
    rail = 0
    direction = 1

    for char in plaintext:
        fence[rail].append(char)

        # Change direction if we reach the first or last rail
        if rail == 0 or rail == rails - 1:
            direction *= -1

        rail += direction

    # Concatenate the characters from all rails
    encrypted_text = ''.join(''.join(rail) for rail in fence)
    return encrypted_text

def decrypt_rail_fence(encrypted_text, rails):
    fence = [[] for _ in range(rails)]
    fence_length = len(encrypted_text)
    rail = 0
    direction = 1

    # Create the zigzag pattern to fill the fence
    for i in range(fence_length):
        fence[rail].append(None)
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    # Fill the fence with encrypted characters
    index = 0
    for rail in range(rails):
        for i in range(len(fence[rail])):
            fence[rail][i] = encrypted_text[index]
            index += 1

    # Read the plaintext from the zigzag pattern
    plaintext = ''
    rail = 0
    direction = 1

    for i in range(fence_length):
        plaintext += fence[rail][0]
        del fence[rail][0]

        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    return plaintext


plaintext = "Rohit"
rails = 3
encrypted_text = encrypt_rail_fence(plaintext, rails)
decrypted_text = decrypt_rail_fence(encrypted_text, rails)

print("Plaintext:", plaintext)
print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text)
