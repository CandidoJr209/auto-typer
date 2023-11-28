# Project AutoTyper

## Introduction
AutoTyper is a Python script designed to automate the process of typing code from a file into your preferred code editor. This project utilizes the `pyautogui` library to simulate keyboard input, saving you the hassle of manually typing lengthy code snippets. Whether you're dealing with long functions or multiline code blocks, AutoTyper is here to make your life easier.

## Features
- **Code Automation**: Automatically types code from a specified file into your code editor.
- **Indentation Handling**: Handles indentation levels and adjusts tabs and backspaces accordingly.
- **Customizable Interval**: Set the typing interval to match your preferred speed.

## How to Use
1. Install the required libraries:
   ```bash
   pip install pyautogui
   ```

2. Copy the auto_typer function into your Python project.

3. Call the function with the path to your code file and the desired interval between the script initialization and the typing:
    ```python
    from auto_typer import auto_typer

    code_path = "path/to/your/code/file.py"
    typing_interval = 0.1  # Adjust as needed

    auto_typer(code_path, interval)
    ```

4. Run your script and switch to your code editor within the specified sleep interval to give it focus.

## Important Notes
* Make sure to adjust the typing_interval based on your code editor's responsiveness.
* Ensure that your code editor is active and ready to receive input when running the script.
