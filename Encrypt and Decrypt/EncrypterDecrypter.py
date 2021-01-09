cypher = {"a":"4bB*","b":"a3Vf","c":"B3a*","d":"1bHn","e":"a*(6","f":"kBH7","g":"bh52","h":"aP3b","i":"a(2h","j":"pI0a","k":"t(A*","l":"aBeL","m":"R*(n","n":"2bA0","o":"Ar9b","p":"a5h*","q":")(*)","r":"b9a)","s":"2jx9","t":"r94k","u":"2j0q","v":"4a*(","w":"4nq3","x":"24(*","y":"*(yz","z":"lM84"}

print("Input 'c' for Cypher, and 'd' for Decypher")
cdChoice = input("Input: ")

if cdChoice.lower() == 'c':
    print("Selected Cypher")
    cypherText = input("Enter text: ")
    cypherText = cypherText.lower()

    words = cypherText.split()
    cypherWordsArr = []
    encryptedText = ""

    # Store each word in array
    for word in words:
        cypherWordsArr.append(word)

    # Encrypt Words
    for wordIndex in range(len(cypherWordsArr)):
        for alphabetIndex in range(len(cypherWordsArr[wordIndex])):
            if cypherWordsArr[wordIndex][alphabetIndex] in cypher:
                encryptedText += cypher[cypherWordsArr[wordIndex][alphabetIndex]]

        encryptedText += " "

    print(encryptedText)

elif (cdChoice.lower() == 'd'):
    print("Selected Decipher")
    decypherText = input("Paste Cryptic text: ")

    encryptedTextArr = []
    encryptedText = ""
    decryptedText = ""

    words = decypherText.split()

    # Store words in array
    for word in words:
        encryptedTextArr.append(word)

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
        decryptedText += " "

    print(decryptedText)
else:
    print("Unknown Input")