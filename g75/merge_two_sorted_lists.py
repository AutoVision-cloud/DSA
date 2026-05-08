from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Time complexity: O(N+M), Space complexity: O(1)
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        current.next = list1 if list1 else list2

        return dummy.next


def to_list(node: Optional[ListNode]):
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

    assert to_list(s.mergeTwoLists(to_linked_list([1, 2, 4]), to_linked_list([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert to_list(s.mergeTwoLists(to_linked_list([]), to_linked_list([]))) == []
    assert to_list(s.mergeTwoLists(to_linked_list([]), to_linked_list([0]))) == [0]
    assert to_list(s.mergeTwoLists(to_linked_list([5]), to_linked_list([1, 2, 3]))) == [1, 2, 3, 5]

    print("All tests passed.")
