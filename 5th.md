# 📄 ⚔️ Problem 5: Reverse Words in a String

## 🧩 Problem Statement
Given a string `s`, reverse the order of words.

### ✅ Rules:
* Words are separated by spaces
* Remove extra spaces
* Return clean string with single space between words

### 🔍 Example:
* **Input:** `"  hello   world  "`
* **Output:** `"world hello"`

---

## 🧠 1. Pattern Recognition

### 🚨 Smell Test
* String manipulation
* Words / spaces involved
* Clean formatting required

### 🧠 Pattern:
* Strings + Two Pointers / Built-in Tricks

---

## 🧠 2. Intuition (Core Thinking)

### ❌ Beginner Thinking
* Reverse whole string → **wrong**

### ✅ Correct Thinking
1.  Extract words
2.  Reverse order of words
3.  Join properly

> **💡 Key Idea:** Words stay same, order changes.

---

## 🧠 3. Approaches

### ⚡ Approach 1: Python Built-in (BEST for interviews)

#### 💻 Code
```python
def reverseWords(s):
    return " ".join(s.split()[::-1])
```
## 🔥 Breakdown 
### s.split(): 
Removes extra spaces automatically.Example: "  hello   world  ".split() → ["hello", "world"][::-1]: Reverses the list." ".join(...): Joins words with a single space.
### ⏱ Complexity 
Time: $O(N)$
Space: $O(N)$

### ⚡ Approach 2: Manual (Interview Deep Understanding)

#### 💻 Code
```python
def reverseWords(s):
    words = []
    word = ""

    for ch in s:
        if ch != " ":
            word += ch
        else:
            if word:
                words.append(word)
                word = ""

    if word:
        words.append(word)

    words.reverse()
    return " ".join(words)
```
### 🧠 What’s happening?
* **Step 1:** Extract words (Ignore multiple spaces).
* **Step 2:** Store words → `["hello", "world"]`.
* **Step 3:** Reverse → `["world", "hello"]`.
* **Step 4:** Join → `"world hello"`.

---

### ⚡ Approach 3: In-place (Advanced 🔥)
#### 💡 Idea
1.  **Reverse entire string.**
2.  **Reverse each word.**

**Example:**
`"hello world"` → `"dlrow olleh"` → `"world hello"`

> 👉 **Note:** Used when space is restricted ($O(1)$ space complexity in languages with mutable strings).

---

## 🧠 4. Edge Cases 🚨
* ❗ **Multiple spaces:** `"  a   b  "` → `"b a"`
* ❗ **Single word:** `"hello"` → `"hello"`
* ❗ **Empty string:** `""` → `""`

---

## 🔥 5. Common Mistakes
* ❌ **Not removing extra spaces**
* ❌ **Using `split(" ")`**: `s.split(" ")` keeps empty strings.
    * ✅ **Use:** `s.split()`
* ❌ **Reversing characters instead of words**

---

## 🧠 6. Mental Model
* ❌ **Wrong:** Reverse entire string blindly.
* ✅ **Correct:** Words = units. Reverse units, not characters.

---

## 🔥 7. Memory Trick
> **Split → Reverse → Join**
> *OR*
> **Clean → Reverse → Rebuild**

---

## ⚔️ 8. Pattern Summary
**When you see:**
* Words in string
* Extra spaces
* Reordering words

👉 **Think:** `Split` + `Reverse` + `Join`

---

## 🚀 9. Final Code (Best Version)
```python
def reverseWords(s):
    return " ".join(s.split()[::-1])
```

## 🧠 Final Insight
This problem teaches: Use built-ins smartly to simplify logic.