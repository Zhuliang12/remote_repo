#  Institution: Leapting Technology
#  Author：liang zhu
#  Time：2023/10/20 16:19

import concurrent.futures
import time
import os
import multiprocessing




def do_something(num):
    for i in range(num):
        pass


if __name__ == "__main__":
    print(multiprocessing.cpu_count())
    print(f'cpu数量={os.cpu_count()}')
    t1 = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.map(do_something, 100000)
        result = future.result()
    # do_something(100000)
    t2 = time.time()

    print(f'time=={t2 - t1}秒')
