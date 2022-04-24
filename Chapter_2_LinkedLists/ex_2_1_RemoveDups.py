# Removes Dups : write code to remove duplicates from an unsorted linked list

from Chapter_2_LinkedLists.Node import Node, SortedList, SortedSet

def remove_duplicates_with_hashset(head: Node):
    node = head
    already_met = set()
    already_met.add(head.data)
    while node.next != None :
        if node.next.data in already_met:
            node.next = node.next.next
        else: # Only move forward if we didn't met a duplicate, because the next element might also be one
            already_met.add(node.next.data)
            node = node.next

def remove_duplicates(head: Node):
    node = head
    while node.next is not None:
        current_data = node.data
        scanner = node
        while scanner.next is not None:
            if scanner.next.data == current_data:
                scanner.next = scanner.next.next
            scanner = scanner.next
        node = node.next

def remove_duplicates_by_sorting(head: Node):
    node = head
    sorted_list = SortedSet(node.data)
    while node.next is not None:
        node = node.next
        sorted_list.insert(node.data)
    print(sorted_list)

linkedlist = Node(5, 1, 2, 3, 4, 2, 1, 4, 2, 3, 5)
print(linkedlist)
remove_duplicates_with_hashset(linkedlist)
print(str(linkedlist))
assert "5 -> 1 -> 2 -> 3 -> 4 -> None" == str(linkedlist)