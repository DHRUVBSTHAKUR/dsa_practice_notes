#@author Dhruv
def dfs(root):
    if not root :
        return 0
    left_depth = dfs(root.left)
    right_depth =dfs(root.right)

    return max(left_depth,right_depth)+1

"""
Only thing that change is where we put the print statement 

Pre-order: print is on top of both recursive calls.

In-order: print is in the middle of the recursive calls.

Post-order: print is at the bottom under both recursive calls.

Level-order: print happens as soon as you pop from the deque.

🕵️‍♂️ Pattern 8: Tree DFS (Recursion)
The Crime Scene Investigation (The "Smell Test"):
Look for these clues. If you see them, ditch the Queue and prepare to write a recursive function:

The "Path" Clue: "Find the max path sum," "Print all paths from root to leaf," "Lowest Common Ancestor."

The "Extremes" Clue: "Max depth," "Min depth," "Count all leaves."

The "Order" Clue: The problem explicitly asks for "Preorder", "Inorder" (gives you a sorted array in a BST), or "Postorder" traversal.

"""