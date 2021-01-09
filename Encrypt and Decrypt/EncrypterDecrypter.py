cypher = {"a":" = B*","b":"a3Vf","c":"B*","d":"1bHn","e":"a*(","f":"kBH7","g":"bh52","h":"aP3b","i":"a(2h","j":"pI0Ba","k":"t(A**","l":"aBeL","m":"R*(n","n":"2bA01","o":"Ar79b","p":"a5h(*","q":"((**)","r":"bw(()","s":"2jx9","t":"r94k","u":"2j0q","v":"4ja*(","w":"45nq3","x":"241(*","y":"*(y","z":"lM84"}

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
    print("Selected Decypher")
    decypherText = input("Enter text: ")
else:
    print("Unknown")