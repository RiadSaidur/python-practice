from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
  if not head or not head.next:
    return head

  odd = head
  even = head.next
  evenHead = even

  while (odd and odd.next) and (even and even.next):
    odd.next = odd.next.next
    odd = odd.next

    even.next = even.next.next
    even = even.next

  odd.next = evenHead
  
  return head
