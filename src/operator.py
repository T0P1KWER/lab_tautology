from src.tree_node import TreeNode


class UnaryOperator(TreeNode):
    def __init__(self, operator: str, operand: TreeNode):
        self._operator = operator
        self._operand = operand

    def solve(self, values: dict[str, int]) -> int:
        if self._operator == "!":
            return 1 - self._operand.solve(values)
        raise ValueError(f"Неизвестный унарный оператор: {self._operator}")


class BinaryOperator(TreeNode):
    def __init__(self, operator: str, left: TreeNode, right: TreeNode):
        self._operator = operator
        self._left = left
        self._right = right

    def solve(self, values: dict[str, int]) -> int:
        left_value = self._left.solve(values)
        right_value = self._right.solve(values)

        if self._operator == "/\\":
            return left_value * right_value
        if self._operator == "\\/":
            return left_value + right_value - left_value * right_value
        if self._operator == "->":
            return int((not left_value) or right_value)
        if self._operator == "~":
            return int(left_value == right_value)

        raise ValueError(f"Неизвестный бинарный оператор: {self._operator}")
