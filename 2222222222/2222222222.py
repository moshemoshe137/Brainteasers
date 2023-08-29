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


solution_O_n_factorial()
