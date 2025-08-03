ranks=["A","1","2","3","4","5","6","7","8","9","10","J","Q","K"]

# print '10','J','Q','K',and 'A' from list (sequential)
print(ranks[10],ranks[11],ranks[12],ranks[13],ranks[0])
# print '10','J','Q','K',and 'A' from list (reverse)
print(ranks[-4],ranks[-3],ranks[-2],ranks[-1],ranks[0])

# Change '10','J','Q','K',and 'A' from list (sequential)
ranks[10] = "drawn"
ranks[11] = "drawn"
ranks[12] = "drawn"
ranks[13] = "drawn"
ranks[0] = "drawn"
# print '10','J','Q','K',and 'A' from list (sequential)
print(ranks[10],ranks[11],ranks[12],ranks[13],ranks[0])

# Change '10','J','Q','K',and 'A' from list (reverse)
ranks[-4] = "drawn X"
ranks[-3] = "drawn X"
ranks[-2] = "drawn X"
ranks[-1] = "drawn X"
ranks[0] = "drawn X"
# print '10','J','Q','K',and 'A' from list (reverse)
print(ranks[-4],ranks[-3],ranks[-2],ranks[-1],ranks[0])