class MyCircularQueue:
    def __init__(self, size: int):
        self.queue = [0] * size
        self.size = size
        self.front, self.rear = -1, -1

    def enqueue(self, value: int) -> bool:
        if self.is_full():
            return False
        if self.front == -1:
            self.front, self.rear = 0, 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        return True

    def dequeue(self) -> bool:
        if self.is_empty(): 
            return False
        if self.front == self.rear:
            self.front, self.rear = -1, -1
        else:
            self.front = (self.front + 1) % self.size
        return True

    def get_front(self) -> int:
        if not self.is_empty():
            return self.queue[self.front]
        return -1

    def get_rear(self):
        if not self.is_empty():
            return self.queue[self.rear]
        return -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.front == 0 and self.rear == (self.size - 1)) or (self.front == (self.rear + 1) % self.size)


# Do not change the following codeT
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
data = []
for item in input().split(','):
    item = item.strip()
    if item == '-':
        data.append([])
    else:
        data.append([int(item)])
obj = MyCircularQueue(data[0][0])
result = []
for i in range(len(operations)):
    if i == 0:
        result.append(None)
    elif operations[i] == "enqueue":
        result.append(obj.enqueue(data[i][0]))
    elif operations[i] == "get_rear":
        result.append(obj.get_rear())
    elif operations[i] == "get_front":
        result.append(obj.get_front())
    elif operations[i] == "dequeue":
        result.append(obj.dequeue())
    elif operations[i] == "is_full":
        result.append(obj.is_full())
    elif operations[i] == "is_empty":
        result.append(obj.is_empty())

print(result)
