# Create the binary for letter "h" as a list of 1's and 0's
binary_h = list(bin(ord('h')))
binary_h = binary_h[2:]
print(binary_h)

# Create the binary for letter "a" as a list of 1's and 0's
binary_a = list(bin(ord('a')))
binary_a = binary_a[2:]
print(binary_a)

# Create the binary for "hahaha"
binary = (binary_h +binary_a) *3
print(binary)