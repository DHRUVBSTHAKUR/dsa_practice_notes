##@AUTHOR DHRUV 
#Two pointers coding pattern 

def two_pointers(s,target):
    left = 0 
    right = len(s)-1
    while left < right :
        curr_sum = s[left]+s[right]
        if curr_sum ==target :
            return [ left , right ]
        elif curr_sum< target:
            left +=1 
        else :
            right -=1
             
    return []

#MEMORISING TRICK 
"""

🧠 The "OA Brain" (Line-by-Line Breakdown)
You are staring at a completely blank screen. The countdown timer is ticking. Your brain goes completely numb. Here is the exact internal dialogue to kick-start your hands into typing this out step-by-step:

1. "Establish the perimeter."

Python
    left = 0
    right = len(nums) - 1
Thought Process: "I need to look at pairs across the whole spectrum. I'll place one lookout at the absolute beginning (left = 0) and another lookout at the absolute end (right = len(nums) - 1). They will walk toward each other."

2. "Do not cross the streams."

Python
    while left < right:
Thought Process: "The search continues as long as my lookouts haven't crossed paths. I use a strict < instead of <= because a single element cannot form a distinct pair with itself."

3. "Take the current measurement."

Python
        current_sum = nums[left] + nums[right]
Thought Process: "Combine the strengths of whatever values my lookouts are currently standing on. I need to compare this combination against the target score."

4. "Is this the guy?"

Python
        if current_sum == target:
            return [left, right]
Thought Process: "If the current value matches the target exactly, stop looking. We found our match. Return the answer immediately."

5. "Adjust the left flank if we are falling short."

Python
        elif current_sum < target:
            left += 1
Thought Process: "Wait, the combined value is too small. Because the array is strictly sorted, moving the right pointer inward would only give me an even smaller number. The only path up is to step my left pointer forward to grab a larger number."

6. "Adjust the right flank if we overshot."

Python
        else:
            right -= 1
Thought Process: "Now the combination is too large. I need to reduce our total value. Stepping the left pointer forward would make it even bigger, so my only option is to step the right pointer backward to find a smaller number.

"""