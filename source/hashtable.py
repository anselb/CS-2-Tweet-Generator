#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        values_list = []

        for linked_list in self.buckets:
            for key_value_tuple in linked_list.items():
                values_list.append(key_value_tuple[1])

        return values_list

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket

        # could be done with 1 line with comprehension
        # return sum(bucket.length() for bucket in self.buckets)

        total_entries = 0

        for linked_list in self.buckets:
            total_entries += linked_list.length()

        return total_entries

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        key_bucket = self._bucket_index(key)
        in_hash_table = False

        for key_value_tuple in self.buckets[key_bucket].items():
            if key_value_tuple[0] is key:
                in_hash_table = True

        return in_hash_table

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        key_bucket = self._bucket_index(key)

        for key_value_tuple in self.buckets[key_bucket].items():
            if key_value_tuple[0] is key:
                return key_value_tuple[1]

        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket
        # key bucket index
        key_bucket = self._bucket_index(key)  # O(1) time
        bucket = self.buckets[key_bucket]  # O(1) time
        in_hash_table = False

        # for key_value_tuple in bucket.items():
        #     old_key, old_value = key_value_tuple
        items = bucket.items()  # O(l) for l items in bucket (LL)
        for old_key, old_value in items:  # O(l) iterations in worst case, O(1) beast case
            if old_key is key:
                in_hash_table = True
                bucket.delete((key, old_value))  # O(l)
                bucket.append((key, value))  # O(1)

        # O(l) in worst case because we iterate over all nodes if near tail or not found
        key_value_pair = bucket.find(lambda key_value: key_value[0] == key)
        if key_value_pair is not None:
            bucket.delete(key_value_pair)  # O(l) time in worst case
            bucket.append((key, value))  # O(1) time if using tail

        # if not in_hash_table:
        else:
            bucket.append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        key_bucket = self._bucket_index(key)
        in_hash_table = False

        print(self.buckets[key_bucket].items())

        for key_value_tuple in self.buckets[key_bucket].items():
            if key_value_tuple[0] is key:
                in_hash_table = True
                self.buckets[key_bucket].delete((key, key_value_tuple[1]))

        if not in_hash_table:
            raise KeyError('Key not found: {}'.format(key))

def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
