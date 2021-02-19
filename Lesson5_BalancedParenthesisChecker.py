import collections

class BalancedParenthesisChecker:

    def __init__(self):
        self.open_close_parens_pairs = {")": "(", "]": "[", "}": "{"}

    def is_open_paren(self, ch):
        is_open = False

        if ch == "(" or ch == "[" or ch == "{":
            is_open = True

        return is_open

    def is_close_paren(self, ch):
        is_close = False

        if ch == ")" or ch == "]" or ch == "}":
            is_close = True

        return is_close

    def parens_are_balanced(self, input_str):
        open_parens = collections.deque()
        str_index = 0
        while str_index < len(input_str):
            if self.is_open_paren(input_str[str_index]):
                open_parens.append(input_str[str_index])
            elif self.is_close_paren(input_str[str_index]):
                # Question: what check is missing here?
                if len(open_parens) > 0:
                    last_open_paren_seen = open_parens.pop()
                    if self.open_close_parens_pairs[input_str[str_index]] != last_open_paren_seen:
                        return False
                else:
                    return False
            str_index += 1
        return len(open_parens) == 0


checker = BalancedParenthesisChecker()
print(checker.parens_are_balanced("()"))
print(checker.parens_are_balanced("[]"))
print(checker.parens_are_balanced("{}"))
print(checker.parens_are_balanced("[][[]]"))
print(checker.parens_are_balanced("[]([{}])"))

print(checker.parens_are_balanced("()["))
print(checker.parens_are_balanced("([)]"))
print(checker.parens_are_balanced("}{"))
print(checker.parens_are_balanced("[]}"))
