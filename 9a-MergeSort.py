from typing import List

def merge_sort(data):
    if len(data)>1:
        mid = len(data)//2
        lefthalf = data[:mid]
        righthalf = data[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                data[k]=lefthalf[i]
                i=i+1
            else:
                data[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            data[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            data[k]=righthalf[j]
            j=j+1
            k=k+1


# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
merge_sort(data)
print(data)
