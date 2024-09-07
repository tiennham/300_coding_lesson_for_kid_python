from typing import Optional

from data.linked_list import ListNode
from data.tree_node import TreeNode

# Ý của bài này là dùng 2 cái list và sử dụng 2 list đó theo nguyên lý của cái stack để thực hiện các hàm push pop..
# Chứ bản thân cái list đã làm được tất cả các hàm push, pop ... rồi


class MyQueue:
    __items = []

    def __init__(self):
        self.__items = []

    def push(self, x: int) -> None:
        self.__items[len(self.__items) - 1] = x
        self.__items.append(x)

    def pop(self, **kwargs) -> int:
        x = self.__items[0]
        self.__items = self.__items[1:]
        return x

    def peek(self, **kwargs) -> int:
        x = self.__items[0]
        return x

    def empty(self) -> bool:
        return not self.__items


commands = ["MyQueue", "push", "push", "peek", "pop", "empty"]
values = [[], [1], [2], [], [], []]

my_queue = MyQueue()

for i in range(len(commands)):
    if commands[i] == "MyQueue":
        my_queue = MyQueue()
        continue
    cmd = getattr(my_queue, commands[i])
    if values[i]:
        for val in values[i]:
            cmd(val)
    else:
        cmd()

    print(commands[i])
    my_queue.print_items()
    print("==================")




