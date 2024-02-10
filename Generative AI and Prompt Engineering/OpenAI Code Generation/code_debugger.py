import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAIAPI with your API key
openai_api = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def fix_code_incorrectness(incorrect_code):
    # Prompt ChatGPT to fix the incorrect code
    prompt = f"Fix the following Python code:\n\n{incorrect_code}"
    response = openai_api.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt}],
        temperature=0.7,
        max_tokens=100,
    )

    # Extract the content of the ChatCompletionMessage
    content = response.choices[0].message.content
    role = response.choices[0].message.role
    function_call = response.choices[0].message.function_call
    tool_calls = response.choices[0].message.tool_calls
    
    return content, role, function_call, tool_calls

def fix_selected_files(folder_path, selected_files):
    # Iterate through the provided Python files
    for file_name in selected_files:
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path) and file_name.endswith(".py"):
            with open(file_path, "r") as file:
                incorrect_code = file.read()
                print("=" * 50)
                print("File:", file_name)
                print("-" * 50)
                print("Incorrect Code:")
                print(incorrect_code)
                print("\nFixed Code:")
                content, role, function_call, tool_calls = fix_code_incorrectness(incorrect_code)
                print("Content:", content)
                print("Role:", role)
                print("Function Call:", function_call)
                print("Tool Calls:", tool_calls)
                print("=" * 50)

def main():
    # Path to the folder containing Python code files
    folder_path = "path/to/files/folder"

    # Prompt the user to enter the names of the files they want to fix
    files_to_fix = input("Enter the names of the Python files you want to fix (separated by commas): ").split(",")

    # Fix incorrect code in the selected files
    fix_selected_files(folder_path, files_to_fix)

if __name__ == "__main__":
    main()
