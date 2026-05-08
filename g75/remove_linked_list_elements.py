from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Time complexity: O(N), space complexity: O(1)
        dummy = ListNode(0)
        current = dummy

        while head:
            if head.val == val:
                head = head.next
            else:
                current.next = head
                head = head.next
                current = current.next

        current.next = None

        return dummy.next


def to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def to_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


if __name__ == "__main__":
    s = Solution()

    assert to_list(s.removeElements(to_linked_list([1, 2, 6, 3, 4, 5, 6]), 6)) == [1, 2, 3, 4, 5]
    assert to_list(s.removeElements(to_linked_list([]), 1)) == []
    assert to_list(s.removeElements(to_linked_list([7, 7, 7, 7]), 7)) == []
    assert to_list(s.removeElements(to_linked_list([1, 2, 3]), 4)) == [1, 2, 3]

    print("All tests passed.")
