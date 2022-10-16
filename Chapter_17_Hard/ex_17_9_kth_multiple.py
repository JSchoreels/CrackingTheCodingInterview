class SortedList:

    def __init__(self):
        self.list = []

    def insert(self, elt):
        prev_i = 0
        next_i = len(self.list)
        if len(self.list) == 0:
            self.list.append(elt)
            return
        if self.list[0] == elt or self.list[-1] == elt:
            return # ignore
        if elt > self.list[-1]:
            self.list.append(elt)
            return
        elif elt < self.list[0]:
            self.list.insert(0, elt)
            return
        while prev_i+1 != next_i:
            mid = prev_i + (next_i - prev_i) // 2
            if self.list[mid] < elt:
                prev_i = mid
            elif self.list[mid] > elt:
                next_i = mid
            else:
                return
        self.list.insert(mid, elt)
        return

    def peek(self):
        return self.list[0] if len(self.list) > 0 else None

    def pop(self):
        return self.list.pop(0)

    def __repr__(self):
        return self.list.__repr__()

def kth_multiple(k):
    queue_3 = SortedList()
    queue_3.insert(3)
    queue_5 = SortedList()
    queue_5.insert(5)
    queue_7 = SortedList()
    queue_7.insert(7)
    if k == 0:
        return 1
    else:
        i = 0
        while i < k:
            if first_has_min(queue_3, queue_5, queue_7):
                current = queue_3.pop()
                queue_3.insert(3*current)
                queue_5.insert(5*current)
            elif first_has_min(queue_5, queue_3, queue_7):
                current = queue_5.pop()
                queue_5.insert(5*current)
            elif first_has_min(queue_7, queue_3, queue_5):
                current = queue_7.pop()
            queue_7.insert(7*current)
            print(f"{i} : {current}")
            print(f"queue3 : {queue_3}")
            print(f"queue5 : {queue_5}")
            print(f"queue7 : {queue_7}")
            i += 1
    return current

def first_has_min(queue_A, queue_B, queue_C):
    return queue_A.peek() \
           and (queue_B.peek() and queue_A.peek() <= queue_B.peek()) \
           and (queue_C.peek() and queue_A.peek() <= queue_C.peek())




kth_multiple(100)
