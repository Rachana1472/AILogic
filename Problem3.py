import sys

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def add_two_numbers(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    carry = 0
    
    p1 = l1
    p2 = l2
    
    while p1 or p2 or carry:
        v1 = p1.val if p1 else 0
        v2 = p2.val if p2 else 0
        
        total = v1 + v2 + carry
        carry = total // 10
        digit = total % 10
        
        curr.next = ListNode(digit)
        curr = curr.next
        
        if p1:
            p1 = p1.next
        if p2:
            p2 = p2.next
            
    return dummy.next

def linked_list_to_list(head):
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    list1_vals = [int(x) for x in input_data[1:1+n]]
    
    m_idx = 1 + n
    m = int(input_data[m_idx])
    list2_vals = [int(x) for x in input_data[m_idx+1:m_idx+1+m]]
    
    l1 = build_linked_list(list1_vals)
    l2 = build_linked_list(list2_vals)
    
    res_head = add_two_numbers(l1, l2)
    res_vals = linked_list_to_list(res_head)
    
    print(*(res_vals))

if __name__ == "__main__":
    main()
