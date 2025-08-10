def count_vowels(string: str) -> int:
    """Return the number of vowels in the given string"""
    #pass
    #
    vowel_count = 0
    vowel_chars = "aeiou"
    for char in string:
        if char in  vowel_chars:
            vowel_count += 1
    
    return vowel_count

def main():
    char_count = count_vowels("The fox jumps over the fence.")
    print(char_count)

main()
