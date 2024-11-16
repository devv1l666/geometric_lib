import circle
import square

figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {'perimeter-circle': 1, 'area-circle': 1, 'perimeter-square': 1, 'area-square': 1}


def calc(fig, func, size):
    assert fig in figs, f"Invalid figure: {fig}. Choose from: {figs}"
    assert func in funcs, f"Invalid function: {func}. Choose from: {funcs}"

    result = eval(f'{fig}.{func}(*{size})')
    return result


if __name__ == "__main__":
    func = ''
    fig = ''
    size = []

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

        while func not in funcs:
            func = input(f"Enter function name, available are {funcs}:\n")

        while len(size) != sizes[f"{func}-{fig}"]:
            size = list(map(int, input(
                "Input figure sizes separated by space, 1 for circle and square\n"
            ).split(' ')))

    calc(fig, func, size)
