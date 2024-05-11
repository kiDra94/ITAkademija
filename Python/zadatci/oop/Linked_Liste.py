# Node class
class Node:
     
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # Initialize next as null

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None # Initialize head as None
 
    # This function insert a new node at the
    # beginning of the linked list
    def push(self, new_data):
     
        # Create a new Node
        new_node = Node(new_data)
 
        # 3. Make next of new Node as head
        new_node.next = self.head
 
        # 4. Move the head to point to new Node
        self.head = new_node

    def pisi(self):
        pom = self.head
        while pom != None:
            print(pom.data,end=" ")
            pom = pom.next

    def pronadji(self,x):
        pom = self.head
        while pom != None:
            if pom.data == x:
                return True
            pom = pom.next
        return False
    
    def len(self):
        brojac = 0
        pom = self.head
        while pom != None:
            brojac += 1
            pom = pom.next
        return brojac
    
    def pronadji_po_indeksu(self,index):
        pom = self.head
        if(self.len()<=index):
            return -1
        if index == 0:
            return pom.data
        for _ in range(index):
            pom = pom.next
        return pom.data
    
    def dodaj_na_kraj(self,x):
        pom = self.head
        while pom.next != None:
            pom = pom.next
        pom.next = Node(x)

    def pisi_rek(self,head):
        if head == None:
            return
        print(head.data,end=" ")
        self.pisi_rek(head.next)

    def pisi_rek_inverzno(self,head):
        if head == None:
            return
        self.pisi_rek_inverzno(head.next)
        print(head.data,end=" ")

# Code execution starts here
if __name__ == '__main__':
 
    # Start with the empty list
    llist = LinkedList()
 
    ''' Use push() to construct below list
        14->21->11->30->10 '''
    llist.push(10)
    llist.push(30)
    llist.push(11)
    llist.push(21)
    llist.push(14)
    llist.pisi()
    print()
    print(llist.pronadji_po_indeksu(5))
    print(llist.pronadji(30))
    llist.dodaj_na_kraj(77)
    llist.pisi()
    print()
    llist.pisi_rek(llist.head)
    print()
    llist.pisi_rek_inverzno(llist.head)

