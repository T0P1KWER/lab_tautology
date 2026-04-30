from src.tree_node import TreeNode


class Operand(TreeNode):
    def __init__(self, name: str):
        self._name = name

    def solve(self, values: dict[str, int]) -> int:
        return values[self._name]
