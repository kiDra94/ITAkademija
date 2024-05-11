class LList:
    def __init__(self):
        self.__head = None
        self.__length = 0 
        self.__current = None
    def add(self,val):
        if not self.__head:
            self.__head = ListItem(val)
            self.__length+=1
            return
        next = self.__head
        while next.next:
            next = next.next
        next.next = ListItem(val)
        self.__length+=1
        next.next.prev = next
    def __get(self,index):
        next = self.__head
        cnt = 0
        if not next:
            return None
        while next:
            if cnt == index:
                return next
            cnt+=1
            next = next.next
        return None 
    def get(self,index):
        for_get = self.__get(index)
        if for_get:
            return for_get.val
        else:
            return None 
    def remove(self,index):
        for_remove = self.__get(index)
        if for_remove:
            if for_remove.prev:
                for_remove.prev.next = for_remove.next
            else: 
                self.__head = for_remove.next
                if for_remove.next :
                    for_remove.next.prev = None
            self.__length-=1
    def size(self):
        return self.__length 
    def sort(self,sorter): 
        if self.__head and self.__head.next: 
            next = self.__head.next
            while True:
                has_sort = False
                
                while next: 
                    if sorter(next.prev.val,next.val):  

                        #Implementirati 
                         

                        has_sort = True 

                    next = next.next
                    
                if not has_sort:
                    break 

    def __iter__(self):
        self.__current = self.__head
        return self
    def __next__(self):
        n = self.__current
        if n:
            self.__current = n.next
            return n.val
        else:
            raise StopIteration

class ListItem:
    def __init__(self,val):
        self.next   = None
        self.prev   = None
        self.val    = val

l = LList()

l.add(6)
l.add(3)
l.add(5)
 
l.sort(lambda a,b : b<a)

for i in l:
    print(i)


