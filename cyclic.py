from llist import *

def llprint(lst, num):
    """print the first num terms of linked list lst"""
    pass

def find_cycle(lst):
    """return the start index and length of the cycle"""
    pass


if __name__ == "__main__":

    lList = LList()
    temp = 1
    for i in range(15):
        node = Node(temp)
        lst = append(lList,node)
        if i == 10:
            temp2 = node
        print(node.val)
        temp *= 2
        if i == 14:
            node.next = temp2
            lst = append(lList,temp2)

