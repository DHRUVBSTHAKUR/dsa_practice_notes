# 📄 ⚔️ Problem 6: Counting Bits (FINAL REVISION SHEET)

## 🧩 Problem Statement
Given an integer `n`, return an array `dp` of size `n + 1` such that:
`dp[i]` = number of 1's in the binary representation of `i`.

### 🔍 Example
* **Input:** `n = 5`
* **Output:** `[0, 1, 1, 2, 1, 2]`

---

## 🧠 1. Pattern Recognition

### 🚨 Smell Test
* Build answers from $0 \to n$
* Repeated subproblems
* Optimization required from brute force
* Bit-related computation

### 🧠 Pattern
* **1D Dynamic Programming + Bit Manipulation**

---

## 🧠 2. Brute Force Approach
### 💡 Idea
Count bits for each number independently using the bit-flip trick:
```python
while x:
    x = x & (x - 1)
```
## ⏱ Complexity:
 Time: O(NlogN) | Space: O(1)

## ❌ Problem: Repeated computation; not optimal for large n.

## 🧠 3. Recursive Insight 
(Core DP Thinking)
💡 Key Observation
A number i is related to i // 2 (which is i >> 1).

## 🔥 Relation
**bits(i)=bits(i≫1)+(i&1)**
## 🧠 Meaning
i >> 1: Removes the last bit.

(i & 1): Extracts the last bit (0 or 1).

## 💻 Recursive Form
Python
def f(i):
    if i == 0: return 0
    return f(i >> 1) + (i & 1)
## ❌ Problem: Overlapping subproblems → repeated calls.

## 🧠 4. Memoization (Top-Down DP)
💡 Idea
Store results to avoid recomputation.

## 💻 Code
Python
```
def countBits(n):
    memo = {}

    def f(i):
        if i == 0: return 0
        if i in memo: return memo[i]
        
        memo[i] = f(i >> 1) + (i & 1)
        return memo[i]

    return [f(i) for i in range(n + 1)]
```
## ⏱ Complexity:
**Time: O(N) | Space: O(N)**

## 🧠 5. Tabulation (Bottom-Up DP) ✅
💡 Idea
Build answers iteratively from 0→n.

## 💻 Code (FINAL)
Python
``` 
def countBits(n):
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)

    return dp
```
## ⏱ Complexity: 
**Time: O(N) | Space: O(N)**

## 🧠 6. Dry Run
***Input: n = 5***
```
i	Binary	dp[i >> 1] + (i & 1)	Result
0	000	-	0
1	001	dp[0] + 1	1
2	010	dp[1] + 0	1
3	011	dp[1] + 1	2
4	100	dp[2] + 0	1
5	101	dp[2] + 1	2
Output: [0, 1, 1, 2, 1, 2]
```
## 🧠 7. Key Bit Tricks
* 🔸 Remove rightmost 1: x = x & (x - 1)

* 🔸 Right shift (Divide by 2): i >> 1

* 🔸 Check odd/even: i & 1 (1 if odd, 0 if even)

## ⚠️ 8. Common Mistakes
* ❌ Using string conversion: bin(i).count('1') (Not optimal).

* ❌ Ignoring DP relation: Recalculating from scratch.

* ❌ Not understanding subproblem: Forgetting that i depends on i // 2.

## 🧠 9. Mental Model
❌ Wrong: Solve each number independently.

✅ Correct: Reuse the result of a smaller number (i >> 1).

## 🔥 10. Memory Trick
Shift → Reuse → Add last bit
OR
dp[i] = half + last_bit

## ⚔️ 11. Pattern Summary
* When you see:

* Binary representation

* Counting bits

* Range computation (0→n)

* O(N) constraint

👉 Think: DP + Bit Manipulation

## 🧠 12. Final Insight
DP = Break problem → reuse smaller results → build up.