class Node(object):
    def __init__(self,item):
        self.elem = item
        self.next = None
        self.prior = None


class DoubleLinkList(object):
    """双链表"""
    def __init__(self, node=None):
        self.__head = node
    def is_empty(self):
        return self.__head is None
    def length(self):
        cur = self.__head
        count = 0
        while cur is not None:
            cur = cur.next
            count += 1
        return count
    def travel(self):
        cur = self.__head
        li = []
        while cur is not None:
            li.append(cur.elem)
            cur = cur.next
        return li
    def add(self,item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            node.next = self.__head
            self.__head.piror = node
            self.__head = node
    def append(self,item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prior = cur
    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            pre = self.__head
            count = 0
            while count < pos-1:
                pre = pre.next
                count += 1
            node.next = pre.next
            pre.next.prior = node
            node.prior = pre
            pre.next = node
    def search(self,item):
        cur = self.__head
        count = 0
        while cur is not None:
            if cur.elem == item:
                return count
            cur = cur.next
            count += 1
        return -1
    def remove(self,item):
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                if cur == self.__head:  # 判断是否为头节点
                    self.__head = cur.next
                    if cur.next:  # 判断是否只有一个节点
                        cur.next.prior = None
                else:
                    cur.prior.next = cur.next
                    if cur.next:
                        cur.next.prior = cur.prior
                    break
            cur = cur.next


data = Node(3)
dll = DoubleLinkList(data)

if __name__ == "__main__":
    print(dll.is_empty())
    dll.add(12)
    dll.append(20)
    dll.insert(1,8)
    print(dll.length())
    dll.remove(20)
    print(dll.travel())
    print(dll.search(20))
