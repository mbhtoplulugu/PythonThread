from concurrent.futures import ThreadPoolExecutor
from time import perf_counter_ns

def sum(ilk,son):
    global toplam
    for i in range(ilk,son+1):
        toplam += i;
    print(f"Ara toplam : {toplam}")

threads = []

for i in range(5):
    global toplam
    toplam = 0 
    
    n = input("Cikis yapmak icin 'x' e basiniz veya \nthread sayisini giriniz:    ")
    print(n)
    if n =='x':
        break

    n=int(n)
    parca = int(100000 / n)
    kalan = 100000 % n
    
    for i in range(n):
        ilk=0
        son=0
        ilk = ilk + i * parca;
        son = ilk + parca - 1
        if i == (n - 1):
            son = son + kalan+1

        print(f"ilk : {ilk} --- son : {son}")

        startTime= perf_counter_ns()
        with ThreadPoolExecutor() as exe:
            exe.submit(sum,ilk,son)        
        endTime = perf_counter_ns()

    print("********************************************")
    print(f"toplam : {toplam}")
    print("---------")
    print(f"With {n} thread, it took {endTime-startTime} ns to complete")
    print("********************************************")
