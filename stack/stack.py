class stack:
  def __init__(self):
    self.size = 0
    self.limit = 1
    self.data = []
    
  def over_flow(self):
    return self.size == self.limit
    
  def under_flow(self):
    return self.size == 0

  def push(self,data):
    if not self.over_flow():
      self.data.append(data)
      self.size += 1
    else:
      print("stack over flow")
    
  def pop(self):
    temp  = None
    if not self.under_flow():
      temp = self.data[-1]
      self.data.remove(self.data[-1])
      self.size -= 1
    else:
      print("stack under flow")
    return temp
    
  def peek(self):
    if not self.under_flow():
      return self.data[-1]
    else:
      print("stack under flow")
    
  def print_stack(self):
    print("stack data :")
    for data in self.data:
      print(data,end=" ") 
    print()


def main():
  st = stack()
  st.print_stack()
  st.push(5)
  st.push(10)
  st.print_stack()
  print("peek : "  + str(st.peek()))
  st.print_stack()
  st.pop()
  st.print_stack()
  st.pop()
  st.print_stack()
  st.pop()
  

if __name__ == '__main__':
  main()