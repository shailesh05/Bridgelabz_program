import array


class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head= None
        self.last_node=None

    def insert(self,data):
        if self.last_node is None:
            self.head =Node(data)
            self.last_node=self.head
        else:
            self.last_node.next=Node(data)
            self.last_node = self.last_node.next
    def print(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next
    def search(self,element):
        current=self.head
        while current != None:
            if current.data==element:
                return True
            current=current.next
        return False
    def delete (self,element):
        current=self.head
        while current != None:
            if self.head.data == element:
                self.head=self.head.next
                break
            if current.data == element:
                self.last_node.next=current.next
                break
            self.last_node= current
            current=current.next


    def write (self,element):
        f1=open('/home/admin1/Desktop/name.txt','w')
        f1.close()
        with open('/home/admin1/Desktop/name.txt','a') as f:
            f.write(','.join(str(word)for word in element))

my_list =LinkedList()
my_list=print()