##@author DHRUV
#SLIDING_WINDOW first pattern learned 
def silding_window(s):
    left = 0 
    max_lenght = 0 
    window_content={}
    for right in range(len(s)):
        char=s[right]
        window_content=window_content.get(char,0)+1
        while window_content[char]>1:
            left_char=s[left]
            window_content[left_char]-=1
            if window_content[left_char]==0:
                del window_content[left_char]
            left+=1

        max_length=max(max_length,right-left+1)
    return max_length

#MEMORISING TRICK 
"""
🧠 The "OA Brain" (Line-by-Line Breakdown)
Imagine you are in the OA. The screen is blank. Here is the exact internal monologue you need to have to rebuild this from scratch:

1. "I need boundaries and a backpack."

Python
    left = 0
    max_len = 0
    window_counts = {} 
Thought Process: "I can't have a window without a start point (left). I need a variable to track my high score (max_len). I need a backpack to keep track of what's currently inside my window (window_counts)."

2. "Send out the scout."

Python
    for right in range(len(s)):
        char = s[right]
Thought Process: "The right pointer is my scout. He marches forward one step at a time, exploring the array. He never looks back. I'll grab whatever he is currently looking at (char)."

3. "Put it in the backpack."

Python
        window_counts[char] = window_counts.get(char, 0) + 1
Thought Process: "The scout found something. Toss it in the backpack. Update the frequency."

4. "Did we break the rules? If so, pack up base camp."

Python
        while window_counts[char] > 1:
Thought Process: "Wait, the problem says 'no duplicate characters'. Does my backpack have more than 1 of the item I just added? If yes, my window is invalid. I must use a while loop, not an if statement, because I might need to shrink the window multiple times to make it valid again."

5. "Kick things out until we are legal again."

Python
            left_char = s[left]
            window_counts[left_char] -= 1
            if window_counts[left_char] == 0:
                del window_counts[left_char]
            left += 1
Thought Process: "To fix the window, the left pointer (base camp) must move up. Before base camp moves, it drops whatever item it was standing on. If the count hits zero, I delete it completely so my backpack doesn't get cluttered."

6. "Record the high score."

Python
        max_len = max(max_len, right - left + 1)
Thought Process: "Okay, the while loop is done (or never ran). My window is officially valid. How big is it? Distance is right - left + 1 (the +1 is because arrays are 0-indexed). Is this bigger than my previous high score? Update it."
"""


