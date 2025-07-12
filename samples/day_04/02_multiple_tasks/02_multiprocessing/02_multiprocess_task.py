from multiprocessing import Pool
import time


def process(number):
    return number * 1_000_000 ** 1_000_000


if __name__ == "__main__":
    start_time = time.time()

    inputs = [1, 2, 3]
    with Pool() as pool:
        outputs = pool.map(process, inputs)

    end_time = time.time()
    print(end_time - start_time)
