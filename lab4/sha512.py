

# Initialize the message schedule
Message = [0] * 80

# Stores the hexadecimal values for calculating hash values
Constants = [
    0x428a2f98d728ae22, 0x7137449123ef65cd,
    0xb5c0fbcfec4d3b2f, 0xe9b5dba58189dbbc,
    0x3956c25bf348b538, 0x59f111f1b605d019,
    0x923f82a4af194f9b, 0xab1c5ed5da6d8118,
    0xd807aa98a3030242, 0x12835b0145706fbe,
    0x243185be4ee4b28c, 0x550c7dc3d5ffb4e2,
    0x72be5d74f27b896f, 0x80deb1fe3b1696b1,
    0x9bdc06a725c71235, 0xc19bf174cf692694,
    0xe49b69c19ef14ad2, 0xefbe4786384f25e3,
    0x0fc19dc68b8cd5b5, 0x240ca1cc77ac9c65,
    0x2de92c6f592b0275, 0x4a7484aa6ea6e483,
    0x5cb0a9dcbd41fbd4, 0x76f988da831153b5,
    0x983e5152ee66dfab, 0xa831c66d2db43210,
    0xb00327c898fb213f, 0xbf597fc7beef0ee4,
    0xc6e00bf33da88fc2, 0xd5a79147930aa725,
    0x06ca6351e003826f, 0x142929670a0e6e70,
    0x27b70a8546d22ffc, 0x2e1b21385c26c926,
    0x4d2c6dfc5ac42aed, 0x53380d139d95b3df,
    0x650a73548baf63de, 0x766a0abb3c77b2a8,
    0x81c2c92e47edaee6, 0x92722c851482353b,
    0xa2bfe8a14cf10364, 0xa81a664bbc423001,
    0xc24b8b70d0f89791, 0xc76c51a30654be30,
    0xd192e819d6ef5218, 0xd69906245565a910,
    0xf40e35855771202a, 0x106aa07032bbd1b8,
    0x19a4c116b8d2d0c8, 0x1e376c085141ab53,
    0x2748774cdf8eeb99, 0x34b0bcb5e19b48a8,
    0x391c0cb3c5c95a63, 0x4ed8aa4ae3418acb,
    0x5b9cca4f7763e373, 0x682e6ff3d6b2b8a3,
    0x748f82ee5defb2fc, 0x78a5636f43172f60,
    0x84c87814a1f0ab72, 0x8cc702081a6439ec,
    0x90befffa23631e28, 0xa4506cebde82bde9,
    0xbef9a3f7b2c67915, 0xc67178f2e372532b,
    0xca273eceea26619c, 0xd186b8c721c0c207,
    0xeada7dd6cde0eb1e, 0xf57d4f7fee6ed178,
    0x06f067aa72176fba, 0x0a637dc5a2c898a6,
    0x113f9804bef90dae, 0x1b710b35131c471b,
    0x28db77f523047d84, 0x32caab7b40c72493,
    0x3c9ebe0a15c9bebc, 0x431d67c49c100d4c,
    0x4cc5d4becb3e42b6, 0x597f299cfc657e2a,
    0x5fcb6fab3ad6faec, 0x6c44198c4a475817,
]

# Function to convert a binary string to hexa-decimal value
def gethex(bin):
    hex_map = {
        "0000": "0", "0001": "1", "0010": "2", "0011": "3",
        "0100": "4", "0101": "5", "0110": "6", "0111": "7",
        "1000": "8", "1001": "9", "1010": "a", "1011": "b",
        "1100": "c", "1101": "d", "1110": "e", "1111": "f",
    }
    return hex_map.get(bin, "")

# Function to convert a decimal value to hexa decimal value
def decimaltohex(deci):
    hexstring = ""
    EQBIN = format(deci, '064b')
    for i in range(0, len(EQBIN), 4):
        temp = EQBIN[i:i+4]
        hexstring += gethex(temp)
    return hexstring

# Function to convert a binary string to decimal value
def BintoDec(bin_str):
    return int(bin_str, 2)

# Function to right rotate x by n bits
def rotate_right(x, n):
    return (x >> n) | (x << (64 - n))

# Function to right shift x by n bits
def shift_right(x, n):
    return (x >> n)

