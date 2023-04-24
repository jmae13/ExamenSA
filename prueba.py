import threading

x = 0
lock = threading.Lock()

def increment():
    global x
    lock.acquire()
    x += 1
    lock.release()

threads = []

for i in range(5):
    t = threading.Thread(target=increment)
    threads.append(t)

for i, t in enumerate(threads):
    if i > 0:
        threads[i-1].join()  
    t.start()

for t in threads:
    t.join()

print("EL VALOR X ES:", x)
