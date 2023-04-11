from PairingHeap import PairingHeap 
class PriorityQueue:
    def __init__(self):
        self.pairing_heap = PairingHeap()

    def push(self, value):
        self.pairing_heap.Insert((value))

    def pop(self):
        return self.pairing_heap.Delete()

    # def decrease_priority(self, value, new_priority):
    #     return self.pairing_heap.decrease_priority(value, new_priority)

    def size(self):
        return self.pairing_heap.size()

    def is_empty(self):
        return self.pairing_heap.Empty()
    

p = PriorityQueue()
p.push((3,4))
p.push((6,2))
p.push((4,9))
p.push((6,3))
print(p.pop())