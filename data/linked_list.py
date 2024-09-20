class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def build_linked_list_from_list(values):
        node_lst = []
        for i in values:
            node_lst.append(ListNode(i))

        for i in range(len(node_lst)):
            node_lst[i].next = node_lst[i+1] if i+1 < len(node_lst) else None

        return node_lst[0]

    @staticmethod
    def print_linked_list(head):
        current = head
        lst_val = []
        while current:
            lst_val.append(str(current.val))
            current = current.next

        print(" => ".join(lst_val))

    @staticmethod
    def build_cycle_linked_list(values, pos):
        if len(values) < 2:
            print("length must be greater than 2")
            return None
        node_lst = []
        for i in values:
            node_lst.append(ListNode(i))

        for i in range(len(node_lst)):
            if i + 1 < len(node_lst):
                node_lst[i].next = node_lst[i + 1]

        node_lst[-1].next = node_lst[pos]

        return node_lst[0]






