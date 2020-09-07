"""
Valid Parenthesis - Easy #020

Given a string that can contain '(', ')', '{', '}', '[' and ']'
Find if the string is valid where a string is valid if it fulfils the following criteria
    - Open brackets must be closed by the same kind of brackets
    - Open brackets must be closed in the correct order

Example:

Input: S = "{[]}"
Output: True

Input: S = "{[}"
Output: False


"""

class Solution:

    def isEqual(self, c1, c2):
        # If the c1 is an open parenthesis 
        # and c2 is a closing paranthesis,
        # return True, else False
        if (c1 == '(' and c2 == ')'):
            return True
        if (c1 == '[' and c2 == ']'):
            return True
        if (c1 == '{' and c2 == '}'):
            return True 
        return False

    def validParenthesis(slef, s: str) -> bool:
        st = []
        for character in s:
            # If the stack is not empty,
            # get the character on the top
            if(len(st) != 0):
                li = st[-1]
                # If the character on the top of the stack 
                # is a open parenthesis of the current character,
                # remove the top character on the stack and continue with the iteration
                if (self.isEqual(li, character)):
                    st.pop()
                    continue
            st.append(character)
        return len(st) == 0
            

        
        
"""
Time Complexity : O(n)
Space Complexity: O(n)
"""