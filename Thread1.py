import threading
from time import perf_counter_ns
from threading import Thread

def sum(ilk,son):
    toplam =0
    for i in range(ilk,(son+1)):
        toplam += i

    print(f"aratoplam  : {toplam}")
    return toplam

threads = []
lock = threading.Lock()
while True:
    anatoplam =0
    ilk=0
    son=0
    n = input("Cikis yapmak icin 'x' e basiniz veya \nthread sayisini giriniz:    ")
    print(n)
    if n =='x':
        break

    n=int(n)
    parca = int(1000 / n)
    kalan = 1000 % n

    startTime= perf_counter_ns()
    for i in range(n):

        ilk = ilk + i * parca    
        son = ilk + parca - 1   
        if (i == n - 1):
            son = son + kalan+1
        
        print(f"ilk : {ilk} --- son : {son}")
        
        a = Thread(target=sum, args=(ilk,son,))
        threads.append(a)

        a.start()
        lock.acquire()
        a.join()
        
        anatoplam += sum(ilk,son)
        endTime = perf_counter_ns()
        print("********************************************")
        print(f"dongu ici genel toplam: {anatoplam}")
        print("---------")
        print(f"With {i} thread, it took {endTime-startTime} ns to complete")
        print("********************************************")
        lock.release()
        
    print("*******************************************")
    print(f"genel toplam: {anatoplam}")
    print("---------")
    print(f"With {n} thread, it took {endTime-startTime} ns to complete")
    print("********************************************")

   

    
    