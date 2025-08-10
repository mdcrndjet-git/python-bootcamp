from multiprocessing import Pool
import time

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    start_time = time.time()
    print("Start Time: ", start_time)

    inputs = [35, 36, 37, 38]
    #outputs = [fib(number) for number in inputs]

    # Mutiple processing
    with Pool() as pool:
        outputs = pool.map(fib, inputs)

    end_time = time.time()
    print("End Time: ", end_time)

    print(end_time - start_time)
