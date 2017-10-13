class node:
  def __init__(self,data):
    self.data = data
    self.next = None

class linked_list:
  def __init__(self):
    self.head = None
    self.length = 0
    
  def addFront(self, val):
    temp = node(val)
    temp.next = self.head
    self.head = temp
    
  def add_node(self, data):
    if self.head == None:
      self.head = node(data)
      self.length += 1
    else:
      temp = self.head
      while(temp.next):
        temp = temp.next
      temp.next = node(data)
      self.length += 1
      
  def list_length(self):
    return self.length
    
  def reverse_list(self):
    if self.head == None:
      print("cannot reverse empty list")
      return
      
    if self.head.next == None:
      print("list has one element and cannot reverse")
      return
    
  def remove_node(self, data):
    temp = self.head
    if temp == None:
      # list is empty
      return
    else:
      if temp.data == data:
        self.head = self.head.next
        return
        
      if temp.next == None:
        print("data node not found to remove")
        return
        
      previous = temp
      current  = temp
      next     = temp.next
      while next != None:
        if current.data == data:
          previous.next = next
          return
        previous = current
        current = next
        next = next.next
        
      if current.data == data:
        previous.next = None
    
  def detect_loop(self):
    pass
    
  def remove_loop(self):
    pass
 
  def print_list(self):
    print("linked list data")
    temp = self.head
    while(temp):
      print(temp.data, end=" ")
      temp = temp.next
    print()

def main():
  llist = linked_list()
  llist.add_node(5)
  llist.add_node(10)
  llist.add_node(15)
  print("length of linked list : " + str(llist.list_length()))
  llist.print_list()
  llist.remove_node(10)
  llist.remove_node(15)
  llist.print_list()

if __name__ == '__main__':
  main()