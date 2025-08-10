def reverse_string(string: str):
    """Return a reversed version of `string`"""
    return string[::-1]

def main():
    print(reverse_string("palindrome"))
    print(reverse_string("The fox jumps over the fence"))

main()