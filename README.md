# Rounded button for Tkinter

![Static Badge](https://img.shields.io/badge/license-Unlicense-purple)

Tkinter rounded button. An unofficial modern button for Tkinter that supports rounding.

![Screenshot](https://raw.githubusercontent.com/limafresh/tkinter-rounded-button/main/screenshot.png)

## How to use?
It's very simple - download the `RoundedButton.py` file and place it in the folder where your script file is. Then import:

```python
from RoundedButton import RoundedButton
```

And create button, for example:

```python
button = RoundedButton(root, text="My button")
button.pack()
```

## Arguments
| Argument | Description |
| ---------------- | ------------ |
| **width** | int value in px, for example, width=250 |
| **height** | int value in px, for example, height=50 |
| **text** | text for button |
| **font** | int (for example, font=20) or tuple (for example, font=("Arial", 20)) |
| **radius** | radius of rounding, int value |
| **bg_color** | button background color, for example bg_color="red" or bg_color="#f0f0f0" |
| **fg_color** | button text color |
| **command** | button command |
| **cursor** | button cursor, by default cursor="hand2" |

## Methods
- `.config()`
- `.cget()`

## Code example
### Simple example
```python
import tkinter
from RoundedButton import RoundedButton


def clickme():
    clickme_button.config(text="Thanks!", bg_color="yellow", fg_color="black")


root = tkinter.Tk()
root.geometry("200x200")
root.title("Simple example")

clickme_button = RoundedButton(root, text="Click me!", command=clickme)
clickme_button.pack(padx=10, pady=10)

quit_button = RoundedButton(root, text="Quit", bg_color="red", command=quit)
quit_button.pack(padx=10, pady=10)

root.mainloop()
```

### Calculator

![Screenshot](https://raw.githubusercontent.com/limafresh/tkinter-rounded-button/main/calculator.png)

```python
import tkinter as tk
from RoundedButton import RoundedButton


def press(key):
    current = entry.get()
    if key == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif key == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, key)


root = tk.Tk()
root.title("Calculator")
root["bg"] = "#2e2e2e"

entry = tk.Entry(root, font=(None, 15), relief=tk.FLAT, justify=tk.RIGHT)
entry.pack(fill=tk.X, padx=5, pady=20)

buttons_frame = tk.Frame(root, bg="#2e2e2e")
buttons_frame.pack()

row, column = 0, 0

buttons = [
    "7",
    "8",
    "9",
    "+",
    "4",
    "5",
    "6",
    "-",
    "1",
    "2",
    "3",
    "*",
    "C",
    "0",
    "=",
    "/",
]

for button_text in buttons:
    button = RoundedButton(
        buttons_frame,
        width=50,
        height=50,
        radius=20,
        text=button_text,
        font=20,
        command=lambda key=button_text: press(key),
    )
    button.grid(row=row, column=column, padx=5, pady=5)

    if button_text in ["+", "-", "*", "/"]:
        button.config(bg_color="orange")
    elif button_text == "=":
        button.config(bg_color="blue")
    else:
        button.config(bg_color="#6e6e6e")

    column += 1
    if column == 4:
        column = 0
        row += 1

root.mainloop()
```
