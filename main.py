"""Часть проекта по сканированию луны - подсчет количества лунных кратеров."""

import sys
import ast


"""Передаем введенный через консоль путь до файла в переменную"""
text_file = str(sys.argv[1])


def crater_finder(matrix: list, row: int, column: int) -> bool:
    """Функция, которая ищет в переданной матрице кратеры, проходясь по её элементам."""
    if len(matrix) == 0:
        return False
    if row < 0 or column < 0:
        return False
    if row > len(matrix) - 1 or column > len(matrix[row]) - 1:
        return False
    if matrix[row][column] == 1:
        matrix[row][column] = 0
        #  Двигаемся вверх.
        crater_finder(matrix, row + 1, column)
        #  Двигаемся вниз.
        crater_finder(matrix, row - 1, column)
        #  Двигаемся вправо.
        crater_finder(matrix, row, column + 1)
        #  Двигаемся влево.
        crater_finder(matrix, row, column - 1)
        return True
    return False


def calculate(matrix: list) -> int:
    """Функция - счетчик, которая подсчитывает количество кратеров."""
    """Использует данные, полученные в результате исполнения функции calculate()."""
    number_of_craters = 0
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if crater_finder(matrix, row, column):
                number_of_craters += 1
    return number_of_craters


def file_to_array(path_to_file: str) -> int:
    """Функция, преобразовывающая строки, прочитанные из файла, в матрицу, и передающая ее дальше для расчетов."""
    with open(path_to_file, "r") as f:
        moon_matrix = ast.literal_eval(f.read())
        return calculate(moon_matrix)


if __name__ == "__main__":
    print(file_to_array(text_file))
