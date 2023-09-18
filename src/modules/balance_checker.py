class BalanceCheckResult:
    def __init__(self, error, raw_str, bracket_index):
        self.error = error
        self.raw_str = raw_str
        self.bracket_index = bracket_index


class BalanceChecker:
    def __init__(self):
        self.bracket_stack = []
        self.brackets = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        self.bracket_keys = self.brackets.keys()

    def check(self, str: str) -> BalanceCheckResult:
        """
        Function checks brackets balance.
        Works with text partials.
        Arguments:
        str - string to check for bracket errors;
        """

        for ind in range(len(str)):
            char = str[ind]
            if char in self.bracket_keys:
                self.bracket_stack.append((char, ind))
            elif char in self.brackets.values():
                if not self.bracket_stack:
                    return BalanceCheckResult(
                        "Unmatched closing bracket", str, ind)
                last_op_br, open_br_ind = self.bracket_stack.pop()
                expected_closing_bracket = self.brackets[last_op_br]
                if char != expected_closing_bracket:
                    return BalanceCheckResult(
                        "Mismatched closing bracket", str, ind)

        # Check for any unmatched opening brackets
        if self.bracket_stack:
            last_op_br, open_br_ind = self.bracket_stack.pop()
            return BalanceCheckResult(
                "Unmatched opening bracket", str, open_br_ind)

        # If no errors were found
        return BalanceCheckResult(False, str, -1)
