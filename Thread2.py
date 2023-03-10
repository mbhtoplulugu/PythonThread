
import concurrent.futures
from time import perf_counter_ns


def sum(ilk,son):
    global toplam
    for i in range(ilk,(son+1)):
        toplam += i;
    print(f"Ara toplam : {toplam}")

for i in range(10):
    global toplam
    toplam = 0 
    n = input("Cikis yapmak icin 'x' e basiniz veya \nthread sayisini giriniz:    ")
    if n =='x':
        break

    n=int(n)
    parca = int(10000000 / n)
    kalan = 10000000 % n
    startTime= perf_counter_ns()
    pool = concurrent.futures.ThreadPoolExecutor()
    for i in range(n):
        ilk=0
        son=0
        ilk = ilk + i * parca;
        son = ilk + parca - 1
        if (i == n - 1):
            son = son + kalan+1
        print(i)
        print(f"ilk : {ilk} --- son : {son}")
        pool.submit(sum,ilk,son)

    pool.shutdown(wait=True)
    
    endTime = perf_counter_ns()
    print("********************************************")
    print(f"toplam : {toplam}")
    print("---------")
    print(f"With {n} thread, it took {endTime-startTime} ns to complete")
    print("********************************************")
    