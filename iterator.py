def list_comprehension(arr):
    new_arr = [number + 1 for number in arr]
    return new_arr

def change_to_tuple(arr):
    tup = tuple(arr)
    return tup

class LinkedList:

    def __init__(self, collection=None):
        self.head = None

        if collection:
            for item in reversed(collection):
                self.insert(item)

    def __iter__(self):

        def value_generator():

            current = self.head
            while current:
                yield current.value
                current = current.next
        return value_generator()

    def __str__(self):
        out = ''

        for value in self:
            out += f'{ {value} } -> '
        out += 'None'
        return out

    def insert(self, value):
        self.head = Node(value, self.head)
    
    def __eq__(self, other):
        return list(self) == list(other)

class Node:
    def __init__(self, value, next_ = None):
        self.value = value
        self.next = next_




if __name__ == "__main__":
    print(list_comprehension([1,2,3]))
    print(change_to_tuple(list_comprehension([1,2,3])))

    ll = LinkedList()
    ll.insert(3)
    ll.insert(2)
    ll.insert(1)

    ll2 = LinkedList()
    ll2.insert(3)
    ll2.insert(2)
    ll2.insert(1)
    print(ll == ll2)
    print(ll)