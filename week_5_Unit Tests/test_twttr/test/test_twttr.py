from twttr import shorten



lower_vowels = ["a", "e", "i", "o" "u"]
upper_vowels = ["A", "E", "I", "O" "U"]

def test_lower_vowels():
    for i in shorten("Aloha world I wil help you"):
        assert i not in lower_vowels

def test_upper_vowels():
    for i in shorten("AlOha wErld I wil hElp yOu"):
        assert i not in upper_vowels

          