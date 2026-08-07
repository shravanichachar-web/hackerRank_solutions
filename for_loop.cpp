#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int a, b;
    // Read the two integers
    cin >> a >> b;
    
    // Array to store the English representation of numbers 1 through 9
    string numbers[] = {"", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    
    // Loop through the inclusive interval [a, b]
    for (int i = a; i <= b; i++) {
        if (i >= 1 && i <= 9) {
            // Print the English word for 1-9
            cout << numbers[i] << endl;
        } else if (i > 9 && i % 2 == 0) {
            // Print "even" for even numbers greater than 9
            cout << "even" << endl;
        } else if (i > 9 && i % 2 != 0) {
            // Print "odd" for odd numbers greater than 9
            cout << "odd" << endl;
        }
    }
    
    return 0;
}
