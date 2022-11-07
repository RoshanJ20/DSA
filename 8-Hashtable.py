import re

def display_hash(hashtable) -> None:
	"""
	Displays elements stored at each position of the hash table.
	"""
	for keyvalue in range(len(hashtable)):
		content = hashtable[keyvalue]
		print(keyvalue, end = " ")
		for element in content:
			print("-->", element, end = " ")
		print()

def Hashing(keyvalue) -> int:
	"""
	Returns the ouput of the hash function for the given key value.
	"""
	return keyvalue % len(HashTable)

def insert(Hashtable, keyvalue, value) -> None:
	"""
	Inserts the value at the position of the hastable returned by applying the hash function to keyvalue.
	"""
	Hashtable[Hashing(keyvalue)].append(value)


# Do not edit the following code
hash_table_size = int(input())
# Create Hashtable as a list of list.
HashTable = [[] for _ in range(hash_table_size)]
input_data = input()
data = []
for item in re.split('], |].', input_data):
  item = item[1:]
  data = item.split(', ')
  if len(data) > 1:
    insert(HashTable, int(data[0]), data[1])

display_hash(HashTable)
