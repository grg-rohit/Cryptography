
#Expansion P-box
import random as r

expansion_Pbox = [32, 1, 2, 3, 4, 5, 4, 5,
                  6, 7, 8, 9, 8, 9, 10, 11,
                  12, 13, 12, 13, 14, 15, 16,
                  17, 16, 17, 18, 19, 20, 21,
                  20, 21, 22, 23, 24, 25, 24,
                  25, 26, 27, 28, 29, 28, 29,
                  30, 31, 32, 1]

def setInputBlock():
    input_block = ""
    for _ in range(32):
        input_block += str(r.randint(0,1))
    return input_block

def expandInput(inputText):
    expandedText = ""
    for index in expansion_Pbox:
        expandedText += inputText[index-1]
    return expandedText

# inputText = setInputBlock()
inputText = "10100110010001100110011001100110"
expandedText = expandInput(inputText)

print("Inital input: ", inputText)

#Expansion P-box
import random as r

expansion_Pbox = [32, 1, 2, 3, 4, 5, 4, 5,
                  6, 7, 8, 9, 8, 9, 10, 11,
                  12, 13, 12, 13, 14, 15, 16,
                  17, 16, 17, 18, 19, 20, 21,
                  20, 21, 22, 23, 24, 25, 24,
                  25, 26, 27, 28, 29, 28, 29,
                  30, 31, 32, 1]

def setInputBlock():
    input_block = ""
    for _ in range(32):
        input_block += str(r.randint(0,1))
    return input_block

def expandInput(inputText):
    expandedText = ""
    for index in expansion_Pbox:
        expandedText += inputText[index-1]
    return expandedText

# inputText = setInputBlock()
inputText = "10100110010001100110011001100110"
expandedText = expandInput(inputText)

print("Inital input: ", inputText)

print("Output After Expansion: ", expandedText)