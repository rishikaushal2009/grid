
dim = 3

class Node:
     
    def __init__(self, data):
       
        self.data = data
        self.prev = None
        self.up = None
        self.down = None
        self.next = None       
         
# function to create a 
# new node
def createNode(data):
 
    temp = Node(data);    
    return temp;
  
# function to construct the
# doubly linked list
def constructDoublyListUtil(mtrx, i, 
                            j, curr):
  
    if (i >= dim or
        j >= dim):
        return None;
      
    # Create Node with value 
    # contain in matrix at 
    # index (i, j)
    temp = createNode(mtrx[i][j]);
  
    # Assign address of curr into
    # the prev pointer of temp
    temp.prev = curr;
  
    # Assign address of curr into
    # the up pointer of temp
    temp.up = curr;
  
    # Recursive call for next 
    # pointer
    temp.next= constructDoublyListUtil(mtrx, i, 
                                       j + 1, 
                                       temp);
  
    # Recursive call for down pointer
    temp.down= constructDoublyListUtil(mtrx, 
                                       i + 1, 
                                       j, temp);
  
    # Return newly constructed node
    # whose all four node connected
    # at it's appropriate position
    return temp;
 
# Function to construct the
# doubly linked list
def constructDoublyList(mtrx):
 
    # function call for construct
    # the doubly linked list
    return constructDoublyListUtil(mtrx,
                                   0, 0, 
                                   None);


  
   
# function for displaying
# doubly linked list data
def display(head):
 
    # pointer to move right
    rPtr = None
  
    # pointer to move down
    dPtr = head;
  
    # loop till node->down 
    # is not NULL
    while (dPtr != None):
  
        rPtr = dPtr;
  
        # loop till node->right 
        # is not NULL
        while (rPtr != None):
            print(rPtr.data), 
 #                 end = ' ')
            rPtr = rPtr.next;
         
        print()
        dPtr = dPtr.down;
     
# Driver code
if __name__=="__main__":
     
    # initialise matrix
    mtrx =[[1, 2, 3], 
           [4, 5, 6], 
           [7, 8, 9]]
  
    list = constructDoublyList(mtrx); 
    display(list);