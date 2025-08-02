has_skipped = False

for item in range(100):
    # Change code to skip printing numbers 20 to 80.
    skip = 20 <= item <= 80
    if skip:
        if not has_skipped:
            has_skipped = True
            print("Skipping 20 to 80")
        continue
    print(item)
