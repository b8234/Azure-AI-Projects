# Count Character Occurrences Function

Write a function in Python that takes a character and a string as input, and returns how many times the character appears in the string.

## Python Function

Here is the function definition:

```python
def count_char(character, string):
    count = 0
    for char in string:
        if char == character:
            count += 1
    return count
```

## Example Usage

To demonstrate how the function works, consider the following example where we count how many times the character `'a'` appears in the string `'banana'`:

```python
char_count = count_char('a', 'banana')
print("The character 'a' appears", char_count, "times in the string 'banana'.")
```

This function iterates through each character in the string and checks if it matches the given character. If it does, it increments the count. Finally, it returns the count of occurrences of the character in the string.
```

In this formatted markdown:

- The title and subtitles are clearly defined with `#` and `##` for headings.
- The Python code is enclosed in triple backticks with `python` specified for syntax highlighting, enhancing readability.
- The explanatory text is placed outside of code blocks, providing a smooth reading flow.