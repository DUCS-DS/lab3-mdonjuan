from llist import LList, Node, append


def length(lst):
    """return the length of a finite linked list"""
    current = lst.head
    size = 0
    while current is not None:
        size += 1
        current = current.next
    return size

def llprint(lst):
    """print a finite linked list"""
    if not lst.head:
        print("There is nothing", end =" ")
        return
    current = lst.head
    while current is not None:
        print(current.val,end = " ")
        current = current.next

if __name__ == "__main__":

    lst = LList()
    append(lst, Node(1))
    append(lst, Node(2))
    append(lst, Node(4))
    append(lst, Node(8))
    append(lst, Node(16))
    append(lst, Node(32))
    append(lst, Node(64))
    append(lst, Node(128))
    append(lst, Node(256))
    append(lst, Node(512))
    
    print("Length of LList: ", length(lst))
    llprint(lst)

    lst2 = LList()
    append(lst2, Node(1))
    append(lst2, Node(8))
    append(lst2, Node(12))
    append(lst2, Node(16))
    append(lst2, Node(20))
    
    print()
    print("Length of LList 2: ", length(lst2))
    llprint(lst2)

    lst3 = LList()

    print()
    print("Length of LList 3: ", length(lst3))
    llprint(lst3)
    
    from genfinite import lst
    print()
    print("Length of genfinite LList: ", length(lst))
