import threading
from time import perf_counter_ns
from threading import Thread



def sum(ilk,son):
    global toplam
    for i in range(ilk,son):
        toplam += i;
    

#def createThread(lock):
    


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

    startTime= perf_counter_ns()
    for i in range(n):
        ilk = ilk + i * parca;
        son = ilk + parca - 1
        if (i == n - 1):
            son += kalan
        
        print(n)
        
        i = Thread(target=sum, args=(lock,ilk,son,))
        threads.append(i)

        i.start()

        i.join()

        lock.acquire()
        sum(ilk,son)
        lock.release()
        
    endTime = perf_counter_ns()

    print("********************************************")
    print(f"toplam : {toplam}")
    print("---------")
    print(f"With {n} thread, it took {endTime-startTime} ns to complete")
    print("********************************************")

    #createThread(lock)

    
    