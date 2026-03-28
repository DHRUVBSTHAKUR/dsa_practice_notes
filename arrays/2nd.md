# 🧠 Product of Array Except Self — Revision Sheet

---

## 🔹 Problem

Given an array `nums`, return an array `answer` such that:

```text
answer[i] = product of all elements except nums[i]
```

### Constraints:

* Must run in **O(n)** time
* **No division allowed**

---

## 🔹 Key Insight (🔥 MOST IMPORTANT)

```text
answer[i] = (product of LEFT) × (product of RIGHT)
```

👉 Split the problem into:

* Left side (prefix)
* Right side (suffix)

---

# 🔸 Approach 1: Prefix + Suffix Arrays (Beginner Friendly)

---

## Step 1: Build Left Products

```python
left_products[0] = 1
for i in range(1, n):
    left_products[i] = left_products[i-1] * nums[i-1]
```

👉 Meaning:

* Store product of everything **before i**

---

## Step 2: Build Right Products

```python
right_products[n-1] = 1
for i in range(n-2, -1, -1):
    right_products[i] = right_products[i+1] * nums[i+1]
```

👉 Meaning:

* Store product of everything **after i**

---

## Step 3: Build Answer

```python
answer = [0] * n

for i in range(n):
    answer[i] = left_products[i] * right_products[i]
```

---

## Full Code

```python
def productExceptSelf(nums):
    n = len(nums)

    left_products = [1] * n
    right_products = [1] * n
    answer = [0] * n

    # left
    for i in range(1, n):
        left_products[i] = left_products[i-1] * nums[i-1]

    # right
    for i in range(n-2, -1, -1):
        right_products[i] = right_products[i+1] * nums[i+1]

    # answer
    for i in range(n):
        answer[i] = left_products[i] * right_products[i]

    return answer
```

---

## Complexity

* Time: **O(n)**
* Space: **O(n)** ❌

---

# 🔸 Approach 2: Optimized (Interview Optimal)

---

## Idea

* Use `res` as left array
* Use a variable `right` instead of extra array

---

## Code

```python
def productExceptSelf(nums):
    n = len(nums)
    res = [1] * n

    # left pass
    left = 1
    for i in range(n):
        res[i] = left
        left *= nums[i]

    # right pass
    right = 1
    for i in range(n-1, -1, -1):
        res[i] *= right
        right *= nums[i]

    return res
```

---

## Complexity

* Time: **O(n)**
* Space: **O(1)** ✅

---

# 🔹 Dry Run Example

```python
nums = [1, 2, 3, 4]
```

### Left:

```text
[1, 1, 2, 6]
```

### Right:

```text
[24, 12, 4, 1]
```

### Answer:

```text
[24, 12, 8, 6]
```

---

# 🔹 Patterns to Remember

### Prefix Pattern

```python
prefix[i] = prefix[i-1] * nums[i-1]
```

### Suffix Pattern

```python
suffix[i] = suffix[i+1] * nums[i+1]
```

---

# 🔹 Key Rules (🔥 IMPORTANT)

* Always **exclude current element**
* Use:

  * `i-1` for left
  * `i+1` for right

---

# 🔹 Common Mistakes

❌ Using `nums[i]` instead of `nums[i-1]` / `nums[i+1`
❌ Wrong loop direction
❌ Updating before storing
❌ Forgetting base case (`1`)

---

# 🔹 Intuition (MEMORY TRICK)

> “Split array into left and right — multiply both”

---

# 🔹 When to Use This Pattern

Look for:

* “Except self”
* “Product/Sum of others”
* “No division allowed”

👉 Think: **Prefix + Suffix**

---

# 🔹 Final Takeaway

```text
Forward → store LEFT
Backward → multiply RIGHT
```

👉 That’s the entire problem.

---
