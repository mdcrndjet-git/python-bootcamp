def brew(drink, extra=None):
    """ Prints the following format:
        I made you {drink} with {extra}

        But make the extra optional:
        I made you {drink}
    """
    if extra:
        print(f"I made you {drink} with {extra}")
    else:
        print(f"I made you {drink}")


brew("coffee", "sugar")
brew("tea", "milk")
brew("coffee")
