# Character Count Function in C#

This document describes a C# function that counts the occurrences of a specified character within a given string. The function, `CountChar`, takes two inputs: a character to search for and the string to search within.

## C# Function Code

```csharp
using System;

class Program
{
    // Function to count occurrences of a character in a string
    static int CountChar(char character, string inputString)
    {
        int count = 0;
        foreach (char c in inputString)
        {
            if (c == character)
            {
                count++;
            }
        }
        return count;
    }

    // Main method to demonstrate the usage of CountChar
    static void Main(string[] args)
    {
        char character = 'a';
        string inputString = "banana";
        int charCount = CountChar(character, inputString);
        Console.WriteLine($"The character '{character}' appears {charCount} times in the string '{inputString}'.");
    }
}
```

## Function Explanation

- The `CountChar` function is designed to iterate through each character in the provided string (`inputString`).
- It compares each character in the string to the specified character (`character`).
- If a match is found, it increments a counter (`count`).
- After completing the iteration through the string, the function returns the total count of occurrences.

## Example Usage

In the provided example within the `Main` method:

- The function is called with the character `'a'` and the string `"banana"`.
- The output demonstrates that the character `'a'` appears 3 times in the string `"banana"`.

This example showcases how to call the `CountChar` function and interpret its output. You can adjust the character and string inputs to fit your specific use case.
