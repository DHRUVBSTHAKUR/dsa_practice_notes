# 🧠 Majority Element — Revision Sheet

---

## 🔹 Problem

Find the element that appears **more than ⌊n/2⌋ times** in an array.

---

## 🔹 Key Insight

* Majority element appears **more than all other elements combined**
* There can be **only one majority element**

---

# 🔸 Approach 1: HashMap (Counting)

## Idea

Count frequency of each element and return the one exceeding `n//2`.

## Code

```python
def majority_hashmap(nums):
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > len(nums) // 2:
            return num
```

## Key Line (IMPORTANT)

```python
counts[num] = counts.get(num, 0) + 1
```

👉 Meaning:

* Get current count (or 0 if not present)
* Add 1
* Store back

## Time & Space

* Time: O(n)
* Space: O(n)

## When to Use

* Frequency counting problems
* Top K elements
* Duplicate detection

---

# 🔸 Approach 2: Boyer-Moore Voting Algorithm

## Core Idea (🔥 MUST REMEMBER)

> “Cancel out different elements — majority survives”

---

## Intuition

* Same element → **increase count**
* Different element → **cancel (decrease count)**
* When count = 0 → pick new candidate

---

## Code

```python
def majorityElement(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        
        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate
```

---

## Optional Verification (if majority NOT guaranteed)

```python
if nums.count(candidate) > len(nums) // 2:
    return candidate
```

---

## Key Concepts

* **Pair cancellation**
* Majority can’t be fully eliminated
* Works in one pass

---

## Time & Space

* Time: O(n)
* Space: O(1) ✅

---

# 🔹 Dry Run Example

Input:

```python
[2, 2, 1, 1, 1, 2, 2]
```

Flow:

* Candidate resets when count = 0
* Final candidate = **2**

---

# 🔹 Patterns to Remember

### HashMap Pattern

```python
counts[x] = counts.get(x, 0) + 1
```

👉 “Increase frequency”

---

### Voting Pattern

```python
if count == 0:
    candidate = num

if num == candidate:
    count += 1
else:
    count -= 1
```

👉 “Same → increase, different → cancel”

---

# 🔹 Mental Models

🧠 HashMap:

> “Vote counting system”

🧠 Boyer-Moore:

> “Battle: friends vs enemies → majority survives”

---

# 🔹 Common Mistakes

* Forgetting `count == 0` reset
* Mixing up increment/decrement
* Not verifying when majority not guaranteed

---

👉 Output: `3`

---

# 🔹 Final Takeaway

* Use **HashMap** → when learning or need counts
* Use **Boyer-Moore** → optimal interview solution

---

✅ Golden Line to Remember:

> “If elements cancel each other, majority will still remain.”
