# Simplify Python Code

This example demonstrates a simple Python function that counts the occurrences of a specific character within a string using the built-in `count()` method.

## Python Function

Here's the function definition:

```python
def count_char(character, string):
    return string.count(character)
```

## Example Usage

You can use the function as follows to count how many times the character `'a'` appears in the string `'banana'`:

```python
char_count = count_char('a', 'banana')
print("The character 'a' appears", char_count, "times in the string 'banana'.")
```

This version uses the built-in `count()` method of strings, which directly counts the occurrences of a given character in the string. Therefore, we can simplify the function by directly returning the result of calling `string.count(character)`.
