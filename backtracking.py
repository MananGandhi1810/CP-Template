def get_combinations(arr: list) -> list[list]:
    result = []

    def backtrack(start: int, current: list):
        result.append(current[:])

        for i in range(start, len(arr)):
            current.append(arr[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result


def get_permutations(arr: list) -> list[list]:
    result = []

    def backtrack(current: list, remaining: list):
        if not remaining:
            result.append(current[:])
            return

        for i in range(len(remaining)):
            current.append(remaining[i])
            backtrack(current, remaining[:i] + remaining[i + 1 :])
            current.pop()

    backtrack([], arr)
    return result
