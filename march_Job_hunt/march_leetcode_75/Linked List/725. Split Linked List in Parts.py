class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None




def split_ll_in_parts(head, k):
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next

    ele_size = length // k
    remainder = length % k

    curr = head
    res = []
    while curr:
        part_size = ele_size + (1 if remainder > 0 else 0)
        remainder -= 1

        part_head = curr
        prev = None
        for _ in range(part_size):
            prev = curr
            curr = curr.next

        if prev:
            prev.next = None
        res.append(part_head)

    while len(res) < k:
        res.append(None)

    return res



if __name__ == "__main__":
    head = [1,2,3]
    k = 5
