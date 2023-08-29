import functools
import itertools
import math

from tqdm import tqdm as og_tqdm

string = "2" * 10  # 2222222222
string += "**"  # 2222222222**

already_tried = []
max_result = 0

tqdm = functools.partial(
    og_tqdm,
    dynamic_ncols=True,
)

for trial in tqdm(itertools.permutations(string), total=math.factorial(len(string))):
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
