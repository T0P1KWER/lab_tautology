class Tokenizer:
    tokens2 = {"/\\", "\\/", "->"}
    tokens1 = {"(", ")", "!", "~"}

    @staticmethod
    def tokenize(expression: str) -> list[str]:
        cleaned_str = expression.replace(" ", "")
        tokens: list[str] = []
        index = 0
        while index < len(cleaned_str):
            symbol = cleaned_str[index]
            if symbol.isalpha() or symbol.isdigit():
                tokens.append(symbol.upper())
                index += 1
                continue

            if symbol in Tokenizer.tokens1:
                tokens.append(symbol)
                index += 1
                continue

            if index + 1 < len(cleaned_str):
                temp = cleaned_str[index:index + 2]
                if temp in Tokenizer.tokens2:
                    tokens.append(temp)
                    index += 2
                    continue

        return tokens

    @staticmethod
    def get_variables(tokens: list[str]) -> list[str]:
        return sorted({token for token in tokens if token.isalpha()})
