class LList:
    def __init__(self):
        self.__head = None
    def add(self,val):
        if not self.__head:
            self.__head = ListItem(val)
            return
        next = self.__head
        while next.next:
            next = next.next
        next.next = ListItem(val)
    def get(self,index):
        next = self.__head
        cnt = 0
        if not next:
            return None
        while next:
            if cnt == index:
                return next.val
            cnt+=1
            next = next.next
        return None 
class ListItem:
    def __init__(self,val):
        self.next   = None
        self.val    = val

l = LList()

l.add("Hello")
l.add("How are")
l.add("You")

msg = l.get(2)
print(msg)