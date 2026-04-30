from src.parser import Parser
from src.tokenizer import Tokenizer
class Validator:
    @staticmethod
    def validate(expression: str) -> tuple[bool, str]:
        try:
            tokens = Tokenizer.tokenize(expression)
        except ValueError as error:
            return False, str(error)

        if not tokens:
            return False, "Формула пуста."

        if not Tokenizer.get_variables(tokens):
            return False, "В формуле должна быть хотя бы одна переменная."

        try:
            Parser(tokens).parse()
        except ValueError as error:
            return False, str(error)

        return True, ""
