import tkinter as tk
import random
import string
import os

# CHANGED: words.txt now has categories, one per line -> "Animals: tiger zebra monkey"
# load_words() returns a list of (category, word) pairs, same shape as the old WORDS list
def load_words():
    # looks for words.txt in the same folder as this .py file
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "words.txt")
    pairs = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            # skip empty lines, comment lines, and lines without a ":"
            if line == "" or line.startswith("#") or ":" not in line:
                continue
            category, word_part = line.split(":", 1)
            for w in word_part.split():
                if w.isalpha():             # skip words with digits or symbols
                    pairs.append((category.strip(), w.upper()))
    return pairs

WORDS = load_words()
if not WORDS:
    raise SystemExit("words.txt has no usable words.")

MAX_WRONG = 6

BG = "#2a9bb0"        # background
HEADER = "#1b7f93"    # top bar
GREEN = "#1f9d8a"     # correct letter
RED = "#e5533d"       # wrong letter
ORANGE = "#e07b39"    # word colour
KEY_BG = "#f2f2f2"    # unused key


class HangmanGame:
    def __init__(self, root):
        self.root = root
        root.title("Hangman")
        root.configure(bg=BG)
        root.resizable(False, False)

        # Top bar with category
        self.category_label = tk.Label(
            root, font=("Arial", 18, "bold"), bg=HEADER, fg="white",
            anchor="w", padx=10, pady=6
        )
        self.category_label.pack(fill="x")

        body = tk.Frame(root, bg=BG)
        body.pack(padx=20, pady=10)

        # Left side: hangman drawing
        self.canvas = tk.Canvas(body, width=220, height=280, bg=BG, highlightthickness=0)
        self.canvas.grid(row=0, column=0, padx=(0, 20))

        # Right side: word, info, keyboard
        right = tk.Frame(body, bg=BG)
        right.grid(row=0, column=1)

        # NEW: category box above the word, like "Animals" in the screenshot
        self.category_box = tk.Label(
            right, font=("Arial", 14, "bold"), bg="white", fg=HEADER,
            bd=2, relief="solid", padx=20, pady=4
        )
        self.category_box.pack(pady=(5, 0))

        self.word_label = tk.Label(right, font=("Courier", 28, "bold"), bg=BG, fg=ORANGE)
        self.word_label.pack(pady=(10, 5))

        self.info_label = tk.Label(right, font=("Arial", 12, "bold"), bg=BG, fg="white")
        self.info_label.pack()

        keyboard = tk.Frame(right, bg=BG)
        keyboard.pack(pady=10)

        self.buttons = {}
        for i, letter in enumerate(string.ascii_uppercase):
            btn = tk.Button(
                keyboard, text=letter, width=3, font=("Arial", 12, "bold"),
                command=lambda l=letter: self.guess(l)
            )
            btn.grid(row=i // 9, column=i % 9, padx=3, pady=3)
            self.buttons[letter] = btn

        self.message_label = tk.Label(right, font=("Arial", 14, "bold"), bg=BG, fg="white")
        self.message_label.pack(pady=5)

        tk.Button(
            right, text="New Game", font=("Arial", 12, "bold"),
            command=self.new_game
        ).pack(pady=5)

        # Let the player use the real keyboard too
        root.bind("<Key>", self.on_key_press)

        self.new_game()

    def new_game(self):
        self.category, self.word = random.choice(WORDS)     # CHANGED: picks (category, word) from your file
        self.guessed = set()
        self.wrong = 0
        self.game_over = False

        self.category_label.config(text=self.category)
        self.category_box.config(text="Category: " + self.category)    # NEW
        self.message_label.config(text="")
        for btn in self.buttons.values():
            btn.config(state="normal", bg=KEY_BG, fg="black")

        self.draw_gallows()
        self.update_display()

    def draw_gallows(self):
        c = self.canvas
        c.delete("all")
        c.create_line(20, 260, 140, 260, width=5, fill="white")   # base
        c.create_line(50, 260, 50, 30, width=5, fill="white")     # pole
        c.create_line(50, 30, 150, 30, width=5, fill="white")     # top beam
        c.create_line(150, 30, 150, 60, width=3, fill="white")    # rope

    def draw_next_part(self):
        c = self.canvas
        parts = [
            lambda: c.create_oval(125, 60, 175, 110, width=3, outline="white"),  # head
            lambda: c.create_line(150, 110, 150, 190, width=3, fill="white"),    # body
            lambda: c.create_line(150, 130, 120, 165, width=3, fill="white"),    # left arm
            lambda: c.create_line(150, 130, 180, 165, width=3, fill="white"),    # right arm
            lambda: c.create_line(150, 190, 125, 235, width=3, fill="white"),    # left leg
            lambda: c.create_line(150, 190, 175, 235, width=3, fill="white"),    # right leg
        ]
        parts[self.wrong - 1]()

    def update_display(self):
        shown = " ".join(ch if ch in self.guessed else "_" for ch in self.word)
        self.word_label.config(text=shown)
        self.info_label.config(text=f"Lives left: {MAX_WRONG - self.wrong}")

    def guess(self, letter):
        if self.game_over:
            return

        btn = self.buttons[letter]
        btn.config(state="disabled", disabledforeground="white")

        if letter in self.word:
            self.guessed.add(letter)
            btn.config(bg=GREEN)
        else:
            self.wrong += 1
            btn.config(bg=RED)
            self.draw_next_part()

        self.update_display()
        self.check_game_end()

    def check_game_end(self):
        if all(ch in self.guessed for ch in self.word):
            self.message_label.config(text="🎉 You won!")
            self.end_game()
        elif self.wrong >= MAX_WRONG:
            self.message_label.config(text=f"💀 You lost! Word: {self.word}")
            self.end_game()

    def end_game(self):
        self.game_over = True
        for btn in self.buttons.values():
            btn.config(state="disabled")

    def on_key_press(self, event):
        letter = event.char.upper()
        if letter in self.buttons and str(self.buttons[letter]["state"]) == "normal":
            self.guess(letter)


root = tk.Tk()
game = HangmanGame(root)
root.mainloop()