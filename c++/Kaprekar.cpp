#include <iostream>
#include <cmath>
using namespace std;

// Function to check if a number is a Kaprekar number in a given base
bool isKaprekar(int number, int base)
{
    // Invalid cases
    if (number < 0 || base <= 1)
    {
        return false;
    }

    // Square the number
    long long squared = static_cast<long long>(number) * number;
    
    // Initial divisor (smallest power of the base greater than squared number)
    long long divisor = 1;
    while (squared / divisor >= base)
    {
        divisor *= base;
    }

    // Check if the sum of left and right parts equals the original number
    while (divisor > 0)
    {
        long long left = squared / divisor;   // Left part of the number
        long long right = squared % divisor;  // Right part of the number

        if (left + right == number && right > 0)
        {
            return true;
        }

        divisor /= base;
    }

    return false;
}

// Function to display a friendly message for Kaprekar result
void displayKaprekarResult(int number, int base, bool isKaprekar)
{
    if (isKaprekar)
    {
        cout << number << " is a Kaprekar number in base " << base << "!" << endl;
    }
    else
    {
        cout << number << " is not a Kaprekar number in base " << base << "." << endl;
    }
}

int main()
{
    int number, base;

    cout << "=== Kaprekar Number Checker ===" << endl;
    
    // Get user input for number and base
    cout << "Enter a number: ";
    cin >> number;
    cout << "Enter the base: ";
    cin >> base;

    // Check if the number is a Kaprekar number and display result
    bool result = isKaprekar(number, base);
    displayKaprekarResult(number, base, result);

    return 0;
}
