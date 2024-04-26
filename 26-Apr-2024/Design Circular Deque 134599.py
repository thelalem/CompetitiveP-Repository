# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class ListNode:
    def __init__(self, value=0):
        self.next = None
        self.prev = None
        self.value = value
class MyCircularDeque:
    def __init__(self, k: int):
       self.capacity = k 
       self.size = 0
       self.head = ListNode()
       self.tail = ListNode()
       self.head.next = self.tail
       self.tail.prev = self.head

    def insertFront(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        new = ListNode(value)
        self._add_node(self.head, new)
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        new_node = ListNode(value)
        self._add_node(self.tail.prev, new_node)
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.size == 0:
            return False
        self._remove_node(self.head.next)
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.size == 0:
            return False
        self._remove_node(self.tail.prev)
        self.size -= 1
        return True



    def getFront(self) -> int:
        if self.size == 0:
            return -1
        return self.head.next.value

    def getRear(self) -> int:
        if self.size == 0:
            return -1
        return self.tail.prev.value
        

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity

    def _add_node(self, node: ListNode, new_node: ListNode) -> None:
        temp = node.next
        node.next = new_node
        new_node.prev = node
        new_node.next = temp
        temp.prev = new_node

    def _remove_node(self, node: ListNode) -> None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()