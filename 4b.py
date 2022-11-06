# Read an integer that denotes the the length of the list which is returned as the output of the algorithm
length_of_circular_linked_list = int(input())
# Read space-separated integers that denote the elements of the list which is returned as the output of the algorithm
circular_linked_list = list(map(int,input().strip().split(" ")))


final_list = [circular_linked_list[i] for i in range(3)]
for i in circular_linked_list:
    if i not in final_list:
        final_list.append(i)

print(len(final_list))
for i in final_list:
    print(i,end=" ")
