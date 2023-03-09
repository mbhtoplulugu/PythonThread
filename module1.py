
import concurrent.futures
import threading
from time import perf_counter_ns
from threading import Thread



def sum():
    global toplam
    for i in range(ilk,son):
        toplam += i;
   
def worker(lock):
    print("Worker thread running")
    startTime= perf_counter_ns()
# create a thread pool with 2 threads
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=n)
 
# submit tasks to the pool
    for i in range(n):
        pool.submit(worker)

    
    sum()
    
# wait for all tasks to complete
    pool.shutdown(wait=True)

    
    endTime = perf_counter_ns()

    print("********************************************")
    print(f"toplam : {toplam}")
    print("---------")
    print(f"With {n} thread, it took {endTime-startTime} ns to complete")
    print("********************************************")

threads = []
global toplam
toplam = 0 
ilk=0
son=0
lock = threading.Lock()
while True:
    n = input("Cikis yapmak icin 'x' e basiniz veya \nthread sayisini giriniz:    ")
    print(n)
    if n =='x':
        break

    n=int(n)
    parca = int(1000 / n)
    kalan = 1000 % n
    
    for i in range(n):
        ilk = ilk + i * parca;
        son = ilk + parca - 1
        if (i == n - 1):
            son += kalan

    worker(lock)

    
    