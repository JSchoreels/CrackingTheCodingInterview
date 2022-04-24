# Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node.
# EXAMPLE
# input:the node c from the linked lista->b->c->d->e->f
# Result: nothing is returned, but the new linked list looks like a->b->d->e->f
from Chapter_2_LinkedLists.Node import Node

def delete_middle_node(node_to_remove: Node):
    node_to_remove.data = node_to_remove.next.data
    node_to_remove.next = node_to_remove.next.next


linkedlist = Node(1, 2, 3, 4, 5, 6, 7, 8)
print(linkedlist)
delete_middle_node(linkedlist.next.next.next.next) # Remove 5
print(linkedlist)
assert str(linkedlist) == "1 -> 2 -> 3 -> 4 -> 6 -> 7 -> 8 -> None"