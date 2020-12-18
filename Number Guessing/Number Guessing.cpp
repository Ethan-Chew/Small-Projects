#include <iostream>
#include <cstdlib>
using namespace std;

class myClass {
public:
    int max, ans;
};

int main() {

    myClass myClass;

    bool isMaxNotNum = true;
    int tries = 0;
    bool correctGuess = false;
    int userGuess = 0;
    bool enableHints = false;
    string isHints = "";
    int giveUpAftTryNum = 0;
    bool giveUp = false;

    cout << "Only enter POSITIVE Numbers. Minimum Number will always be 0." << endl;
    cout << "Enter Max Number: ";
    cin >> myClass.max;
    cout << "Would you like to enable hints? Enter 'True' or 'False' only." << endl;
    cin >> isHints;
    cout << "Give up after how many tries: ";
    cin >> giveUpAftTryNum;

    if (isHints == "True") {
        enableHints = true;
    } else {
        enableHints = false;
    }

    // Check if Max is a number
    while (isMaxNotNum) {
        if (int(myClass.max) < 0) {
            cout << "Max is not a Positive Number";
            cout << "Enter Max Number: ";
            cin >> myClass.max;
        } else {
            myClass.max = int(myClass.max);
            isMaxNotNum = false;
            myClass.max = floor(myClass.max);
            myClass.ans = rand() % myClass.max;
        }
    }



    while(correctGuess != true || giveUp != true) {
        cout << "Guess the number!" << endl;
        cin >> userGuess;

        if (userGuess == myClass.ans) {
            if(tries < 10) {
                cout << "Good Job! You guessed the answer in under 10 tries!" << endl;
                correctGuess = true;
            } else if (tries == 0) {
                cout << "How...? You guessed the answer in one try!" << endl;
                correctGuess = true;
            } else {
                cout << "Good Job! You guessed the answer!" << endl;
                correctGuess = true;
            }
        } else if (userGuess != myClass.ans) {
            tries += 1;
            if (tries == giveUpAftTryNum) {
                cout << "Max Number of tries! The answer was " << myClass.ans << ". Try again next time!" << endl;
                giveUp = true;
            } else {
                if (enableHints) {
                    if (userGuess > myClass.ans) {
                        cout << "OOF. It's wrong! Try giving a smaller number." << endl;
                    } else {
                        cout << "OOF. It's wrong! Try giving a larger number." << endl;
                    }
                } else {
                    cout << "OOF. You got it wrong! Try again." << endl;
                }
            }
        } else if (userGuess > myClass.max) {
            tries += 1;
            if (tries == giveUpAftTryNum) {
                cout << "Max Number of tries! The answer was " << myClass.ans << ". Try again next time!" << endl;
                giveUp = true;
            } else {
                cout << "Your guess is higher than the max number!";
            }
        }
    }
}
