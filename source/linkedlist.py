#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: O(n) for the best and worst case because all n nodes must
        be counted to find the length of the linked list."""
        # Loop through all nodes and count one for each
        count = 0
        current_node = self.head

        if not self.is_empty():
            # comments shoud say why
            while current_node is not None:
                count += 1
                current_node = current_node.next

        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1) for the best and worst case because the tail node is
        saved and can quickly be appended to."""
        # Create new node to hold given item
        # Append node after tail, if it exists
        # if self.is_empty():
        #     self.head = Node(item)
        #     self.tail = self.head
        # elif self.tail == self.head:
        #     self.tail = Node(item)
        #     self.head.next = self.tail
        # else:
        #     self.tail.next = Node(item)
        #     self.tail = Node(item)

        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        # In either case, the tail will be the new node
        self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1) because the head node is saved and can quickly be
        prepended to."""
        # Create new node to hold given item
        # Prepend node before head, if it exists
        if self.is_empty():
            self.head = Node(item)
            self.tail = self.head
        elif self.tail == self.head:
            self.head = Node(item)
            self.head.next = self.tail
        else:
            old_first = self.head
            self.head = Node(item)
            self.head.next = old_first

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: O(1) because if the first node's data satisfies
        the given quality, it will return the item and end the loop of nodes.
        Worst case running time: O(n) because in the worst case, the item that
        satisfies the quality will be in the last node, so all nodes would have
        to be looped through. In addition, if none of the items satisfy the
        requirement, all nodes will be looped through before None will be
        returned."""
        # Loop through all nodes to find item where quality(item) is True
        # Check if node's data satisfies given quality function
        item = None
        current_node = self.head

        if not self.is_empty():
            while current_node:
                if quality(current_node.data):
                    return current_node.data
                current_node = current_node.next

        return item

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(n) because I iterate through all of the nodes
        to delete any item that matches the given item. I understand that if I
        were to delete only one item that matched the given item, the best case
        would be O(1) if the first item found matched and was returned.
        Worst case running time: O(n) for the same reasons of my best case. If
        no item is mateched, all the nodes will be run through and an error
        will be raised."""
        # Loop through all nodes to find one whose data matches given item
        # Update previous node to skip around node with matching data
        # Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        current_node = self.head
        deleted = False

        # while current_node is not None and current_node.data is item:
        #     if self.head.next is None:
        #         self.tail = None
        #     self.head = current_node.next
        #     current_node = self.head
        #     deleted = True
        #
        # while current_node is not None and current_node.next is not None:
        #     if current_node.next.data is item and current_node.next.next is None:
        #         current_node.next = None
        #         self.tail = current_node.next
        #         deleted = True
        #     else:
        #         if current_node.next.data is item:
        #             current_node.next = current_node.next.next
        #             deleted = True
        #     if self.head.next is None:
        #         self.tail = self.head
        #
        #     current_node = current_node.next

        # NOTE: == is not the same as 'is'
        previous = None
        while current_node is not None:
            if current_node.data == item and current_node is self.head and current_node is self.tail:
                self.head = None
                self.tail = None
                deleted = True
            elif current_node.data == item and current_node is self.head:
                self.head = current_node.next
                if self.head == self.tail:
                    self.tail = current_node.next
                deleted = True
            elif current_node.data == item and current_node is self.tail:
                self.tail = previous
                self.tail.next = None
                if self.head == self.tail:
                    self.head = previous
                deleted = True
            elif current_node.data == item:
                previous.next = current_node.next
                deleted = True
            previous = current_node
            current_node = current_node.next

        if not deleted:
            raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
