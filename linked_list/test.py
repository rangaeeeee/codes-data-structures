class node:
   def __init__(self, val):
      self.value = val
      self.next = None

class llist:

   def __init__(self):
      self.val = None
      self.head = None
   
   def addFront(self, val):
       temp = node(val)
       temp.next = self.head
       self.head = temp

def loadList():
   ll = llist()
   for i in range(11):
      ll.addFront(i)
   return ll

def main():
   a = node(10)
   b = node(10)
   print a.value
   print a.next
   out = loadList()
   tn = out.head
   while tn.next:
      print tn.value
      tn = tn.next

if __name__ == "__main__":
   main()
