class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

headA = ListNode(4)
headA.next= ListNode(1)
headA.next.next= ListNode(8)
headA.next.next.next= ListNode(4)
headA.next.next.next.next= ListNode(5)

headB = ListNode(5)
headB.next = ListNode(0)
headB.next.next = ListNode(1)
headB.next.next.next = ListNode(8)
headB.next.next.next.next = ListNode(4)
headB.next.next.next.next.next = ListNode(5)

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
        pa = headA
        pb = headB
        
        while pa:
            print(pa.val)
            while pb:
            	# print(pb.val)
            	if pa == pb:
            		return pa
            	pb = pb.next
            pb = headB
            pa = pa.next
        
        return None

print(getIntersectionNode(headA, headB))