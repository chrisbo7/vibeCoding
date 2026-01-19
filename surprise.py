"""
surprise.py
A small Tkinter-based surprise popup that shows a celebratory message for a colleague.

Usage:
    python surprise.py "Colleague Name"

If run without arguments, it will ask for a name interactively.
"""
from __future__ import annotations

import sys
import random
import threading
import time
from typing import Optional

try:
    import tkinter as tk
    from tkinter import messagebox
except Exception:
    tk = None  # type: ignore


def generate_message(name: Optional[str]) -> str:
    """Return a friendly surprise message for the given name."""
    if not name:
        name = "friend"
    templates = [
        "Surprise, {name}! 🎉\nYou're awesome and we appreciate you!",
        "Hey {name}, look who just got surprised! 🎈\nHave a fantastic day!",
        "{name}, you deserve a round of applause! 👏\nThanks for everything you do.",
        "Heads up, {name}! 🌟\nThere's a little celebration in your honor!",
    ]
    return random.choice(templates).format(name=name)


def _burst(canvas: tk.Canvas, width: int, height: int, burst_time: float = 2.0) -> None:
    """Draw a lightweight confetti-like burst on the given canvas for burst_time seconds."""
    colors = ["#FF6633", "#FFB399", "#FF33FF", "#FFFF99", "#00B3E6", "#E6B333", "#3366E6", "#999966"]
    particles = []
    for _ in range(80):
        x = width // 2
        y = height // 3
        dx = random.uniform(-6, 6)
        dy = random.uniform(-8, -1)
        size = random.randint(4, 9)
        color = random.choice(colors)
        particles.append([x, y, dx, dy, size, color])

    start = time.time()

    def step():
        nonlocal particles
        now = time.time()
        elapsed = now - start
        canvas.delete("particle")
        for p in particles:
            x, y, dx, dy, size, color = p
            x += dx
            y += dy + 0.5 * elapsed
            dy += 0.2
            p[0], p[1], p[3] = x, y, dy
            canvas.create_oval(x, y, x + size, y + size, fill=color, outline=color, tags="particle")
        if now - start < burst_time:
            canvas.after(40, step)
        else:
            canvas.delete("particle")

    canvas.after(10, step)


def show_surprise(name: Optional[str] = None) -> None:
    """Show the Tkinter surprise window. Safe to call from main thread only."""
    if tk is None:
        print(generate_message(name))
        return

    root = tk.Tk()
    root.title("Surprise!")
    width = 520
    height = 320
    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()
    x = (screen_w - width) // 2
    y = (screen_h - height) // 3
    root.geometry(f"{width}x{height}+{x}+{y}")
    root.resizable(False, False)

    canvas = tk.Canvas(root, width=width, height=height, bg="#FFFFFF")
    canvas.pack(fill="both", expand=True)

    # Big message label
    msg = generate_message(name)
    lbl = tk.Label(root, text=msg, font=("Segoe UI", 14), bg="#FFFFFF", justify="center")
    lbl.place(relx=0.5, rely=0.55, anchor="n")

    # Button to close
    def on_close():
        root.destroy()

    btn = tk.Button(root, text="Close", command=on_close, font=("Segoe UI", 10))
    btn.place(relx=0.5, rely=0.85, anchor="s")

    # Start confetti burst after a short delay
    root.after(300, lambda: _burst(canvas, width, height, burst_time=3.0))

    # Make the window appear on top
    root.attributes("-topmost", True)
    root.after(5000, lambda: root.attributes("-topmost", False))

    root.mainloop()


def main(argv: list[str] | None = None) -> None:
    if argv is None:
        argv = sys.argv[1:]
    name = None
    if argv:
        name = argv[0]
    else:
        # ask for input if interactive
        try:
            name = input("Enter colleague's name (or press enter for a friendly surprise): ")
        except Exception:
            name = None
    show_surprise(name)


if __name__ == "__main__":
    main()
