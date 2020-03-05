import threading
import time

def arraygenerator():
    i=0
    v=[]
    while i!=101:
        v.insert(i,i)
        i=i+1
   # print( v)
    p=v
    return p

#p=arraygenerator()
#print (p)
def potencia(x):
    d=[]
    l=0
    for i in x:
      d.insert(l,pow(i,2))
      l=l+1
    print(d)

def potencia1(x):
    d=[]
    l=0
    for i in x:
      if l<26:
       d.insert(i,pow(i,2))
      l=l+1
    print(d)

def potencia2(x):
    d=[]
    l=0
    for i in x:
      if 26<=l<52:
       d.insert(i,pow(i,2))
      l=l+1
    print(d)

def potencia3(x):
    d=[]
    l=0
    for i in x:
      if 52<=l<78:
       d.insert(i,pow(i,2))
      l=l+1
    print(d)
def potencia4(x):
    d=[]
    l=0
    for i in x:
      if 78<=l<104:
       d.insert(i,pow(i,2))
      l=l+1
    print(d)


t1=threading.Thread(target=arraygenerator)
t1.start()
\n

start=time.perf_counter()
t2=threading.Thread(target=potencia, args=(arraygenerator(),))
t2.start()
finish=time.perf_counter()


start1=time.perf_counter()
t21=threading.Thread(target=potencia1, args=(arraygenerator(),))
t21.start()

t22=threading.Thread(target=potencia2, args=(arraygenerator(),))
t22.start()

t23=threading.Thread(target=potencia3, args=(arraygenerator(),))
t23.start()

t24=threading.Thread(target=potencia4, args=(arraygenerator(),))
t24.start()

finish1=time.perf_counter()
t1.join()
t2.join()
t21.join()
t22.join()
t23.join()
t24.join()



print("EL unico hilo",finish-start,"s")

print("Hilo de 4",finish1-start1,"s")
