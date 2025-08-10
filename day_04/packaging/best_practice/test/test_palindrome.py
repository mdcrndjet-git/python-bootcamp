def palindrome(text):
    return text in text[::-1]

def test_palindrome():
    assert palindrome("racecar")
    assert not palindrome("yes")
    assert palindrome("level")