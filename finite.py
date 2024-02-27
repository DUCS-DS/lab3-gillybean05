from llist import LList, Node, append


def length(lst):
    """return the length of a finite linked list"""
    temp = lst.head
    it = 0
    while temp:
        it+=1
        temp = temp.next

    return it



def llprint(lst):
    """print a finite linked list"""
    temp = lst.head
    string = ''
    while temp.next:
        string += str(temp.val)+", "
        temp = temp.next

    string += str(temp.val)
    return string


if __name__ == "__main__":

    lList = LList()
    temp = 1
    for i in range(10):
        node = Node(temp)
        lst = append(lList,node)
        print(node.val)
        temp *= 2
    print()
    print(length(lList))
    print(llprint(lList))

    from genfinite import lst
    print(length(lst))