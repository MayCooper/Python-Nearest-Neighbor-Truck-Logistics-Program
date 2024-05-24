"""
Implements a dynamic hash table that automatically resizes based on load factor. This approach helps maintain
optimal performance by balancing the number of entries with the bucket size, reducing collision and improving
lookup efficiency.

"""
# Sets up the hash table with an initial capacity and a threshold for resizing. 
# This method prepares the underlying data structures needed for the hash table operations.
class ResizableDict:
    def __init__(self, capacity=10, load_factor_threshold=0.7):
        """
        Complexity:
            Time: O(n) - Initializes 'n' empty buckets for storing key-value pairs.
            Space: O(n) - Allocates space for 'n' buckets, each capable of holding multiple entries.
            Note:
                - Time: I initialize a list with 'n' empty lists, which takes linear time relative to 'n'.
                - Space: The space is proportional to the capacity 'n' as each bucket is an empty list.
        """
        # Initialize hash table with specified capacity and load factor threshold.
        self._buckets = [[] for _ in range(capacity)] # Create empty buckets based on the initial capacity.
        self._count = 0 # Track the number of key-value pairs stored.
        self._load_factor_threshold = load_factor_threshold # Set the threshold for resizing.

# Determines the appropriate bucket index for a given key using Python's built-in hash function and modulo operation.
    def _hash(self, key):
        """
        Complexity:
            Time: O(1) - Hashing and modulo calculation are done in constant time.
            Space: O(1) - This method does not require additional space; it simply computes an index.
            Note:
              - Both the hash function and the modulo operation are constant-time operations regardless of input size.
        """
        return hash(key) % len(self._buckets)

# Increases the hash table's capacity and rehashes all existing key-value pairs into new buckets.
# This method is called when the number of elements exceeds the capacity times the load factor threshold.
    def _resize(self, new_capacity):
        """
        Complexity:
            Time: O(n) - Iterates through all existing entries to rehash them into the new bucket structure.
            Space: O(n) - Temporary additional space is needed during the resizing process to hold the new bucket array.
            Note:
                - Time: Must traverse each existing entry and re-insert it, which depends on the number of entries 'n'.
                - Space: A new, larger array of buckets is created, doubling the previous capacity, thus requiring additional space.
        """
        # Rehash all entries into a new set of buckets with increased capacity.
        old_buckets = self._buckets  # Store the current buckets.
        self._buckets = [[] for _ in range(new_capacity)]  # Create new empty buckets at the new capacity.
        self._count = 0  # Reset count to 0, will be updated in `put`.

        # Reinsert each key-value pair into the new buckets.
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)  # Rehash key-value pairs into the new buckets.

# Inserts a new key-value pair or updates the value of an existing key. The method ensures that
# if the load factor threshold is exceeded, the table is resized before adding the new entry.
    def put(self, key, value):
        """        
        Complexity:
            Time: Average O(1), Worst O(n) - Normally quick but may degrade to linear time if many collisions occur.
            Space: O(1) - The memory footprint does not increase with the number of entries added.
            Note:
                - Normally, the insertion is direct (O(1)). However, resizing (when necessary) involves rehashing all entries.
        """
        # Put a key-value pair into the hash table, resizing if necessary.
        if self._count / len(self._buckets) >= self._load_factor_threshold:
            self._resize(2 * len(self._buckets))  # Resize if load factor exceeds threshold.

        bucket_index = self._hash(key)  # Get bucket index for the key.
        bucket = self._buckets[bucket_index]  # Retrieve bucket by index.

        # Update value if key exists, else append new key-value pair.
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return  # Exit after update to avoid adding duplicate.

        bucket.append([key, value])  # Add new key-value pair.
        self._count += 1  # Increment count of items in the hash map.

# Retrieves the value for a given key from the hash table. Performance varies based on collision occurrence.
    def get(self, key):
        """      
        Complexity:
            Time: Average O(1), Worst O(n) - Typically fast but can slow down if the bucket has many collisions.
            Space: O(1) - Retrieving an item does not require additional space beyond the existing data structure.
            Note:
                - Retrieval time depends on the number of collisions in the bucket, which can potentially be many.
        """
        bucket_index = self._hash(key)  # Compute bucket index for the key.
        bucket = self._buckets[bucket_index]  # Access the corresponding bucket.

        # Search for the key in the bucket.
        for pair in bucket:
            if pair[0] == key:
                return pair[1]  # Return the value if the key is found.

        return None  # Return None if the key is not found.

# Deletes a key-value pair from the hash table, if the key exists.  
    def remove(self, key):
        """
        Complexity:
            Time: Average O(1), Worst O(n) - Fast in most cases but may take longer if the key is in a long bucket list.
            Space: O(1) - No additional space is needed for deletion.
            Note:
                - While deletion from the list is typically quick, searching through a long list can take linear time.
        """
        # Remove a key-value pair from the hash table if the key exists.
        bucket_index = self._hash(key)  # Compute the bucket index for the key.
        bucket = self._buckets[bucket_index]  # Access the bucket containing the key.

        # Iterate over the bucket to find and delete the key-value pair.
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                del bucket[i]  # Delete the pair.
                self._count -= 1  # Decrement the count of items.
                return True  # Return True to indicate successful deletion.

        return False  # Return False if the key was not found.

# Provides the total number of entries in the hash table. Useful for monitoring the table's size and for debugging.
    def count(self):
        """
        Complexity:
            Time: O(1) - Accessing the count is a direct read operation.
            Space: O(1) - No extra space is utilized to fetch this count.
        """
        return self._count
    
# Yields all key-value pairs in the hash table, allowing iteration over the table's contents.
    def items(self):
        """        
        Complexity:
            Time: O(n) - Needs to traverse every bucket and each entry within them.
            Space: O(1) - Yields elements one at a time, thus maintaining a constant space complexity.
            Note:
                - Must iterate over all entries to yield them, but this operation does not increase memory usage.
        """
        for bucket in self._buckets:  # Iterate through each bucket.
            for key, value in bucket:  # Iterate through each key-value pair in the bucket.
                yield key, value  # Yield the key-value pair.

