import time

def type_text(text, delay=0.05):
    """Prints text with a typing effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()