import time
from threading import Thread
from multiprocessing import Pool


COUNT = 50000000


def countdown(number: int):

    while number > 0:
        number -= 1


def run_cpu_bound_multi_threaded():

    t1 = Thread(target=countdown, args=(COUNT//2,))
    t2 = Thread(target=countdown, args=(COUNT//2, ))

    start = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time.time()

    print(f'Time taken: {end-start} seconds')


def run_cpu_bound_single_threaded():
    """Performs countdown of a very large number"""

    start = time.time()
    countdown(COUNT)
    end = time.time()

    print(f'Time taken: {end - start} seconds')


def run_cpu_bound_multi_process():
    pool = Pool(processes=2)
    start = time.time()
    r1 = pool.apply_async(countdown, [COUNT//2])
    r2 = pool.apply_async(countdown, [COUNT//2])
    pool.close()
    pool.join()
    end = time.time()
    print(f'Time taken in seconds: {end-start}')


if __name__ == '__main__':
    run_cpu_bound_multi_process()
