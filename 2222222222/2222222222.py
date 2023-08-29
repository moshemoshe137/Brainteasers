string = "2" * 10  # 2222222222


def solution() -> None:
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


solution()
