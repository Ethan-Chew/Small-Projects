hashedTable = {
    "Ethan": ""
}
didUserSelectChoice = False
userChoice = ""

print("Welcome to this useless system.")

while didUserSelectChoice == False:
    userChoiceInput = input("Enter '1' to Login, and '2' to Create a New Account.")

    if userChoiceInput == "1":
        userChoice = "Login"
        didUserSelectChoice = True
        break
    elif userChoiceInput == "2":
        userChoice = "New Account"
        didUserSelectChoice = True
        break
    else:
        print("Unknown Choice. Please try again.")
        didUserSelectChoice = False

def login():
    usernameInput = input("Username: ")
    passwordInput = hash(input("Password: "))

    if usernameInput in hashedTable.keys():
        hashedPassword = hashedTable[usernameInput]

        if hashedPassword == passwordInput:
            didUserLogout = False
            print("Welcome to the Useless System, " + usernameInput)

            while didUserLogout == False:
                userLogoutInput = input("Enter 'Logout' at anytime to logout.")

                if userLogoutInput.lower() == "logout":
                    logoutConfirmation = input("Are you sure you want to logout? Enter 'y' or 'n'.")

                    if logoutConfirmation.lower() == "y":
                        print("Logout Confirmed.")

                        didUserLogin = False
                        break
                    else:
                        print("Okay, no Logout today.")

            didUserLogin = True
        else:
            print("Incorrect Username or Password. Please try again")
            didUserLogin = False

    else:
        print("Incorrect Username or Password. Please try again.")
        didUserLogin = False

if userChoice == "Login":
    didUserLogin = False

    while didUserLogin == False:
        login()

elif userChoice == "New Account":
    didUserCreateAccount = False

    while didUserCreateAccount == False:
        print("Create a new account!")
        isUsernameTaken = False;
        createdUsernameInput = input("Username: ")

        if createdUsernameInput in hashedTable.keys():
            print("Username Taken. Please try again.")
            isUsernameTaken = True

        while isUsernameTaken == False and didUserCreateAccount == False:
            createdPasswordInput1 = input("Password: ")

            if len(createdPasswordInput1) <= 8:
                print("Password is too short! Enter a longer password with more than 8 Characters.")
            else:
                createdPasswordInput1 = hash(createdPasswordInput1)
                createdPasswordInput2 = hash(input("Renter Password: "))

                if createdPasswordInput1 == createdPasswordInput2:
                    userPassword = createdPasswordInput2
                    hashedTable[createdUsernameInput] = userPassword
                    didUserCreateAccount = True
                    print("Successfully Created Account! You may now login")
                    break
                else:
                    print("Passwords do not match! Renter both passwords again.")

if didUserCreateAccount == True:
    didUserLogin = False

    while didUserLogin == False:
        login()