# Function to divide the string into chunks
def separator(getBlock):
    chunknum = 0
    for i in range(0, len(getBlock), 64):
        Message[chunknum] = BintoDec(getBlock[i:i+64])
        chunknum += 1
    for g in range(16, 80):
        WordA = rotate_right(Message[g - 2], 19) ^ rotate_right(Message[g - 2], 61) ^ shift_right(Message[g - 2], 6)
        WordB = Message[g - 7]
        WordC = rotate_right(Message[g - 15], 1) ^ rotate_right(Message[g - 15], 8) ^ shift_right(Message[g - 15], 7)
        WordD = Message[g - 16]
        T = WordA + WordB + WordC + WordD
        Message[g] = T

# Function to find the major of a, b, c
def maj(a, b, c):
    return (a & b) ^ (b & c) ^ (c & a)

# Function to find the ch value of a, b, and c
def Ch(e, f, g):
    return (e & f) ^ (~e & g)

# Function to find the Bitwise XOR with the right rotate over 14, 18, and 41
def sigmaE(e):
    return rotate_right(e, 14) ^ rotate_right(e, 18) ^ rotate_right(e, 41)

# Function to find the Bitwise XOR with the right rotate over 28, 34, and 39
def sigmaA(a):
    return rotate_right(a, 28) ^ rotate_right(a, 34) ^ rotate_right(a, 39)

# Function to generate the hash code
def Func(a, b, c, d, e, f, g, h, K):
    T1 = h + Ch(e, f, g) + sigmaE(e) + Message[K] + Constants[K]
    T2 = sigmaA(a) + maj(a, b, c)
    d = d + T1
    h = T1 + T2

# Function to convert the hash value of a given string
def SHA512(myString):
    A = 0x6a09e667f3bcc908
    B = 0xbb67ae8584caa73b
    C = 0x3c6ef372fe94f82b
    D = 0xa54ff53a5f1d36f1
    E = 0x510e527fade682d1
    F = 0x9b05688c2b3e6c1f
    G = 0x1f83d9abfb41bd6b
    H = 0x5be0cd19137e2179
    AA, BB, CC, DD, EE, FF, GG, HH = A, B, C, D, E, F, G, H

    fixedstream = ""

    for char in myString:
        fixedstream += format(ord(char), '08b')

    s1024 = fixedstream
    orilen = len(s1024)
    modded = orilen % 1024
    tobeadded = 1024 - modded if 1024 - modded >= 128 else 2048 - modded

    s1024 += '1'
    s1024 += '0' * (tobeadded - 129)
    lengthbits = format(orilen, '0128b')
    s1024 += lengthbits

    blocksnumber = len(s1024) // 1024
    chunknum = 0
    Blocks = ["" for _ in range(blocksnumber)]

    for i in range(0, len(s1024), 1024):
        Blocks[chunknum] = s1024[i:i+1024]
        chunknum += 1

    for letsgo in range(blocksnumber):
        separator(Blocks[letsgo])
        A, B, C, D, E, F, G, H = AA, BB, CC, DD, EE, FF, GG, HH
        count = 0

        for _ in range(10):
            Func(A, B, C, D, E, F, G, H, count)
            count += 1
            Func(H, A, B, C, D, E, F, G, count)
            count += 1
            Func(G, H, A, B, C, D, E, F, count)
            count += 1
            Func(F, G, H, A, B, C, D, E, count)
            count += 1
            Func(E, F, G, H, A, B, C, D, count)
            count += 1
            Func(D, E, F, G, H, A, B, C, count)
            count += 1
            Func(C, D, E, F, G, H, A, B, count)
            count += 1
            Func(B, C, D, E, F, G, H, A, count)

        A += AA
        B += BB
        C += CC
        D += DD
        E += EE
        F += FF
        G += GG
        H += HH

    output = ""
    output += decimaltohex(A)
    output += decimaltohex(B)
    output += decimaltohex(C)
    output += decimaltohex(D)
    output += decimaltohex(E)
    output += decimaltohex(F)
    output += decimaltohex(G)
    output += decimaltohex(H)

    return output

# Driver Code

S = input("Enter message: ")
result=SHA512(S)
print("\nAfter Hashing\n----------")
print(S + ": " + result)

    
