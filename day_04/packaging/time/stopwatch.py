import time

start = time.time()
print("Start Time: ", start)

for _ in range(1_000_000):
    x = 10 ** 1000

end = time.time()
print("End Time: ", end)

print("Execution Time:", end - start)