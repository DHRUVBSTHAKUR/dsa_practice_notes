# 🧠 First Missing Positive — Revision Sheet

---

## 🔹 Problem

Given an unsorted array `nums`, return the **smallest missing positive integer**.

### Constraints:

* Time: **O(n)**
* Space: **O(1)**

---

# 🔥 Pattern to Use: Cyclic Sort

---

## 🧠 When to Detect This Pattern

Use **Cyclic Sort** when you see:

* “Missing number”
* “Unsorted array”
* “O(1) space required”
* Values are in range like **1 → n**

👉 Instantly think:

```text
Place each number at its correct index
```

---

# 🧠 Core Idea

```text
value → correct index
1 → index 0
2 → index 1
3 → index 2
```

👉 Formula:

```python
correct_index = nums[i] - 1
```

---

# 🧠 Your Mnemonic (🔥 GOLD)

```text
1. Home Address → Calculate where the value should go
2. Swap → If not home, send it there
3. Advance → Move only if current is correct
```

---

# 🔁 Step 1: Cyclic Sort (Main Logic)

```python
i = 0
while i < n:
    correct_idx = nums[i] - 1

    if 1 <= nums[i] <= n and nums[i] != nums[correct_idx]:
        nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
    else:
        i += 1
```

---

## 🔍 Explanation Using Mnemonic

### 🏠 Home Address

```python
correct_idx = nums[i] - 1
```

---

### 🔄 Swap

```python
if nums[i] != nums[correct_idx]:
    swap
```

---

### ➡️ Advance

```python
else:
    i += 1
```

👉 Only move when current index is correct

---

# 🔍 Step 2: Find Missing Number

```python
for i in range(n):
    if nums[i] != i + 1:
        return i + 1
```

---

# 🔥 Edge Case

If all positions are correct:

```python
return n + 1
```

---

# 🔹 Full Code

```python
def firstMissingPositive(nums):
    n = len(nums)
    i = 0

    while i < n:
        correct_idx = nums[i] - 1

        if 1 <= nums[i] <= n and nums[i] != nums[correct_idx]:
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1
```

---

# 🔹 Dry Run Example

```python
nums = [3, 4, -1, 1]
```

After cyclic sort:

```text
[1, -1, 3, 4]
```

Scan:

```text
index 1 → expected 2 → missing → answer = 2
```

---

# 🔹 Important Rules

* Ignore:

  * negatives ❌
  * zero ❌
  * numbers > n ❌

* Only care about:

```text
1 to n
```

---

# 🔹 Common Mistakes

❌ Forgetting `nums[i] != nums[correct_idx]` → infinite loop
❌ Using wrong index formula
❌ Incrementing `i` after swap

---

# 🔥 Final Intuition

```text
Put every number in its correct place,
then find the first place where it's wrong.
```

---

# 🧠 One-Line Memory Hook

```text
"Send numbers home → first empty home is the answer"
```

---

# 🚀 Complexity

* Time: **O(n)**
* Space: **O(1)**

---
