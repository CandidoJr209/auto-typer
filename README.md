# Project AutoTyper

## Introduction
AutoTyper is a Python script designed to automate the process of typing code from a file into your preferred code editor. This project utilizes the `pyautogui` library to simulate keyboard input, saving you the hassle of manually typing lengthy code snippets. Whether you're dealing with long functions or multiline code blocks, AutoTyper is here to make your life easier.

## Features
- **Code Automation**: Automatically types code from a specified file into your code editor.
- **Indentation Handling**: Handles indentation levels and adjusts tabs and backspaces accordingly.
- **Customizable Interval**: Set the typing interval to match your preferred speed.

## How to Use
1. Clone the repository to your local machine:
   ```bash
   git clone git@github.com:CandidoJr209/auto-typer.git
   ```

2. Set up a virtual environment and install the dependencies:
    ```bash
    cd auto-typer

    python -m venv venv
    source venv/bin/activate

    pip install -r requirements.txt
    ```


3. Make the script executable::
    ```bash
    chmod +x auto_typer.py
    ```

4. Run the script with command line arguments:
    ```bash
    ./auto_typer.py path/to/your/code/file.py 3
    ```

## Important Notes
* Make sure to adjust the typing_interval based on your code editor's responsiveness.
* Ensure that your code editor is active and ready to receive input when running the script.
