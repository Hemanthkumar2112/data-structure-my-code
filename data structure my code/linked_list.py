class Node:
    def __init__(self , val):
        self.val = val
        self.next = None
    def getItem(self):
        return self.val
    def getNext(self):
        return self.next
    
    
class LinkedList:
    def __init__(self ,head = None):
        self.head = None
        self.count = 0
        
    def lenght(self):
        return self.count
    def insert(self,item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.count +=1

    def display(self):
        all_ele = self.head
        while all_ele.getNext() != None:
            print(all_ele.getItem() , all_ele.getNext())
            all_ele = all_ele.getNext()
            
    def is_empty(self):
        return self.head == None

    def del_all(self):
        self.head = None
        self.count = 0
        return "flushed"
    
    def find(self ,item):
        all_ele = self.head
        index = 0
        while all_ele.getNext() != None:
            if all_ele.getItem() == item:
                return "item present in {} index in queue".format(index)
            
            all_ele = all_ele.next
            index +=1
        return "item not present"

x = LinkedList()
for i in range(40):
    x.insert(i)

x.display()
