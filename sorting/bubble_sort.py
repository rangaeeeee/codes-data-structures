import random

def bubble_sort(data):
  print("before bubble sort")
  print_list(data)
  length = len(data)
  if(len(data) < 2):
    return
  else:
    for i in range(length-1):
      for j in range(0,length-1-i):
        if (data[j] > data[j+1]):
          temp = data[j]
          data[j] = data[j+1]
          data[j+1] = temp
  print("after sort")
  print_list(data)

def print_list(data):
  for i in data:
    print(i,end=" ")
  print()

def generate_random(size):
    random_list = [] 
    for _ in range(size):
        random_list.append(random.randrange(10))
    return random_list

def main():
    iList = generate_random(5)
    bubble_sort(iList)

if __name__ =='__main__':
    main()
