from src.parser import Parser
from src.tautology_checker import TautologyChecker
from src.tokenizer import Tokenizer
from src.validator import Validator


def execute() :
    expression = input("Введите формулу: ")
    is_valid, error_message = Validator.validate(expression)

    if not is_valid:
        print(f"Некорректная формула: {error_message}")
        return

    tokens = Tokenizer.tokenize(expression)
    tree = Parser(tokens).parse()
    variables = Tokenizer.get_variables(tokens)
    table = TautologyChecker.build_truth_table(tree, variables)

    print("\nТаблица истинности:")
    print(TautologyChecker.format_table(table, variables))

    if TautologyChecker.is_tautology(table):
        print("\nФормула является тавтологией.")
    else:
        counterexample = TautologyChecker.find_counterexample(table, variables)
        print("\nФормула не является тавтологией.")
        if counterexample is not None:
            values = ", ".join(f"{name}={value}" for name, value in counterexample.items())
            print(f"Контрпример: {values}")


def menu():
    while True:
        print("\nМеню:")
        print("1. Проверить, является ли формула тавтологией")
        print("0. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            execute()
        elif choice == "0":
            break
        else:
            print("Некорректный выбор.")





if __name__ == "__main__":
    menu()
