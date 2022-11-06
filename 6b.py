class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Queue:
  def __init__(self):
    self.head = None
    self.last = None

  def enqueue(self, data) -> None:
    # Write your code here
    new = Node(data)
    if self.head == None:
      new.next = None
      self.head = new
      self.last = new
    else:
      self.last.next = new
      new.next = None
      self.last = new

  def dequeue(self) -> None:
    # Write your code here
    if self.head == None:
      pass
    else:
      self.head = self.head.next
      

  def status(self) -> None:
    # Write your code here
    trav = self.head
    while trav != None:
      print(trav.data, "=>", sep = "", end = "")
      trav = trav.next
    print("None")
    
# Do not change the following code
queue = Queue()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "enqueue":
    queue.enqueue(int(data[i]))
  elif operations[i] == "dequeue":
    queue.dequeue()
queue.status()
