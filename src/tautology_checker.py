from itertools import product

from src.tokenizer import Tokenizer
from src.tree_node import TreeNode


class TautologyChecker:
    @staticmethod
    def build_truth_table(tree: TreeNode, variables: list[str]) -> list[list[int]]:
        table: list[list[int]] = []

        for values in product([0, 1], repeat=len(variables)):
            state = dict(zip(variables, values))
            result = tree.solve(state)
            table.append(list(values) + [result])

        return table

    @staticmethod
    def is_tautology(table: list[list[int]]) -> bool:
        return all(row[-1] == 1 for row in table)

    @staticmethod
    def find_counterexample(table: list[list[int]], variables: list[str]) -> dict[str, int] | None:
        for row in table:
            if row[-1] == 0:
                return dict(zip(variables, row[:-1]))
        return None

    @staticmethod
    def format_table(table: list[list[int]], variables: list[str]) -> str:
        header = "  ".join(variables) + " | F"
        separator = "-" * len(header)
        lines = [header, separator]

        for row in table:
            values = "  ".join(str(value) for value in row[:-1])
            lines.append(f"{values} | {row[-1]}")

        return "\n".join(lines)

    @staticmethod
    def extract_variables(expression: str) -> list[str]:
        return Tokenizer.get_variables(Tokenizer.tokenize(expression))
