import traceback
import sys
from surprise import generate_message

failed = 0

def assert_in(sub, s):
    global failed
    if sub not in s:
        print(f"Assertion failed: expected '{sub}' in '{s}'")
        failed += 1


def test_generate_message_uses_name():
    msg = generate_message("Alex")
    assert_in("Alex", msg)


def test_generate_message_fallback():
    msg = generate_message("")
    assert_in("friend", msg)


def test_generate_message_has_exclaim():
    msg = generate_message("Sam")
    if "!" not in msg and "🎉" not in msg:
        print(f"Assertion failed: expected punctuation or emoji in '{msg}'")
        global failed
        failed += 1


tests = [
    test_generate_message_uses_name,
    test_generate_message_fallback,
    test_generate_message_has_exclaim,
]

if __name__ == "__main__":
    for t in tests:
        try:
            t()
            print(f"PASS: {t.__name__}")
        except Exception:
            print(f"ERROR in {t.__name__}:")
            traceback.print_exc()
            failed += 1
    if failed:
        print(f"\n{failed} test(s) failed")
        sys.exit(1)
    else:
        print("\nAll tests passed")
