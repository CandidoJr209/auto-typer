#!/usr/bin/env python
import pyautogui
from pathlib import Path
import argparse

INDENTATION_WIDTH = 4

def auto_typer(file_path, interval):
    if not Path(file_path).is_file():
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    with open(file_path, "r") as file:
        lines = file.read().splitlines()

    pyautogui.sleep(interval)

    prev_spaces = 0
    prev_line = ""

    for line in lines:
        spaces = 0

        if not line:
            pyautogui.press('enter')
        else:
            while line.startswith(" " * INDENTATION_WIDTH):
                spaces += 1
                line = line[INDENTATION_WIDTH:]

            auto_tabs = 1 if prev_line.endswith(":") else 0
            auto_backspaces = 1 if prev_line.startswith(("return", "raise")) else 0


            delta_spaces = spaces - prev_spaces
            delta_auto_spaces = auto_tabs - auto_backspaces

            current_change = delta_spaces - delta_auto_spaces

            if current_change > 0:
                pyautogui.press('tab', current_change)
            elif current_change < 0:
                pyautogui.press('backspace', abs(current_change))

            pyautogui.write(line, interval=0.05)

            prev_spaces = spaces
            prev_line = line

            pyautogui.press('enter')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automate typing code into a code editor.")
    parser.add_argument("file_path", help="Path to the code file.")
    parser.add_argument("interval", type=float, help="Interval between the script initialization and typing, in seconds.")

    args = parser.parse_args()

    auto_typer(args.file_path, args.interval)