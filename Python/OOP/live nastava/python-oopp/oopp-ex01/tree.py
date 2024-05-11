class TreeNode:
    def __init__(self,key,val):
        self.val    = val
        self.key    = key
        self.left   = None
        self.right  = None

class Tree:
    def __init__(self):
        self.__root = None

    def __get(self,k,target):
        if k == target.key:
            return target.val
        else:
            if k<target.key:
                return self.__get(k,target.left)
            else:
                return self.__get(k,target.right)

    def get(self,k):
        if self.__root:
            return self.__get(k,self.__root)
        else:
            return None

    def __add(self,target,node): 
        if node.key == target.key:
            target.val = node.val
        elif node.key < target.key:
            if target.left:
                self.__add(target.left,node)
            else:
                target.left = node
        else:
            if target.right:
                self.__add(target.right,node)
            else:
                target.right = node

    def add(self,k,v):
        newNode = TreeNode(k,v)
        if not self.__root:
            self.__root = newNode
        else:
            self.__add(self.__root,newNode)


t = Tree()
t.add(5,"Hello")
t.add(10,"How")
t.add(3,"Are")
t.add(8,"You")  
print(t.get(3))



