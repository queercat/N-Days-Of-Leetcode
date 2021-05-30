# Given two sorted linked lists, merge them.

# Naive solution, just turn both linked lists into an array, sort that array and then return a linked list.

def merge_two_lists(la, lb):
	to_sort = []

	if not la:
		return lb

	if not lb:
		return la

	while la:
		to_sort.append(la.val)

		la = la.next

	while lb:
		to_sort.append(lb.val)

		lb = lb.next

	to_sort.sort()

	head = ListNode(to_sort[0])
	curr = head
	for elem in to_sort[1:]:
		curr.next = ListNode(elem)
		curr = curr.next

	return head