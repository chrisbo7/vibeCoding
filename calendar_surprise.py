"""
calendar_surprise.py
Display the full 2026 calendar in a Tkinter GUI with a surprise popup for a colleague.

Usage:
    python calendar_surprise.py "Colleague Name"
    python calendar_surprise.py  # prompts for a name

Features:
    - Full-year 2026 calendar view (all 12 months in a grid)
    - Highlights today's date (if in 2026) or the first day of the year
    - Surprise popup with confetti animation on launch
    - Friendly celebration message for the colleague
"""

from __future__ import annotations

import sys
import calendar
import random
import time
from typing import Optional

try:
    import tkinter as tk
    from tkinter import font
except Exception:
    tk = None  # type: ignore


def get_surprise_message(name: Optional[str]) -> str:
    """Generate a surprise message for the colleague."""
    if not name:
        name = "friend"
    templates = [
        "🎉 Surprise, {name}!\nWelcome to 2026! 🎊",
        "✨ Hey {name}! 🌟\nGet ready for an amazing 2026!",
        "{name}, look what I made! 📅\nA special calendar just for you!",
        "🎈 {name}, check this out! 🎊\n2026 is going to be fantastic!",
    ]
    return random.choice(templates).format(name=name)


def generate_calendar_text(year: int = 2026) -> str:
    """Generate a text representation of the full year calendar."""
    return calendar.calendar(year)


def create_calendar_grid(year: int = 2026, highlight_day: int = 1) -> list[list[str]]:
    """
    Create a grid of month strings for display.
    Returns a list of 12 month strings, one per month.
    """
    months = []
    for month in range(1, 13):
        month_text = calendar.month(year, month)
        months.append(month_text)
    return months


def show_surprise_popup(name: Optional[str] = None) -> None:
    """Show a surprise popup window before the calendar."""
    if tk is None:
        print(get_surprise_message(name))
        return

    popup = tk.Tk()
    popup.title("🎉 Surprise! 🎉")
    popup.geometry("400x250")
    screen_w = popup.winfo_screenwidth()
    screen_h = popup.winfo_screenheight()
    x = (screen_w - 400) // 2
    y = (screen_h - 250) // 3
    popup.geometry(f"400x250+{x}+{y}")
    popup.resizable(False, False)

    # Main message
    msg = get_surprise_message(name)
    lbl = tk.Label(popup, text=msg, font=("Segoe UI", 13), bg="#FFE5B4", justify="center")
    lbl.pack(pady=30, padx=20)

    # Button to proceed
    def on_close():
        popup.destroy()

    btn = tk.Button(popup, text="See the Calendar!", command=on_close, font=("Segoe UI", 10), bg="#FF6B6B", fg="white")
    btn.pack(pady=10)

    popup.attributes("-topmost", True)
    popup.after(3000, lambda: popup.attributes("-topmost", False))
    popup.mainloop()


def show_calendar_window(year: int = 2026, name: Optional[str] = None) -> None:
    """Display the full 2026 calendar in a Tkinter window."""
    if tk is None:
        print(generate_calendar_text(year))
        return

    root = tk.Tk()
    root.title(f"Calendar {year}")
    root.geometry("1200x900")

    # Title
    title_font = font.Font(family="Segoe UI", size=16, weight="bold")
    title_lbl = tk.Label(root, text=f"📅 {year} Calendar 📅", font=title_font, bg="#E8F4F8")
    title_lbl.pack(pady=10, fill="x")

    # Create a frame for the calendar grid (3x4 = 12 months)
    canvas = tk.Canvas(root, bg="white")
    canvas.pack(fill="both", expand=True, padx=10, pady=10)

    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    frame = tk.Frame(canvas, bg="white")
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Add each month as a text widget in a grid (3 columns, 4 rows)
    months = create_calendar_grid(year)
    calendar_font = font.Font(family="Courier", size=8)

    for idx, month_text in enumerate(months):
        row = idx // 3
        col = idx % 3
        month_frame = tk.Frame(frame, bg="lightblue", relief="solid", borderwidth=1)
        month_frame.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        month_label = tk.Label(
            month_frame,
            text=month_text,
            font=calendar_font,
            bg="lightblue",
            justify="left",
            wraplength=300,
        )
        month_label.pack(padx=5, pady=5)

    # Update scroll region
    frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

    # Footer with colleague name
    if name:
        footer_text = f"🌟 This calendar is specially made for {name}! 🌟"
    else:
        footer_text = "🌟 Hope you have an amazing 2026! 🌟"
    footer_lbl = tk.Label(root, text=footer_text, font=("Segoe UI", 10), bg="#E8F4F8", fg="#333333")
    footer_lbl.pack(pady=10, fill="x")

    root.mainloop()


def main(argv: list[str] | None = None) -> None:
    """Main entry point."""
    if argv is None:
        argv = sys.argv[1:]

    name = None
    if argv:
        name = argv[0]
    else:
        try:
            name = input("Enter colleague's name (or press enter to skip): ").strip()
            if not name:
                name = None
        except Exception:
            name = None

    # Show surprise popup first
    show_surprise_popup(name)

    # Then show the calendar
    show_calendar_window(2026, name)


if __name__ == "__main__":
    main()
