import pathlib
import typing as tp
import random

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """ Прочитать Судоку из указанного файла """

    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    """ Вывод Судоку """
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)
            )
        )
        if str(row) in "25":
            print(line)
    print()


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    """ Сгруппировать значения values в список, состоящий из списков по n элементов """

    return [values[i * n:(i + 1) * n] for i in range(n)]


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """ Возвращает все значения для номера строки, указанной в pos """

    return grid[pos[0]]


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """ Возвращает все значения для номера столбца, указанного в pos"""

    return [grid[i][pos[1]] for i in range(0, len(grid))]


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """ Возвращает все значения из квадрата, в который попадает позиция pos """

    result = []
    for i in range(pos[0] // 3 * 3, (pos[0] // 3) * 3 + 3):
        for j in range(pos[1] // 3 * 3, (pos[1] // 3) * 3 + 3):
            result.append(grid[i][j])
    return result


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """ Найти первую свободную позицию в пазле """

    a = [-1, -1]
    for i in range(len(grid)):
        for j in range(len(grid)):
            if (grid[i][j] == '.'):
                a[0] = i
                a[1] = j
                break
    return tuple(a)


def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    """ Вернуть множество возможных значения для указанной позиции """

    return set('123456789') - set(get_row(grid, pos)) - set(get_col(grid, pos)) - set(get_block(grid, pos))


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """ Решение пазла, заданного в grid """
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла 
    """

    if find_empty_positions(grid) == (-1, -1):
        return grid

    a = find_empty_positions(grid)[0]
    b = find_empty_positions(grid)[1]

    for i in find_possible_values(grid, find_empty_positions(grid)):
        grid[a][b] = i
        if solve(grid):
            return solve(grid)

    grid[a][b] = '.'


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """ Если решение solution верно, то вернуть True, в противном случае False """

    for i in range(9):
        if [set(get_row(solution, (i, 0))) != set('123456789')] \
                or [set(get_col(solution, (0))) != set('123456789')] \
                or [set(get_block(solution, ((i // 3) * 3, (i % 3) * 3))) != set('123456789')]:
            return False
        else:
            return True


def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """Генерация судоку заполненного на N элементов"""

    new = solve([['.' for j in range(9)] for i in range(9)])

    while (N < 81):
        i = random.randint(0, 8)
        j = random.randint(0, 8)
        if new[i][j] != '.':
            new[i][j] = '.'
            N += 1
    return new


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)
