# 🧮 Add Two Numbers (Linked List)

## 📘 Problem Statement

You are given two non-empty linked lists representing two non-negative integers.  
The digits are stored in **reverse order**, and each of their nodes contains a single digit.  
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

---

## 🧾 Example 1
**Input:**  
```
l1 = [2,4,3]
l2 = [5,6,4]
```

**Output:**  
```
[7,0,8]
```

**Explanation:**  
342 + 465 = 807

---

## 🧾 Example 2
**Input:**  
```
l1 = [0]
l2 = [0]
```
**Output:**  
```
[0]
```

---

## 🧾 Example 3
**Input:**  
```
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
```
**Output:**  
```
[8,9,9,9,0,0,0,1]
```

---

## 🧠 Constraints
- The number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros.

---

## 💡 Approach

1. Use a **dummy head node** to simplify result list creation.  
2. Traverse both lists simultaneously, adding corresponding digits along with a **carry** value.  
3. If one list is shorter, treat missing values as `0`.  
4. Create a new node for each sum’s unit digit (`sum % 10`).  
5. Update the carry for next iteration (`carry = sum // 10`).  
6. If a carry remains after traversal, add an extra node.  

---

## 🧠 Complexity Analysis

| Type | Complexity | Description |
|------|-------------|--------------|
| ⏱️ Time | **O(max(m, n))** | Each list is traversed once |
| 💾 Space | **O(max(m, n))** | Result list grows with the largest input |

---

## ✅ Full Solution Code

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: 'Optional[ListNode]', l2: 'Optional[ListNode]') -> 'Optional[ListNode]':
        # Dummy node to simplify result list creation
        dummy = ListNode(0)
        current = dummy
        carry = 0

        # Traverse both linked lists
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry

            # Calculate new digit and carry
            carry = total // 10
            new_val = total % 10

            # Append to result list
            current.next = ListNode(new_val)
            current = current.next

            # Move to next nodes
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
```

---

## 🧪 Example Test Runner (for Local Testing)

```python
# Helper functions for local testing
def build_linked_list(nums):
    dummy = ListNode(0)
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Example usage
if __name__ == "__main__":
    l1 = build_linked_list([2,4,3])
    l2 = build_linked_list([5,6,4])
    result = Solution().addTwoNumbers(l1, l2)
    print(linked_list_to_list(result))  # Output: [7, 0, 8]
```

---

## 🧑‍💻 Author
**Vishal Kumar R**  
Python Developer | Problem Solver | Algorithm Enthusiast
