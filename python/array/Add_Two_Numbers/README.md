## 🧮 Add Two Numbers (Linked List)

### 📘 Problem Description
You are given two **non-empty linked lists** representing two non-negative integers.  
The digits are stored in **reverse order**, and each node contains a **single digit**.  
Add the two numbers and return the **sum** as a linked list.

You may assume that both numbers **do not contain any leading zeros**, except for the number **0** itself.

---

### 🧩 Example

#### Example 1
**Input:**  
`l1 = [2,4,3]`, `l2 = [5,6,4]`  
**Output:**  
`[7,0,8]`  
**Explanation:**  
342 + 465 = 807

#### Example 2
**Input:**  
`l1 = [0]`, `l2 = [0]`  
**Output:**  
`[0]`

#### Example 3
**Input:**  
`l1 = [9,9,9,9,9,9,9]`, `l2 = [9,9,9,9]`  
**Output:**  
`[8,9,9,9,0,0,0,1]`

---

### ⚙️ Constraints
- The number of nodes in each linked list is in the range **[1, 100]**
- `0 <= Node.val <= 9`
- It is guaranteed that the list represents a number that does **not have leading zeros**

---

### 🧠 Approach
1. Traverse both linked lists simultaneously.  
2. At each step, add the values of the current nodes and any carry from the previous step.  
3. Compute:
   - `total = val1 + val2 + carry`
   - `carry = total // 10`
   - `new_node_value = total % 10`
4. Create a new linked list node for each computed digit.  
5. Continue until both lists are fully traversed **and** no carry remains.

---

### 💻 Code Implementation
```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            new_val = total % 10

            current.next = ListNode(new_val)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
```

---

### 🧪 Example Test Code
```python
# Helper functions to test locally
def list_to_linkedlist(lst):
    dummy = ListNode()
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linkedlist_to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

# Test
l1 = list_to_linkedlist([2,4,3])
l2 = list_to_linkedlist([5,6,4])
sol = Solution()
result = sol.addTwoNumbers(l1, l2)
print(linkedlist_to_list(result))  # Output: [7,0,8]
```

---

### 👨‍💻 Author
**Balaji P**  
*Python Developer | Problem Solver | LeetCode Enthusiast*
