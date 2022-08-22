# 문제
# # 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
# #
# # 명령은 총 다섯 가지이다.
# #
# # push X: 정수 X를 스택에 넣는 연산이다.
# # pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# # size: 스택에 들어있는 정수의 개수를 출력한다.
# # empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# # top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# # 입력
# # 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.
# #
# # 출력
# # 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            new_head = Node(value)
            new_head.next = self.head
            self.head = new_head

    def pop(self):
        if self.head is None:
            return -1

        value = self.head.value
        self.head = self.head.next
        return value

    def size(self):
        num = 0
        cur = self.head
        while cur is not None:
            num += 1
            cur = cur.next

        return num

    def empty(self):
        if self.head is None:
            return 1
        return 0

    def top(self):
        if self.head is None:
            return -1
        return self.head.value


def main():
    n = int(input("input N : "))
    cmd_list = []
    stk = Stack()


    for _ in range(n):
        cmd = input("input Command : ").split()
        cmd_list.append(cmd)

    for cmd in cmd_list:
        if cmd[0] == "push":
            value = int(cmd[1])
            stk.push(value)
        elif cmd[0] == "pop":
            print(stk.pop())
        elif cmd[0] == "size":
            print(stk.size())
        elif cmd[0] == "empty":
            print(stk.empty())
        elif cmd[0] == "top":
            print(stk.top())
        else:
            print("Incorrect Command")


main()