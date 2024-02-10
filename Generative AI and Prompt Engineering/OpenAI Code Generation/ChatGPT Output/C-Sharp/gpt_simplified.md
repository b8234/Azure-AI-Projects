# Simplified Character Count in C# Using LINQ

This document provides a simplified version of a C# program that counts the occurrences of a character within a string. By leveraging LINQ (Language Integrated Query), the code becomes more concise and readable.

## Simplified C# Code

The following C# code demonstrates a streamlined approach to counting characters using LINQ's `Count` method combined with a lambda expression:

```csharp
using System;
using System.Linq;

class Program
{
    // Simplified method to count character occurrences using LINQ
    static int CountChar(char character, string inputString)
    {
        // Use LINQ's Count method for concise character counting
        return inputString.Count(c => c == character);
    }

    // Main method to test the CountChar function
    static void Main(string[] args)
    {
        // Example character and string
        char character = 'a';
        string inputString = "banana";
        
        // Count occurrences of the character and print the result
        int charCount = CountChar(character, inputString);
        Console.WriteLine($"The character '{character}' appears {charCount} times in the string '{inputString}'.");
    }
}
```

## Explanation

- The `CountChar` method takes a character and a string as inputs. It returns an integer representing how many times the character appears in the string.
- Within `CountChar`, the `inputString.Count(c => c == character)` statement uses LINQ to count occurrences of `character` within `inputString`. The lambda expression `c => c == character` specifies the condition to match each character `c` in the string against the `character` parameter.
- The `Main` method provides an example usage of the `CountChar` function. It demonstrates counting the occurrences of the character `'a'` in the string `"banana"` and prints the result.

This LINQ-based approach simplifies the character counting logic, making the code cleaner and more intuitive to read and maintain.
