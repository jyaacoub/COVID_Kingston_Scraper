from multiprocessing import Process
import os
import time

def displayNum(num):
    while True:
        print("I am displaying the number", num, "My id is:", os.getpid(), __name__)
        time.sleep(5)
        pass

if __name__ == '__main__':
    p = Process(target=displayNum, args=('54',), name='billyboi')
    print(p.is_alive(), p.name)
    p.start()
    print(p.is_alive(), p.name)
