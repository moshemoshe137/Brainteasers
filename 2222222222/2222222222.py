import functools
import itertools
import math

from tqdm import tqdm as og_tqdm

tqdm = functools.partial(
    og_tqdm,
    dynamic_ncols=True,
)

string = "2" * 10  # 2222222222


def solution_O_n_factorial() -> None:
    string_star = string + "**"  # 2222222222**
    already_tried = []
    max_result = 0

    for trial in tqdm(
        itertools.permutations(string_star), total=math.factorial(len(string_star))
    ):
        if trial in already_tried:
            continue
        trial_str = "".join(trial)
        if "**" in trial_str or trial_str.startswith("*") or trial_str.endswith("*"):
            continue
        already_tried.append(trial)
        result = eval(trial_str)
        if result > max_result:
            max_result = result
            max_expr = trial_str

    print(f"{max_expr} = {max_result:,}")


# solution_O_n_factorial()


def solution_O_n() -> None:
    max_result = 0

    for first_times_pos in range(1, len(string)):
        for second_times_pos in range(first_times_pos + 1, len(string) - 1):
            left = first_times_pos
            middle = second_times_pos - left
            right = len(string) - second_times_pos
            # middle = len(string) - left - right

            left2 = int("2" * left)
            middle2 = int("2" * middle)
            right2 = int("2" * right)

            result = left2 * middle2 * right2
            if result > max_result:
                max_result = result
                max_expr = f"{left2:,} * {middle2:,} * {right2:,} = {max_result:,}"
    print(max_expr)


solution_O_n()
