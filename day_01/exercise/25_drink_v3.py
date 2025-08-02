"""
Create a function brew that takes a parameter `drink` and `extra`
and prints the following format:

    I made you {drink} with {extra}

But make the extra optional:
    I made you {drink}
"""

def brew(drink, extra=None):
    if not extra:
        print(f"I made you {drink}")
    else:
        print(f"I made you {drink} with {extra}")

brew("coffee", "sugar")
brew("tea", "milk")
brew("dark coffee")