class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Stack:
  def __init__(self):
    self.head = None

  def push(self, data) -> None:
    # Write your code here
    new = Node(data)
    if self.head == None:
      new.next = None
      self.head = new
    else:
      new.next = self.head
      self.head = new

  def pop(self) -> None:
    # Write your code here
    if self.head == None:
      pass
    else:
      self.head = self.head.next

  def status(self):
    """
    It prints all the elements of stack.
    """
    # Write your code here
    trav = self.head
    while trav != None:
      print(trav.data, "=>",sep = "", end = "")
      trav = trav.next
    print("None")
    
# Do not change the following code
stack = Stack()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "push":
    stack.push(int(data[i]))
  elif operations[i] == "pop":
    stack.pop()
stack.status()
