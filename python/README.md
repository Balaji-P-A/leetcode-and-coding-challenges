# 🧠 LeetCode Problems & Solutions (Python)

Welcome to my **LeetCode Practice Repository**!  
This project contains Python solutions to various **LeetCode coding problems**, organized by topic and difficulty level.  
Each problem includes clean, optimized code with helpful explanations and comments.

---

## 📁 Folder Structure

leetcode/
│
├── arrays/
│ ├── two_sum.py
│ ├── best_time_to_buy_and_sell_stock.py
│ └── ...
│
├── strings/
│ ├── valid_anagram.py
│ ├── longest_common_prefix.py
│ └── ...
│
├── dynamic_programming/
│ ├── climbing_stairs.py
│ ├── house_robber.py
│ └── ...
│
└── README.md


---

## 🚀 Features

- 🧩 **Categorized by topic** — Arrays, Strings, Linked Lists, Trees, Dynamic Programming, etc.  
- 🧠 **Optimized Python solutions** — Clean, readable, and efficient code.  
- 💬 **Problem descriptions & approach notes** — Short explanations included as comments.  
- 🏗️ **Continuous updates** — Regularly adding new problems and revising older ones.

---

## 🧰 Technologies Used

- **Language:** Python 3  
- **IDE:** VS Code / PyCharm  
- **Version Control:** Git & GitHub  

---

## 🗂️ File Naming Convention

Each file follows this format:
problem_name.py


Example:


two_sum.py
longest_substring_without_repeating_characters.py


---

## 🧩 Example Solution

```python
# Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i

💡 How to Use

Clone this repository:

git clone https://github.com/yourusername/leetcode-python.git


Navigate into the folder:

cd leetcode-python


Run any solution:

python arrays/two_sum.py

🏆 Goal

To solve 500+ LeetCode problems while improving:

Algorithmic thinking

Data structure mastery

Code optimization skills

👤 Author

Balaji P
📧 [balajiprakash694@gmail.com
]
💼 [https://www.linkedin.com/in/balajiprasad-p/]

⭐ Acknowledgment

Thanks to LeetCode
 for providing challenging problems that help developers grow and refine their skills.


---

Would you like me to make this **shorter (for GitHub)** or **detailed (for a portfolio project)**  or **detailed (for a portfolio project)** version?
