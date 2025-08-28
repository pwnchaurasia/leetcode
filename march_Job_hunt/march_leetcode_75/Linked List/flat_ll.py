class ListOfLists:
    class Node:
        def __init__(self, data, down=None, right=None):
            self.data_ = data
            self.down_ = down
            self.right_ = right

    def __init__(self):
        self.root_ = None

    def append(self, l):
        if self.root_ == None:
            self.root_ = l
        else:
            r = self.root_
            while r.right_:
                r = r.right_
            r.right_ = l

    def verify(self):
        curr = self.root_
        while curr is not None:
            assert curr.down_ is None
            print(curr.data_)
            curr = curr.right_

    def print(self):
        n = self.root_
        while n:
            d = n
            while d:
                print(d.data_)
                d = d.down_
            print('---')
            n = n.right_

    def flatten(self, head):
        # Implement this function
        current = head
        prev = current.right_

        while current:
            if current.down_ is None:
                current.right_ = prev
                cur_prev = prev.right_ if prev else None
                current = prev
                prev = cur_prev
            else:
                cur_down = current.down_
                current.down_ = None
                current.right_ = cur_down
                current = cur_down
        return head