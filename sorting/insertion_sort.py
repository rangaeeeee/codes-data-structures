def print_list(data):
  for i in data:
    print(i,end=" ")
  print()
  
def move_elements(data,start,end,element):
  length = end- start
  if length == 1:
    data[start] = element
    return
  else:
    for i in range(length):
      temp = data[start+i]
      data[start+i] = element
      element = temp

def insertion_sort(data):
  print("before bubble sort")
  print_list(data)
  length = len(data)
  print("----------")
  for i in range(1,length):
    for j in range(i+1):
      if data[j] > data[i]:
        temp = data[j]
        data[j] = data[i]
        move_elements(data,j+1,i+1,temp)
        
        break
  print("--------")
  print("after sort")
  print_list(data)
  

def main():
  data_list =[12,11,13,5,6]
  insertion_sort(data_list)
  
if __name__ == '__main__':
  main()
