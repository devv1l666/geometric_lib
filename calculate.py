import circle
import square

figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {'perimeter-circle': 1, 'area-circle': 1, 'perimeter-square': 1, 'area-square': 1}


def calc(fig1, func1, size1):
    assert fig1 in figs, f"Invalid figure: {fig1}. Choose from: {figs}"
    assert func1 in funcs, f"Invalid function: {func1}. Choose from: {funcs}"

    result = eval(f'{fig1}.{func1}(*{size1})')
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
            temp = "Input figure sizes separated by space, 1 for circle and square\n"
            size = list(map(int, input(temp).split(' ')))

    calc(fig, func, size)


square.area(3)
circle.area(3)
