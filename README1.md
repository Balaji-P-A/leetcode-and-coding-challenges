# Array Concepts in Python

**Author:** Balaji P  

---

## 🧠 Overview

In Python, arrays are fundamental data structures used to store multiple values in a single variable.  
There are two common ways to represent arrays:

1. **Built-in Lists** — flexible, dynamic, and can hold mixed data types.  
2. **NumPy Arrays** — efficient, fixed-type, and optimized for numerical computation.

---

## 📘 Built-in Python Lists

Python’s built-in list can act like a dynamic array.  
You can store integers, floats, strings, or even mixed data types.

### Example 1: Creating and Accessing Lists

```python
# Creating a list
arr = [10, 20, 30, 40, 50]

# Accessing elements
print(arr[0])  # Output: 10
print(arr[-1]) # Output: 50
```

### Example 2: Modifying and Slicing

```python
arr[2] = 100
print(arr)  # Output: [10, 20, 100, 40, 50]

# Slicing
print(arr[1:4])  # Output: [20, 100, 40]
```

---

## ⚙️ NumPy Arrays

NumPy is a powerful library for numerical and matrix operations.  
Unlike Python lists, NumPy arrays are **homogeneous** (all elements have the same data type).

### Example 1: Creating NumPy Arrays

```python
import numpy as np

# Creating a 1D array
np_arr = np.array([1, 2, 3, 4, 5])
print(np_arr)
# Output: [1 2 3 4 5]

# Creating a 2D array
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)
# Output:
# [[1 2 3]
#  [4 5 6]]
```

### Example 2: Array Operations

```python
import numpy as np

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a + b)  # Output: [11 22 33]
print(a * b)  # Output: [10 40 90]
print(a.mean())  # Output: 20.0
print(a.reshape(3, 1))
# Output:
# [[10]
#  [20]
#  [30]]
```

---

## 📊 Summary Table

| Feature | Python List | NumPy Array |
|----------|--------------|--------------|
| Type Flexibility | Can store mixed types | Only one data type |
| Speed | Slower | Faster (C-optimized) |
| Memory Efficiency | Less efficient | More efficient |
| Mathematical Operations | Manual loops | Vectorized (fast) |
| Multi-dimensional Support | Nested lists | Native support |

---

## ✅ Key Takeaways

- Use **lists** for general-purpose storage.  
- Use **NumPy arrays** for numerical or matrix-based operations.  
- NumPy arrays are optimized for performance and data consistency.

---

*Created by Balaji P*
