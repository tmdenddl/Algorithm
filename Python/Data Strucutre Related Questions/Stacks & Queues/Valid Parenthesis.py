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

    def validParenthesis(self, s: str) -> bool:
        # Initialize a stack
        st = []

        # Start looping over the input string
        for character in s:
            # If the stack is not empty, get the character on the top
            if(len(st) != 0):
                li = st[-1]

                # If the character on the top of the stack is a open parenthesis, 
                # and if the current character is a closing parenthesis of the same type,
                # remove the top character on the stack and continue with the iteration.
                # Note: we don't remove the top character from the stack if the match is invalid
                if (self.isEqual(li, character)):
                    st.pop()
                    continue
            # If the two parenthesis are not a match, append the current character to the stack
            st.append(character)

        # By the time we each return statement, if there are elements present in the stack,
        # given parenthesis were not valid
        return len(st) == 0
            

        
        
"""
Time Complexity : O(n)
Space Complexity: O(n)
"""