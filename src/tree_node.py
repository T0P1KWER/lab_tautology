from abc import ABC, abstractmethod


class TreeNode(ABC):
    @abstractmethod
    def solve(self, values: dict[str, int]) -> int:
        pass
