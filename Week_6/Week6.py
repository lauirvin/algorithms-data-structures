
class BinTreeNode(object):
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
       
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree
 #change search to return the needed node and its parent
def searchNode(self, tree, target):
    if tree.value == target:
        return tree
    elif target > tree.value:
        return searchNode(tree.left, target)
    else:
        return searchNode(tree.right, target)
 
def deleteNode(self, value, node = None):          
     if node == None:              #data not found
        node = self.searchNode(value)

     #Searrch for Node we wish to delete HERE.
        
     #If we find it then we can delete
     if value == node.value: # if founds the node you want to delete
        if node.left == None and node.right == None: #if node has no childen
           if node < parent.value:                   #if child node is less than parent node value
               parent.left = None #this is removing the reference to the node (deleting it)
           else:
               parent.right = None
           return  
        
        elif node.left and node.right == None: #remove-node left child node only (case for single children)
             if node < parent.value:           #check if node is a left child or right child of its parent
                 parent.left = node.left   #if left child, we assign it to the parent child
             else:
                 parent.right = node.left # same but for right
             return               
        
        elif node.left == None and node.right:#remove-node right child (case for single children)
            if node < parent.value:          #same as remove left node above
                parent.left = node.right    #if right child, we assign it to the parent child
            else :
                parent.right = node.right
            return      
        
        elif node.right == None and node.left: # remove two children (using max values)
            maxvalue = self.max(node)          #replace deleted node with the value
            node.value = maxvalue.value
            maxvalue.parent.right = None
            return  

def max(self,node): #finding the max value (from the left subtree)
    root = node
    if node == None:
        node = self.node
    
    if node.left != None:
        node = node.left
    else:
        return node
    if node.right != None:
        return self.max(node = node.right)

def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)
 
def in_order(tree):
    if(tree.left!=None):
        in_order(tree.left)
    print (tree.value)
    if(tree.right!=None):
        in_order(tree.right)
 
if __name__ == '__main__':
   
  t=tree_insert(None,6)
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  deleteNode(t,6) #deleting the node 11
  in_order(t)

