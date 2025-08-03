# Slcing list

ranks = ["A","1","2","3","4","5","6","7","8","9","10","J","Q","K"]

# print '10','J','Q','K',and 'A' from list (sequential)
print(ranks[10:],ranks[0])
# print '10','J','Q','K',and 'A' from list (reverse)
print(ranks[-4:],ranks[0])

# print '10','J','Q','K',and 'A' from list (sequential) - remove square bracket
print(*ranks[10:],ranks[0])
# print '10','J','Q','K',and 'A' from list (reverse) - remove square bracket
print(*ranks[-4:],ranks[0])