import pytest
import array
import random
class Queue:
    def __init__(self,size_max):
        assert size_max > 0
        self.max = size_max
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = array.array('i', range(size_max))

    def empty(self):
        return self.size == 0

    def full(self):
        return self.size == self.max

    def enqueue(self,x):
        if self.size == self.max:
            return False
        self.data[self.tail] = x
        self.size += 1
        self.tail += 1
        if self.tail == self.max:
            self.tail = 0
        return True

    def dequeue(self):
        if self.size == 0:
            return None
        x = self.data[self.head]
        self.size -= 1
        self.head += 1
        if self.head == self.max:
            self.head = 0
        return x

def test1():
    q = Queue(2)
    res = q.empty()
    if not res:
        print("test1 NOT ok")
        return
    res = q.enqueue(10)
    if not res:
        print("test1 NOT ok")
        return
    res = q.enqueue(11)
    if not res:
        print("test1 NOT ok")
        return
    x = q.dequeue()
    if x != 10:
        print("test1 NOT ok")
        return
    x = q.dequeue()
    if x != 11:
        print("test1 NOT ok")
        return
    res = q.empty()
    if not res:
        print("test1 NOT ok")
        return
    print("test1 OK")

def test2():
    print("test2 OK")

def test3():
    print("test3 OK")


queue = Queue(3)


def test_empty():
    assert queue.empty() == False

def test_full():
    assert queue.full() == False

def test_dequeue():
    queue.dequeue() == None

def test_enqueue():
    assert queue.enqueue(8) == True
    assert queue.enqueue(3) == True
    assert queue.enqueue(6) == True
    assert queue.enqueue(5) == False


print(queue.dequeue())
print(queue.full())