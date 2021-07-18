"""Часть проекта по сканированию луны - подсчет количества лунных кратеров."""

import sys
import numpy


"""Передаем введенный через консоль путь до файла в переменную"""
text_file = str(sys.argv[1])


def calculate(matrix: list, row: int, column: int) -> bool:
    """Функция, которая ищет в переданной матрице кратеры, проходясь по её элементам."""
    if len(matrix) == 0:
        return False
    if row < 0 or column < 0:
        return False
    if row > len(matrix) - 1 or column > len(matrix[0]) - 1:
        return False
#    matrix[row][column] = 0
    calculate(matrix, row + 1, column)
    calculate(matrix, row - 1, column)
    calculate(matrix, row, column + 1)
    calculate(matrix, row, column - 1)
    return True


def crater_counter_function(matrix) -> int:
    if not matrix:
        return 0
    number_of_craters = 0
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column] == 1:
                number_of_craters += 1
                calculate(matrix, row, column)
            return number_of_craters


def file_to_array(path_to_file) -> None:
    with open(path_to_file, "r") as f:
        moon_matrix = f.read()
        input_data = numpy.array(moon_matrix)
        crater_counter_function(input_data)


if __name__ == "__main__":
    print(crater_counter_function(text_file))
