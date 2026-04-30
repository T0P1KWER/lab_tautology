from src.operand import Operand
from src.operator import BinaryOperator, UnaryOperator
from src.tree_node import TreeNode


class Parser:
    def __init__(self, tokens: list[str]):
        self._tokens = tokens
        self._index = 0

    def parse(self) -> TreeNode:
        if not self._tokens:
            raise ValueError("Пустая формула.")

        node = self._parse_equivalence()
        if self._index != len(self._tokens):
            raise ValueError("В формуле есть лишние символы.")
        return node

    def _parse_equivalence(self) -> TreeNode:
        node = self._parse_implication()
        while self._match("~"):
            right = self._parse_implication()
            node = BinaryOperator("~", node, right)
        return node

    def _parse_implication(self) -> TreeNode:
        node = self._parse_disjunction()
        while self._match("->"):
            right = self._parse_implication()
            node = BinaryOperator("->", node, right)
        return node

    def _parse_disjunction(self) -> TreeNode:
        node = self._parse_conjunction()
        while self._match("\\/"):
            right = self._parse_conjunction()
            node = BinaryOperator("\\/", node, right)
        return node

    def _parse_conjunction(self) -> TreeNode:
        node = self._parse_unary()
        while self._match("/\\"):
            right = self._parse_unary()
            node = BinaryOperator("/\\", node, right)
        return node

    def _parse_unary(self) -> TreeNode:
        if self._match("!"):
            return UnaryOperator("!", self._parse_unary())

        if self._match("("):
            node = self._parse_equivalence()
            self._consume(")")
            return node

        token = self._current_token()
        if token is None or not token.isalpha():
            raise ValueError("Ожидалась переменная или подформула в скобках.")

        self._index += 1
        return Operand(token)

    def _match(self, token: str) -> bool:
        if self._current_token() == token:
            self._index += 1
            return True
        return False

    def _consume(self, token: str) -> None:
        if not self._match(token):
            raise ValueError(f"Ожидался токен: {token}")

    def _current_token(self) -> str | None:
        if self._index >= len(self._tokens):
            return None
        return self._tokens[self._index]
