"""
Make a function that takes an input text and returns the longest word (excluding special char)
    "The quick brown fox jumps" -> "quick"
    "I love programming in Python!" -> "programming"
    "" -> ""
"""

def get_longest_word(text):
    # Add decoding process
    longest_word = ""
    words = text.split()

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word

string = "The quick brown fox jumps"
print(string)
longest_word_found = get_longest_word(string)
print("Longest word: ",longest_word_found)

string = "I love programming in Python!"
print(string)
longest_word_found = get_longest_word(string)
print("Longest word: ",longest_word_found)