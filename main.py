import pyautogui
from pathlib import Path

def auto_typer(code_path, interval):
    with open(code_path, "r") as f:
        text = f.read().splitlines()
    
    pyautogui.sleep(interval)

    prev_spaces = 0
    prev_line = ""
    for line in text:
        spaces = 0
        if line == "":
            pyautogui.press('enter')
        else:
            while line.startswith("    "):
                spaces += 1
                line = line[4:]

            auto_tabs = 1 if prev_line.endswith(":") else 0
            auto_backspaces = 1 if prev_line.startswith("return") else 0

            delta_spaces = spaces - prev_spaces
            delta_auto_spaces = auto_tabs - auto_backspaces

            current_change = delta_spaces - delta_auto_spaces

            if current_change > 0:
                pyautogui.press('tab', current_change)
            if current_change < 0:
                pyautogui.press('backspace', abs(current_change))

            pyautogui.write(line, interval=0.05)

            prev_spaces = spaces
            prev_line = line

            pyautogui.press('enter')

if __name__ == "__main__":
    file_path = Path(__file__).parent / "test.py"
    auto_typer(file_path, 5)
