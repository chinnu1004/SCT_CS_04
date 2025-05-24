# ⌨️ Python Keylogger (Educational Use Only)

A simple keylogger written in Python using the `pynput` library. It captures keyboard input and logs it to a file.

> ⚠️ **Disclaimer:** This tool is for **educational and authorized testing** purposes **only**. Unauthorized use of keyloggers is illegal and unethical. Always obtain proper consent.

---

## 🚀 Features

- Logs all keystrokes (letters, numbers, special characters)
- Records both printable and special keys (like `Enter`, `Shift`, etc.)
- Saves output to a text file: `keystrokes.txt`

---

## 🛠 Requirements

- Python 3.6+
- [`pynput`](https://pypi.org/project/pynput/)

Install with pip:

```bash
pip install pynput
```

---

## 📁 Project Structure

```
keylogger/
├── keylogger.py        # Main script
├── keystrokes.txt      # Output file (auto-created)
```

---

## ▶️ How to Run

1. Clone or download the repository
2. Run the script using Python:

```bash
python keylogger.py
```

3. The script will start logging keys into `keystrokes.txt`
4. Press `Ctrl + C` in the terminal to stop the logger

---

## 📄 Example Output (`keystrokes.txt`)

```
h
e
l
l
o
[Key.space]
w
o
r
l
d
```

---

## ❗ Important Notice

- This project is **for learning purposes only**.
- **Do not deploy or run this on any system without full legal and ethical consent.**
- Misuse of this script may lead to **legal consequences**.

---

## 📄 License

This project is released under the MIT License. See the `LICENSE` file for more information.

---

## 🙋 Author

Developed with a focus on cybersecurity education and Python scripting practice.

---

## 📚 Related Topics

- Cybersecurity
- Ethical Hacking
- Python Automation
- Keyboard Monitoring
