# 🧠 Two Pointers — Complete Revision Sheet

---

# 🔥 Pattern Recognition (MOST IMPORTANT)

Use Two Pointers when:

* You are comparing **two elements / sequences**
* Order matters OR array is sorted
* Need **O(n)** instead of O(n²)

👉 Think:

```text
Two pointers → reduce search space efficiently
```

---

# 🔸 Variant 1: Single Array (Sorted) — Opposite Ends

---

## 🔹 When to Use

* Sorted array ✅
* Find pair (sum / condition)

---

## 🧠 Core Idea

```text
Start from both ends → shrink window
```

---

## 🔁 Movement Logic

```text
If sum < target → move left++
If sum > target → move right--
```

---

## Template

```python
left, right = 0, len(arr) - 1

while left < right:
    if condition:
        return result
    elif need bigger:
        left += 1
    else:
        right -= 1
```

---

## 🧠 Memory

```text
Small + Big → adjust window
```

---

# 🔸 Variant 2: Two Arrays / Strings — Same Direction

---

## 🔹 When to Use (VERY IMPORTANT)

* Comparing two strings/arrays
* Checking **subsequence / matching / merging**
* Order matters ✅

👉 Example:

* Is Subsequence
* Merge problems

---

## 🧠 Core Idea

```text
One pointer scans (fast)
One pointer matches (slow)
```

---

## 🔁 Movement Logic

```text
If match → move both
If no match → move only second pointer
```

---

## Template

```python
i, j = 0, 0

while i < len(arr1) and j < len(arr2):
    if arr1[i] == arr2[j]:
        i += 1   # matched
    j += 1       # always move

return i == len(arr1)
```

---

## 🔍 Why This Works

* `j` explores everything
* `i` only moves when match happens

👉 Ensures **order is preserved**

---

## 🧠 Intuition (BEST MEMORY MODEL)

```text
arr1 → what you need
arr2 → where you search
```

---

## 🧠 Your Analogy

```text
Shopping list (arr1)
Supermarket (arr2)

Scan store → pick items in order
```

---

# 🔴 Common Mistakes

❌ Moving both pointers always
❌ Forgetting final condition `i == len(arr1)`
❌ Using wrong variant for problem

---

# 🔥 Choosing the Right Variant

| Situation                | Use            |
| ------------------------ | -------------- |
| Sorted array + pair      | Opposite ends  |
| Two arrays / subsequence | Same direction |

---

# 🧠 Final Memory Hooks

### Variant 1:

```text
Shrink window from both ends
```

### Variant 2:

```text
Scan big, match small
```

---

# 🔥 One-Line Takeaway

```text
Two Pointers = controlled movement to avoid brute force
```

---
