class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.data = [None] * self.size

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, number):
        index = self.hash_function(key)
        new_contact = Contact(key, number)
        new_node = Node(key, new_contact)

        if self.data[index] is None:
            self.data[index] = new_node
        else:
            current = self.data[index]
            while current:
                if current.key == key:
                    current.value = new_contact
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def print_table(self):
        for i in range(self.size):
            print(f"Index {i}:", end=" ")
            if self.data[i] is None:
                print("Empty")
            else:
                current = self.data[i]
                while current:
                    print(f"- {current.value}", end=" ")
                    current = current.next
                print()




                       
# A hash table is the ideal structure for this contact management system because it provides constant-time average-case performance (O(1)) for insertions and lookups. Instead of scanning through an entire list like a linear search (O(n)), hashing converts a contact name into a numerical index, allowing near-instant access to the desired entry. This is crucial for systems that must handle hundreds of contacts efficiently on resource-limited devices. 
# I implemented a simple hash function by summing the ASCII values of characters in the name and taking the remainder when divided by the table size. This evenly distributes keys across the array for most inputs. Collisions — when two keys map to the same index—are handled using separate chaining. Each array index holds a linked list of Node objects, allowing multiple contacts to coexist in the same slot. When inserting, if a contact’s name already exists; its phone number is updated instead of creating a duplicate entry. 
# An engineer might choose a hash table over a list or tree when speed is the top priority, and data retrieval is based on unique keys, such as names or IDs. Lists are simpler but inefficient for searching large datasets, while trees maintain order but require more memory and time for balancing. For this project, the hash table strikes the best balance between simplicity, performance, and scalability. 