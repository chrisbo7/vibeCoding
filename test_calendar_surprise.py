"""
test_calendar_surprise.py
Unit tests for calendar_surprise.py helper functions.
"""
from calendar_surprise import get_surprise_message, generate_calendar_text, create_calendar_grid


def test_surprise_message_includes_name():
    msg = get_surprise_message("Jordan")
    assert "Jordan" in msg, f"Name not in message: {msg}"
    print("✓ Surprise message includes name")


def test_surprise_message_fallback():
    msg = get_surprise_message(None)
    assert "friend" in msg, f"Fallback not in message: {msg}"
    print("✓ Surprise message fallback works")


def test_surprise_message_has_emoji():
    msg = get_surprise_message("Sam")
    # Check for common emoji characters or exclamation
    assert any(c in msg for c in "🎉✨🌟🎊🎈📅!"), f"No emoji/punctuation in: {msg}"
    print("✓ Surprise message has emoji/punctuation")


def test_calendar_text_contains_year():
    cal = generate_calendar_text(2026)
    assert "2026" in cal, "Year not found in calendar text"
    print("✓ Calendar text contains year")


def test_calendar_text_contains_months():
    cal = generate_calendar_text(2026)
    assert "January" in cal and "December" in cal, "Months not in calendar"
    print("✓ Calendar text contains months")


def test_calendar_grid_has_12_months():
    grid = create_calendar_grid(2026)
    assert len(grid) == 12, f"Expected 12 months, got {len(grid)}"
    print("✓ Calendar grid has 12 months")


def test_calendar_grid_contains_month_names():
    grid = create_calendar_grid(2026)
    all_text = " ".join(grid)
    assert "January" in all_text and "December" in all_text, "Month names missing"
    print("✓ Calendar grid contains month names")


if __name__ == "__main__":
    tests = [
        test_surprise_message_includes_name,
        test_surprise_message_fallback,
        test_surprise_message_has_emoji,
        test_calendar_text_contains_year,
        test_calendar_text_contains_months,
        test_calendar_grid_has_12_months,
        test_calendar_grid_contains_month_names,
    ]

    failed = 0
    for test in tests:
        try:
            test()
        except AssertionError as e:
            print(f"✗ {test.__name__}: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__}: {type(e).__name__}: {e}")
            failed += 1

    if failed:
        print(f"\n{failed}/{len(tests)} tests failed")
        exit(1)
    else:
        print(f"\nAll {len(tests)} tests passed!")
