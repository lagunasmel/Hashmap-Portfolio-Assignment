# hash_map.py
# ===================================================
# Implement a hash map with chaining
# ===================================================


class SLNode:
    def __init__(self, key, value):
        self.next = None
        self.key = key
        self.value = value

    def __str__(self):
        return '(' + str(self.key) + ', ' + str(self.value) + ')'


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_front(self, key, value):
        """Create a new node and inserts it at the front of the linked list
        Args:
            key: the key for the new node
            value: the value for the new node"""
        new_node = SLNode(key, value)
        new_node.next = self.head
        self.head = new_node
        self.size = self.size + 1

    def remove(self, key):
        """Removes node from linked list
        Args:
            key: key of the node to remove """
        if self.head is None:
            return False
        if self.head.key == key:
            self.head = self.head.next
            self.size = self.size - 1
            return True
        cur = self.head.next
        prev = self.head
        while cur is not None:
            if cur.key == key:
                prev.next = cur.next
                self.size = self.size - 1
                return True
            prev = cur
            cur = cur.next
        return False

    def contains(self, key):
        """Searches linked list for a node with a given key
        Args:
            key: key of node
        Return:
            node with matching key, otherwise None"""
        if self.head is not None:
            cur = self.head
            while cur is not None:
                if cur.key == key:
                    return cur
                cur = cur.next
        return None

    def __str__(self):
        out = '['
        if self.head is not None:
            cur = self.head
            out = out + str(self.head)
            cur = cur.next
            while cur is not None:
                out = out + ' -> ' + str(cur)
                cur = cur.next
        out = out + ']'
        return out


def hash_function_1(key):
    hash = 0
    for i in key:
        hash = hash + ord(i)
    return hash


def hash_function_2(key):
    hash = 0
    index = 0
    for i in key:
        hash = hash + (index + 1) * ord(i)
        index = index + 1
    return hash


class HashMap:
    """
    Creates a new hash map with the specified number of buckets.
    Args:
        capacity: the total number of buckets to be created in the hash table
        function: the hash function to use for hashing values
    """

    def __init__(self, capacity, function):
        self._buckets = []
        for i in range(capacity):
            self._buckets.append(LinkedList())
        self.capacity = capacity
        self._hash_function = function
        self.size = 0

    def clear(self):
        """
        Empties out the hash table deleting all links in the hash table.
        """
        self._buckets = []
        for i in range(self.capacity):
            self._buckets.append(LinkedList())
        self.size = 0


    def get(self, key):
        """
        Returns the value with the given key.
        Args:
            key: the value of the key to look for
        Return:
            The value associated to the key. None if the link isn't found.
        """
        # Find the index
        index = self._hash_function(key) % self.capacity
        # Grab the node
        node = self._buckets[index].contains(key)
        # If the link
        if node is not None:
            return node.value
        else:
            return None

    def get_buckets(self):
        """Returns the buckets list."""
        return self._buckets

    def resize_table(self, capacity):
        """
        Re-sizes the hash table to have a number of buckets equal to the given
        capacity. All links need to be rehashed in this function after resizing
        Args:
            capacity: the new number of buckets.
        """
        # Create a new array and initiate new linked lists
        temp = []
        for num in range(capacity):
            temp.append(LinkedList())

        # Iterate through each linked list in the previous array and retrieve new hashes
        # Add these into new existing array
        for bucket in self._buckets:
            if bucket.head is not None:
                curr = bucket.head
                while curr is not None:
                    new_index = self._hash_function(curr.key) % capacity
                    temp[new_index].add_front(curr.key, curr.value)
                    curr = curr.next
        # Update buckets to point to new array
        self._buckets = temp
        # Update to new capacity
        self.capacity = capacity


    def put(self, key, value):
        """
        Updates the given key-value pair in the hash table. If a link with the given
        key already exists, this will just update the value and skip traversing. Otherwise,
        it will create a new link with the given key and value and add it to the table
        bucket's linked list.

        Args:
            key: they key to use to has the entry
            value: the value associated with the entry
        """
        index = self._hash_function(key) % self.capacity
        node = self._buckets[index].contains(key)
        # Point to the linked list in this index
        if node is not None:
            node.value = value
        else:
            self._buckets[index].add_front(key, value)
            self.size += 1

    def remove(self, key):
        """
        Removes and frees the link with the given key from the table. If no such link
        exists, this does nothing. Remember to search the entire linked list at the
        bucket.
        Args:
            key: they key to search for and remove along with its value
        """
        index = self._hash_function(key) % self.capacity

        if self.contains_key(key) is True:
            self._buckets[index].remove(key)
            self.size -= 1
        else:
            return


    def contains_key(self, key: object) -> object:
        """
        Searches to see if a key exists within the hash table

        Returns:
            True if the key is found False otherwise

        """
        index = self._hash_function(key) % self.capacity
        # Used the contains method for the linked list to see if it's in the bucket
        if self._buckets[index].contains(key) is not None:
            return True
        else:
            return False

    def empty_buckets(self):
        """
        Returns:
            The number of empty buckets in the table
        """
        count = 0
        # Find buckets with empty heads and increment count
        for bucket in self._buckets:
            if bucket.head is None:
                count += 1
        return count


    def table_load(self):
        """
        Returns:
            the ratio of (number of links) / (number of buckets) in the table as a float.

        """
        return float(self.size/self.capacity)

    def __str__(self):
        """
        Prints all the links in each of the buckets in the table.
        """

        out = ""
        index = 0
        for bucket in self._buckets:
            out = out + str(index) + ': ' + str(bucket) + '\n'
            index = index + 1
        return out
