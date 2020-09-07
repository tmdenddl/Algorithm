"""
Min Stack - Easy #155

Design a stack that supports push, pop, top, and retrieving the minimum element

push(x)   : push element x onto the stack
pop(x)    : removes the element on top of the stack
top( )    : get the top element
getMin( ) : retrieve the minimum element of the stack

"""

class MinStack:

    def __init__(self):
        self.st = []

    def push(self, x: int) -> None:
        # Get current minimum value of the stack
        currMin = self.getMin()

        # If there is no currMin or currMin is bigger than x,
        # x is now the currMin
        if (currMin == None or currMin > x):
            currMin = x

        # Append push x and currMin to the stack
        self.st.append((x, currMin))

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        # If the stack is not empty, return the first value of top of the stack (x)
        # else, return None
        return self.st[-1][0] if self.st else None

    def getMin(self) -> int:
        # If the stack is not empty, return the second value of top of the stack (currMin)
        # else, return None
        return self.st[-1][1] if self.st else None
        
        
"""
Time Complexity
    - push()   : O(1)
    - pop()    : O(1)
    - top()    : O(1)
    - getMin() : O(1)
"""