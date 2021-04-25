import pytest
from iterator import list_comprehension, change_to_tuple, LinkedList, Node

def test_list_comprehension():
    actual = list_comprehension([1,2,3])
    expected = [2,3,4]
    assert actual == expected

def test_change_to_tuple():
    arr = list_comprehension([1,2,3])
    actual = change_to_tuple(arr)
    expected = (2,3,4)
    assert actual == expected

def test_dunder_iter():
    ll = LinkedList()
    ll.insert(3)
    ll.insert(2)
    ll.insert(1)
    
    actual = str(ll)
    expected = '{1} -> {2} -> {3} -> None'
    
def test_dunder_eq():
    ll = LinkedList()
    ll.insert(3)
    ll.insert(2)
    ll.insert(1)

    ll2 = LinkedList()
    ll2.insert(3)
    ll2.insert(2)
    ll2.insert(1)
    
    actual = ll == ll2
    expected = True
    assert actual == expected
