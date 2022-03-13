from threading import Thread
import time
import sys
import signal


def display1():
    t = Thread(target=display2)
    # t.setDaemon(True)
    t.start()
    for i in range(5):
        print("Child Thread 1")
        time.sleep(2)


def display2():
    for i in range(5):
        print("Child Thread 2")
        time.sleep(2)


def handler(signum, frame):
    sys.exit(0)


signal.signal(signal.SIGINT, handler)

t = Thread(target=display1)
t.setDaemon(True)
t.start()
time.sleep(5)
print("End of Main Thread")
