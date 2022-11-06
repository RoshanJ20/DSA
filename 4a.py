from typing import Optional


class Node:
    """
    This class describes Node objects to act as elements of the LinkedList
    Attributes:
        -> data - stored associated data
        -> next - link to next node
    """

    def __init__(self, data=None, next=None):
        """
        Initialises the Node with given attributes
        """
        self.data = data
        self.next = next


class LinkedList:
    """
    This class implements LinkedList using Node objects
    Methods:
        -> insert_at_end - inserts node with data at the end of the list
        -> status - displays all elements of the lisT
    Attributes
        -> self.head - contains first node of LinkedList, None if list empty
    """

    def __init__(self):
        """
        Initialize the head
        """
        self.head = None

    def insert_at_end(self, data):
        """
        Insert node at end of the list
        :param data: integer data that will be used to create a node
        """
        new = Node(data, None)
        curr = self.head
        if curr is None:
            self.head = new
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = new

    def status(self):
        """
        It prints all the elements of list.
        """
        elements = []
        curr = self.head
        while curr:
            elements.append(curr.data)
            curr = curr.next
        print(elements)


class Solution:
    """
    Class implementing functions to add numbers in a LinkedListT
    
    """

    def addTwoNumbers(self, first_list: Optional[LinkedList], second_list: Optional[LinkedList]) -> Optional[
        LinkedList]:
        """
        :param first_list: Linkedlist with non-negative integers
        :param second_list: Linkedlist with non-negative integers
        :return: returns the sum as a linked list
        """
        result = self.get_num(first_list) + self.get_num(second_list)
        sum_list = LinkedList()
        for digit in list(map(int, str(result)[::-1])):
            sum_list.insert_at_end(digit)
        return sum_list

    def get_num(self, l: Optional[LinkedList]) -> int:
        """
        :param l: LinkedList with non-negative integers
        :return: returns digits of the list as a single integer
        """
        curr = l.head
        if curr is None:
            return 0
        num = ""
        while curr is not None:
            num = str(curr.data) + num
            curr = curr.next
        return int(num)


# Do not edit the following code
# Create an instance for LinkedList
first_list = LinkedList()
# Create an another instance for LinkedListT
second_list = LinkedList()
# Read data for first list
data_for_first_list = list(map(int, input().strip().split(" ")))
# Add data at the end of first_list
for data in data_for_first_list:
    first_list.insert_at_end(data)
# Read data for second list
data_for_second_list = list(map(int, input().strip().split(" ")))
# Add data at the end of second_list
for data in data_for_second_list:
    second_list.insert_at_end(data)
# Create an instance for Solution
solution = Solution()
# Pass first_list and second_list to addTwoNumbers, which returns a new linked list
new_list = solution.addTwoNumbers(first_list, second_list)
# Display the status of new_list
new_list.status(
