# GPT-3.5 Turbo Planet Generator

This Python script utilizes the GPT-3.5 Turbo model from OpenAI to generate unique and fictional names for planets, along with descriptions for each planet type.

## Setup

1. Clone this repository to your local machine.
2. Install the required Python packages using pip:

```
pip install openai python-dotenv
```

3. Create a `.env` file in the project directory and add your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

4. Run the script:

```
python planet_generator.py
```

## Description

The script interacts with the GPT-3.5 Turbo model through the OpenAI API to generate names and descriptions for fictional planets. It first prompts the model to generate a specified number of unique planet names. Then, it pairs each generated name with a randomly selected planet type (Gas Giant, Moon, or Rogue Planet). Finally, it prompts the model to generate a random description for each planet, ensuring that each description consists of exactly two sentences.

## Usage

Modify the `planet_names_prompt` variable to specify the number of unique planet names you want to generate.

```python
planet_names_prompt = "Generate 3 unique and fictional names for planets."
```

Adjust the `planet_types` list to include the types of planets you want to generate descriptions for.

```python
planet_types = ['Gas Giant', 'Moon', 'Rogue Planet']
```

Run the script and observe the generated planet names and descriptions printed to the console.


## Contributing

Your contributions are welcome! If you have suggestions for improving the script or have found a bug, please open an issue or a pull request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

If you have any questions or feedback, feel free to [open an issue](https://github.com/b8234/Azure-AI-Projects/issues/new). I welcome your input and suggestions to improve this repository further.
