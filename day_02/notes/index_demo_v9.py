from statistics import mean

# list tuple /tuple list

# list tuple
tuples = [(1,2,3),(4,5),(7,)]

# statistics: average
print(min(tuples, key=mean))
print(max(tuples, key=mean))