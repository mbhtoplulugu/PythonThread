
import concurrent.futures
import threading
from time import perf_counter_ns
from threading import Thread




def sum(ilk,son):
    global toplam
    for i in range(ilk,son+1):
        toplam += i;
    print(f"Ara toplam : {toplam}")
   
threads = []

for i in range(3):
    global toplam
    toplam = 0 
    
    n = input("Cikis yapmak icin 'x' e basiniz veya \nthread sayisini giriniz:    ")
    print(n)
    if n =='x':
        break

    n=int(n)
    parca = int(1000000 / n)
    kalan = 1000000 % n
    startTime= perf_counter_ns()
    #worker(n)
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=32)
    for i in range(n):
        ilk=0
        son=0
        ilk = ilk + i * parca;
        son = ilk + parca - 1
        if (i == n - 1):
            son = son + kalan+1
        print(f"ilk : {ilk} --- son : {son}")
        pool.submit(sum,ilk,son)

    pool.shutdown(wait=True)

    endTime = perf_counter_ns()
    print("********************************************")
    print(f"toplam : {toplam}")
    print("---------")
    print(f"With {n} thread, it took {endTime-startTime} ns to complete")
    print("********************************************")
    