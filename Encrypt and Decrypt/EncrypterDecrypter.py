cypher = {"a":"4bB*","b":"a3Vf","c":"B3a*","d":"1bHn","e":"a*(6","f":"kBH7","g":"bh52","h":"aP3b","i":"a(2h","j":"pI0a","k":"t(A*","l":"aBeL","m":"R*(n","n":"2bA0","o":"Ar9b","p":"a5h*","q":")(*)","r":"b9a)","s":"2jx9","t":"r94k","u":"2j0q","v":"4a*(","w":"4nq3","x":"24(*","y":"*(yz","z":"lM84"}
specialChar = ['!', '?', ',', '&', "'", '"']

print("Input 'c' for Cypher, and 'd' for Decypher")
cdChoice = input("Input: ")

if cdChoice.lower() == 'c':
    print("Selected Cypher, () CANNOT BE USED IN YOUR CYPHER TEXT")
    cypherText = input("Enter text: ")
    cypherText = cypherText.lower()

    words = cypherText.split()
    cypherWordsArr = []
    encryptedText = ""
    positionOfSpecialChar = {}

    # Store each word in array
    for word in words:
        cypherWordsArr.append(word)
        # Check for Special Characters
        for i in range(len(specialChar)):
            for a in range(len(cypherWordsArr)):
                if specialChar[i] in cypherWordsArr[a]:
                    positionOfSpecialChar[cypherWordsArr[a].find(specialChar[i])*4] = specialChar[i] # Times 4 because each alphabet encrypted is 4 letters long

    # Encrypt Words
    for wordIndex in range(len(cypherWordsArr)):
        for alphabetIndex in range(len(cypherWordsArr[wordIndex])):
            if cypherWordsArr[wordIndex][alphabetIndex] in cypher:
                encryptedText += cypher[cypherWordsArr[wordIndex][alphabetIndex]]

        encryptedText += " "

    encryptedText = encryptedText + "\b"

    # Check for Special Char
    if not positionOfSpecialChar:
        print("No Special Characters")
    else:
        positions = list(positionOfSpecialChar.keys())
        symbols = list(positionOfSpecialChar.values())
        lengthEncryptedText = len(encryptedText)

        if len(positionOfSpecialChar) == 1:
            encryptedText = encryptedText[:positions[0]] + symbols[0] + encryptedText[lengthEncryptedText:]
        else:
            for i in range(len(positionOfSpecialChar)):
                print(len(positionOfSpecialChar))
                encryptedText = encryptedText[:positions[i]] + symbols[i] + encryptedText[lengthEncryptedText - i:]

    print("Cipher Text: "+encryptedText)

elif cdChoice.lower() == 'd':
    print("Selected Decipher")
    decypherText = input("Paste Cryptic text: ")

    encryptedTextArr = []
    positionOfSpecialChar = {}
    encryptedText = ""
    decryptedText = ""

    words = decypherText.split()

    # Store words in array
    for word in words:
        encryptedTextArr.append(word)
        # Check for Special Characters
        for i in range(len(specialChar)):
            for a in range(len(encryptedTextArr)):
                if specialChar[i] in encryptedTextArr[a]:
                    positionOfSpecialChar[encryptedTextArr[a].find(specialChar[i])] = specialChar[i] # Times 4 because each alphabet encrypted is 4 letters long

    # Decrypt
    ## Explaination
    ### Because each alphabet represents a 4 letter alphanumeric code, we will split the word after every 4 letters
    for wordIndex in range(len(encryptedTextArr)):
        endIndex = 4
        startIndex = 0
        for codeIndex in range(len(encryptedTextArr[wordIndex])):
            alphabetCode = encryptedTextArr[wordIndex][startIndex:endIndex]
            startIndex += 4
            endIndex += 4

            if alphabetCode in cypher.values():
                cypherValues = list(cypher.values())
                cypherKey = list(cypher.keys())

                decrypt = cypherValues.index(alphabetCode)
                decryptedText += cypherKey[decrypt]
            elif alphabetCode in specialChar:
                positionOfSpecialChar[i] = alphabetCode
        decryptedText += " "

    decryptedText = decryptedText + "\b"

    # Check for Special Char
    if not positionOfSpecialChar:
        print("No Special Characters")
    else:
        positions = list(positionOfSpecialChar.keys())
        symbols = list(positionOfSpecialChar.values())
        lengthEncryptedText = len(encryptedText)

        if len(positionOfSpecialChar) == 1:
            position = int((positions[0]/4))
            encryptedText = encryptedText[:position] + symbols[0] + encryptedText[lengthEncryptedText - 0:]
        else:
            for i in range(len(positionOfSpecialChar)):
                position = int(positions[i]/4)
                encryptedText = encryptedText[:position] + symbols[i] + encryptedText[lengthEncryptedText - i:]

    print(decryptedText)
else:
    print("Unknown Input")