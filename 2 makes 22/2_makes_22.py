import itertools

NUM_TO_USE = 2
NUM_REPEATS = 7
DESIRED_RESULT = 22


def apply_operator(num1: float, num2: float, operator: str) -> float:
    return eval(f"{num1}{operator}{num2}")


allowed_operators = ["+", "-", "*", "/", "**"]
count = 0
# while result != 22:
for operators in itertools.product(allowed_operators, repeat=NUM_REPEATS - 1):
    result: float = NUM_TO_USE  # as long as `NUM_TO_USE != DESIRED_RESULT`
    result_str = ""
    for operator in operators:
        result = apply_operator(result, NUM_TO_USE, operator)

    if result == DESIRED_RESULT:
        print(f"Found in {count:,} tries!!")

        for operator in operators:
            result_str += f"{NUM_TO_USE}) {operator} "
            result_str = "(" + result_str
        result_str += f"{NUM_TO_USE} = {DESIRED_RESULT}"
        # Remove one pair of extra parentheses
        result_str = result_str.replace(f"({NUM_TO_USE})", f"{NUM_TO_USE}")
        print(result_str)
        print()
    count += 1
