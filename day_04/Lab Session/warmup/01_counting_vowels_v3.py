def count_vowels(string: str) -> int:
    """Return the number of vowels in the given string"""
    #pass
    #
    vowel_chars = "aeiou"
    vowel_char = [char for char in string if char in vowel_chars]

    return len(vowel_char)

def main():
    char_count = count_vowels("The fox jumps over the fence.")
    print(char_count)

main()
