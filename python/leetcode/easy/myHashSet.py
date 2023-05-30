class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:
    def __init__(self):
        self.size = 10000
        self.buckets = [None] * self.size

    def add(self, key: int) -> None:
        index = hash(key) % self.size
        if not self.buckets[index]:
            self.buckets[index] = ListNode(key)
        else:
            curr = self.buckets[index]
            while True:
                if curr.key == key:
                    return
                if not curr.next:
                    break
                curr = curr.next
            curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = hash(key) % self.size
        if not self.buckets[index]:
            return
        if self.buckets[index].key == key:
            self.buckets[index] = self.buckets[index].next
            return
        curr = prev = self.buckets[index]
        while curr:
            if curr.key == key:
                prev.next = curr.next
                return
            prev, curr = curr, curr.next

    def contains(self, key: int) -> bool:
        index = hash(key) % self.size
        curr = self.buckets[index]
        while curr:
            if curr.key == key:
                return True
            curr = curr.next
        return False
