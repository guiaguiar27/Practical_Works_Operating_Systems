import os
def child():
   print('\nA new child ',  os.getpid())
   os._exit(0)  

def parent(): 
    print("its work")
    while True:
        newpid = os.fork()
        if newpid == 0: 
            print("call the child")
            child()
        else:
            pids = (os.getpid(), newpid)
            print("parent: %d, child: %d\n" % pids)
        reply = input("q for quit / c for new fork")
        if reply == 'c': 
            continue
        else:
            break

parent() 