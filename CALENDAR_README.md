# Calendar Surprise Script

A fun Python script that displays the full 2026 calendar in a Tkinter GUI window and surprises your colleague with a celebratory popup message!

## Features

- 📅 **Full-year 2026 calendar** displayed in a 3x4 grid (12 months)
- 🎉 **Surprise popup** with a friendly message and emoji confetti
- 🌟 **Personalized greeting** for your colleague
- ✨ **Clean Tkinter UI** with scrollable calendar view
- 🔄 **Fallback to console** if Tkinter/GUI is not available
- ✓ **Fully tested** with 7 unit tests (all passing)

## Requirements

- Python 3.8+ (Tkinter usually included in standard CPython installations)
- Windows, macOS, or Linux

## Usage

### Basic Usage (Interactive)

```cmd
python calendar_surprise.py
```

When run without arguments, the script will prompt you to enter your colleague's name.

### With Colleague Name (Recommended)

```cmd
python calendar_surprise.py "Jordan"
```

Replace `"Jordan"` with your colleague's actual name.

## What Happens

1. A **surprise popup** appears with a celebratory message personalized for your colleague
2. Click **"See the Calendar!"** button to proceed
3. The full **2026 calendar** opens in a new window, showing all 12 months in an easy-to-read grid
4. A personalized footer message displays at the bottom

## Testing

Run the included unit tests to validate all helper functions:

```cmd
python test_calendar_surprise.py
```

All 7 tests verify:
- ✓ Surprise messages include the colleague's name
- ✓ Fallback message works (if no name provided)
- ✓ Messages include emoji/celebration characters
- ✓ Calendar text contains the year 2026
- ✓ Calendar text contains all 12 month names
- ✓ Calendar grid has exactly 12 months
- ✓ Calendar grid contains month names

## Files Included

- `calendar_surprise.py` — Main calendar script with surprise popup
- `test_calendar_surprise.py` — Unit tests (7 tests, all passing)
- `README.md` — This file

## Troubleshooting

### "Tkinter not found" or GUI doesn't open

If you're in a headless environment (no display) or Tkinter isn't installed:
- The script will fall back to printing the calendar to the console
- Install Tkinter if needed: `pip install tk`

### Python command not found

On Windows, try:
```cmd
python calendar_surprise.py "Colleague Name"
```

Or use the full path to your Python interpreter:
```cmd
C:\Users\<YourUsername>\.virtualenvs\<env_name>\Scripts\python.exe calendar_surprise.py "Colleague Name"
```

### Script runs but no GUI appears

This is normal in remote/headless environments. The calendar text will print to the console instead.

## Customization Ideas

Want to enhance the script? Here are some ideas:

- Add sound effects (beep/celebration sound on popup)
- Highlight specific dates (birthdays, holidays, important dates)
- Add color themes (dark mode, seasonal colors)
- Export calendar to PDF
- Add past/future year navigation
- Include lunar calendar or holidays
- Add animated confetti with physics

## How to Run on Your Machine

**Windows Command Prompt:**
```cmd
cd "c:\Users\cmpotsiar\OneDrive - OTE\Desktop\IT ARCHITECTURE PROJECTS\CODE test"
python calendar_surprise.py "YourColleagueName"
```

**If using virtualenv:**
```cmd
cd "c:\Users\cmpotsiar\OneDrive - OTE\Desktop\IT ARCHITECTURE PROJECTS\CODE test"
C:\Users\cmpotsiar\.virtualenvs\YOUR_DJANGO_PROJECT-2y_e-DLS\Scripts\python.exe calendar_surprise.py "YourColleagueName"
```

Enjoy surprising your colleague! 🎉
