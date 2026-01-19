import re
from surprise import generate_message


def test_generate_message_uses_name():
    msg = generate_message("Alex")
    assert "Alex" in msg


def test_generate_message_fallback():
    msg = generate_message("")
    assert "friend" in msg


def test_generate_message_has_emoji_or_punctuation():
    msg = generate_message("Sam")
    # Should contain either emoji or at least an exclamation mark
    assert re.search(r"[!\u263A-\U0001F64F]", msg) or "!" in msg
