from module_stack import Stack
import itertools

"""
 Python3 code to check for
 balanced parentheses in an expression
"""


def check_parenthesis(sti):
    parentthesis_d = {'(': ')', '[': ']', '{': '}'}
    parenthesis_s = set(itertools.chain((k for k in parentthesis_d), (v for v in parentthesis_d.values())))
    s = ''.join(c for c in sti if c in parenthesis_s)
    st = Stack()
    for c in s:
        if parentthesis_d.get(c, False):
            wait_c = parentthesis_d[c]
            st.push(wait_c)
        else:
            if st.is_Empty():
                return False
            if c == wait_c:
                st.pop()
                wait_c = st.peek()
            else:
                return False
    return True if st.is_Empty() else False


if __name__ == "__main__":
    stt = '({[]})'
    ans = check_parenthesis(stt)
    print(f'{stt} {"Сбалансировано" if ans else "Не сбалансировано"}')
    stt = '[{}{})(]'
    ans = check_parenthesis(stt)
    print(f'{stt} {"Сбалансировано" if ans else "Не сбалансировано"}')
    stt = '(((([{}]))))'
    ans = check_parenthesis(stt)
    print(f'{stt} {"Сбалансировано" if ans else "Не сбалансировано"}')
    stt = '[([])((([[[]]])))]{()}'
    ans = check_parenthesis(stt)
    print(f'{stt} {"Сбалансировано" if ans else "Не сбалансировано"}')
    stt = '{{[()]}}'
    ans = check_parenthesis(stt)
    print(f'{stt} {"Сбалансировано" if ans else "Не сбалансировано"}')
    stt = '}{}'
    ans = check_parenthesis(stt)
    print(f'{stt} {"Сбалансировано" if ans else "Не сбалансировано"}')
    stt = '{{[(])]}}'
    ans = check_parenthesis(stt)
    print(f'{stt} {"Сбалансировано" if ans else "Не сбалансировано"}')
    stt = '[[{())}]'
    ans = check_parenthesis(stt)
    print(f'{stt} {"Сбалансировано" if ans else "Не сбалансировано"}')


# Function to check parentheses
# def check(myStr):
#     stack = []
#     for i in myStr:
#         if i in open_list:
#             stack.append(i)
#         elif i in close_list:
#             pos = close_list.index(i)
#             if ((len(stack) > 0) and
#                     (open_list[pos] == stack[len(stack) - 1])):
#                 stack.pop()
#             else:
#                 return "Unbalanced"
#     if len(stack) == 0:
#         return "Balanced"
#     else:
#         return "Unbalanced"


# Driver code
# string = "{[]{()}}"
# print(string, "-", check(string))
#
# string = "[{}{})(]"
# print(string, "-", check(string))
#
# string = "((()"
# print(string, "-", check(string))
#

# Python3 program to check for
# balanced brackets.

# function to check if
# brackets are balanced


# def areBracketsBalanced(expr):
#     stack = []
#
#     # Traversing the Expression
#     for char in expr:
#         if char in ["(", "{", "["]:
#
#             # Push the element in the stack
#             stack.append(char)
#         else:
#
#             # IF current character is not opening
#             # bracket, then it must be closing.
#             # So stack cannot be empty at this point.
#             if not stack:
#                 return False
#             current_char = stack.pop()
#             if current_char == '(':
#                 if char != ")":
#                     return False
#             if current_char == '{':
#                 if char != "}":
#                     return False
#             if current_char == '[':
#                 if char != "]":
#                     return False
#
#     # Check Empty Stack
#     if stack:
#         return False
#     return True
#
#
# # Driver Code
# if __name__ == "__main__":
#     expr = "{()}[]"
#
#     # Function call
#     if areBracketsBalanced(expr):
#         print("Balanced")
#     else:
#         print("Not Balanced")

# This code is contributed by AnkitRai01 and improved
# by Raju Pitta

