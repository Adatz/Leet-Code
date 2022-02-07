# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        setNums = set(nums)
        res = 0
        while head:
            if head.val in setNums and (head.next == None or head.next.val not in setNums):
                res += 1
            head = head.next
        return res
        