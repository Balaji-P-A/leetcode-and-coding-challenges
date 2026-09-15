# 1. Two Sum

## Problem Statement

You are given an array of integers `nums` and an integer `target`.

Return the **indices of the two numbers** such that they add up to `target`.

You may assume that:

* Each input has **exactly one solution**.
* You may **not use the same element twice**.
* You can return the answer in **any order**.

---

## Examples

### Example 1

**Input:**

```text
nums = [2,7,11,15]
target = 9
```

**Output:**

```text
[0,1]
```

**Explanation:**

Because:

```text
nums[0] + nums[1] = 2 + 7 = 9
```

we return `[0, 1]`.

---

### Example 2

**Input:**

```text
nums = [3,2,4]
target = 6
```

**Output:**

```text
[1,2]
```

**Explanation:**

Because:

```text
nums[1] + nums[2] = 2 + 4 = 6
```

we return `[1, 2]`.

---

### Example 3

**Input:**

```text
nums = [3,3]
target = 6
```

**Output:**

```text
[0,1]
```

**Explanation:**

Because:

```text
nums[0] + nums[1] = 3 + 3 = 6
```

we return `[0, 1]`.

---

## Constraints

```text
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
```

* Only **one valid answer** exists.

---

## Follow-Up

Can you come up with an algorithm that is **less than `O(n²)` time complexity**?
