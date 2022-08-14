from random import randrange
from xml.dom.minidom import Element


class linked_list:
    def __init__(self ,element) -> None:
        self.element = element 
        self.next = None


def insert(root,item):
    temp = linked_list(item)
    if root == None:
        root = temp
    else:
        temp2 = root
        while temp2.next !=None:
            temp2 = temp2.next
        temp2.next = temp
    return root

def display(root):
    while root.next !=None:
        print(root.element , root.next)
        root = root.next

###test
root = None
for i in range(10):
    root = insert(root,i)

display(root=root)

        
