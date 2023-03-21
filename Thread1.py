from time import perf_counter_ns
from threading import Thread

def sum(ilk,son):
    global toplam
    for i in range(ilk,(son+1)):
        toplam += i
 

global toplam
toplam = 0 
ilk=0
son=0
threads = []

while True:
    
    toplam = 0 
    n = input("Cikis yapmak icin 'x' e basiniz veya \nthread sayisini giriniz:    ")
    print(n)
    if n =='x':
        break
    n=int(n)
    parca = int(10000000 / n)
    kalan = 10000000 % n
    del threads
    threads = []
    startTime= perf_counter_ns()
    for i in range(n):
        ilk=0
        son=0
        ilk = ilk + i * parca;
        son = ilk + parca - 1
        if i == (n - 1):
            son = son + kalan+1
        
        print(f"ilk : {ilk} --- son : {son}")
        a = Thread(target=sum, args=(ilk,son,))
        threads.append(a)

    for a in threads:
        a.start()
        #lock.acquire()
        a.join()
        endTime = perf_counter_ns()
     
        #lock.release()
        
    print("********************************************")
    print(f"toplam : {toplam}")
    print("---------")
    print(f"With {n} thread, it took {endTime-startTime} ns to complete")
    print("********************************************")

   

    
    