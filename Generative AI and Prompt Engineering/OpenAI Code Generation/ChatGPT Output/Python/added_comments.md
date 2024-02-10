# Python Function with Comments

Certainly! Here's the code with added comments:

## Function Definition

```python
def count_char(character, string):
    """
    Count the occurrences of a character in a given string.

    Parameters:
        character (str): The character to count.
        string (str): The input string.

    Returns:
        int: The count of occurrences of the character in the string.
    """
    return string.count(character)
```

## Example Usage

Below is an example demonstrating how to use the `count_char` function:

```python
char_count = count_char('a', 'banana')  # Count occurrences of 'a' in 'banana'
print("The character 'a' appears", char_count, "times in the string 'banana'.")
```

## Explanation of Comments

- The `count_char` function is defined with two parameters: `character` and `string`.
- A docstring is provided to explain what the function does, its parameters, and its return value.
- The function uses the `count()` method of strings to count the occurrences of the specified character in the input string.
- The example usage demonstrates how to call the function and print the result.
```

In this markdown:

- Headings are used to segment the document into clear, readable sections.
- Code blocks are wrapped in triple backticks with `python` specified for syntax highlighting, enhancing readability.
- An explanation section is provided outside of the code blocks to discuss the comments and functionality in plain English.