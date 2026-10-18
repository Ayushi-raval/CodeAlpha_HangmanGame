<h1 align="center">🎮 Hangman Game in Python</h1>

<p align="center">
  A classic word-guessing game with a console version and a bonus graphical interface.<br>
  Built as <b>Task 1</b> of the <b>CodeAlpha Python Programming Internship</b>.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Interface-Console%20%7C%20GUI-green" alt="Interface">
  <img src="https://img.shields.io/badge/Internship-CodeAlpha-orange" alt="CodeAlpha">
</p>

---

## 📑 Table of Contents
- [About the Project](#-about-the-project)
- [Features](#-features)
- [Project Files](#-project-files)
- [Requirements](#-requirements)
- [How to Run](#-how-to-run)
- [How to Play](#-how-to-play)
- [Concepts Used](#-concepts-used)
- [Author](#-author)

---

## 📖 About the Project

Hangman is a word-guessing game where the player tries to find a hidden word by guessing one letter at a time. Every wrong guess brings the player closer to losing, so the goal is to reveal the whole word before the attempts run out.

This project has two versions of the game:
1. A **console version** that runs in the terminal.
2. A **GUI version** (bonus) with a graphical window, so the game is easier and more fun to play.

Words are loaded from an external file and grouped by category, so new words can be added without changing the code.

---

## ✨ Features

- 🔤 Random word selection from a word list
- 🗂️ Words organised by **category**
- ✅ Shows correct letters in their position and tracks wrong guesses
- ❌ Limited number of attempts
- 🏆 Win and lose messages at the end of each game
- 🖥️ Bonus: graphical version of the game
- ➕ Easy to extend by adding new words to `words.txt`

---

## 📂 Project Files

| File | Description |
|------|-------------|
| [`hangman.py`](https://github.com/Ayushi-raval/CodeAlpha_HangmanGame/blob/main/hangman.py) | Main game. Console (terminal) version of Hangman. |
| [`hangman_gui.py`](https://github.com/Ayushi-raval/CodeAlpha_HangmanGame/blob/main/hangman_gui.py) | Bonus version. Hangman with a graphical interface. |
| [`words.txt`](https://github.com/Ayushi-raval/CodeAlpha_HangmanGame/blob/main/words.txt) | Word list grouped by category, used by both versions. |
| [`README.md`](https://github.com/Ayushi-raval/CodeAlpha_HangmanGame/blob/main/README.md) | Project documentation (this file). |

---

## 🛠️ Requirements

- **Python 3.x** ([download here](https://www.python.org/downloads/))
- No extra libraries needed. The game uses only Python's built-in modules.

To check if Python is installed, run:

```bash
python --version
```

---

## ▶️ How to Run

**Step 1. Get the project**

Download it as a ZIP from the green **Code** button on GitHub, or clone it:

```bash
git clone https://github.com/Ayushi-raval/CodeAlpha_HangmanGame.git
cd CodeAlpha_HangmanGame
```

**Step 2. Run the version you want**

Console version:

```bash
python hangman.py
```

GUI version:

```bash
python hangman_gui.py
```

> 💡 On some systems you may need to use `python3` instead of `python`.

---

## 🎯 How to Play

1. Start the game and choose a category (if asked).
2. A hidden word appears as blanks, for example `_ _ _ _ _ _`.
3. Guess **one letter** at a time.
4. If the letter is in the word, it is revealed in the correct position.
5. If it is not, you lose one attempt.
6. **You win** by guessing the full word before running out of attempts.
7. **You lose** if all attempts are used up. The correct word is then shown.

**Example:**

```
Word:  _ y _ h o _
Wrong guesses: x, q
Attempts left: 4
Enter a letter:
```

---

## 🧠 Concepts Used

- Variables, strings and lists
- Loops (`while`, `for`) and conditional statements
- Functions to organise the code
- Reading data from a file
- Random selection using the `random` module
- Input validation
- Basic GUI programming (bonus)

---

## 👩‍💻 Author

**Ayushi Raval**
B.Tech Computer Science and Engineering
GitHub: [@Ayushi-raval](https://github.com/Ayushi-raval)

---

## 🙏 Acknowledgement

This project was created as part of the **Python Programming Internship at [CodeAlpha](https://www.codealpha.tech/)**.

<p align="center">⭐ If you like this project, give it a star! ⭐</p>
