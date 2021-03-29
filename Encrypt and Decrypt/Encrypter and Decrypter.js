const choice = prompt("Enter 'e' for Encrypt, and 'd' for Decrypt: ")

if (choice === "e") {
    encryptText()
} else if (choice === "d") {
    decryptText()
} else {
    console.log("Invalid")
}

function encryptText() {
    const cypher = {"a":"4bB*","b":"a3Vf","c":"B3a*","d":"1bHn","e":"a*(6","f":"kBH7","g":"bh52","h":"aP3b","i":"a(2h","j":"pI0a","k":"t(A*","l":"aBeL","m":"R*(n","n":"2bA0","o":"Ar9b","p":"a5h*","q":")(*)","r":"b9a)","s":"2jx9","t":"r94k","u":"2j0q","v":"4a*(","w":"4nq3","x":"24(*","y":"*(yz","z":"lM84"}
    const textToEncrypt = prompt("Text to Encrypt: ")
    var splittedText = textToEncrypt.split(" ")
    var encryptedText = ""

    for (var i; i < splittedText.length; i++) {
        for (var j; j < splittedText[i].length; j++) {
            if (splittedText[i][j] in cipher) {
                encryptedText += cipher[splittedText[i][j]]
            }
        }
    }
    console.log(encryptedText)
}

function decryptText() {
    const cypher = {"a":"4bB*","b":"a3Vf","c":"B3a*","d":"1bHn","e":"a*(6","f":"kBH7","g":"bh52","h":"aP3b","i":"a(2h","j":"pI0a","k":"t(A*","l":"aBeL","m":"R*(n","n":"2bA0","o":"Ar9b","p":"a5h*","q":")(*)","r":"b9a)","s":"2jx9","t":"r94k","u":"2j0q","v":"4a*(","w":"4nq3","x":"24(*","y":"*(yz","z":"lM84"}
    const textToDecrypt = prompt("Text to Decrypt: ")
    var splittedText = textToDecrypt.split(" ")
    var decryptedText = ""

    for (var i; i < splittedText.length; i++) {
        const currentWord = splittedText[i]
        const lastIndex = splittedText[i].length
        var index = 0
        var endIndex = 5
        for (var j; j < (splittedText[i].length)/4; j++) {
            // Get 4 Letter Code
            const currentLetter = currentWord.slice(index, endIndex)

            // Check Corr Code
            const values = Object.values(cypher)
            const keys = Object.keys(cypher)

            const temp = values.index(currentLetter)
            decryptedText += keys[temp]

            index += 4
        }
        decryptedText += " "
    }
    console.log(decryptedText)
}