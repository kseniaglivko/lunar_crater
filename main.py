
"""Часть проекта по сканированию луны - подсчет количества лунных кратеров."""

import os
import sys
import ast


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
    if matrix[row][column] == 1:
        matrix[row][column] = 0
        calculate(matrix, row + 1, column)
        calculate(matrix, row - 1, column)
        calculate(matrix, row, column + 1)
        calculate(matrix, row, column - 1)
        return True


def crater_counter_function(matrix: list) -> int:
    if not matrix:
        return 0
    number_of_craters = 0
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if calculate(matrix, row, column):
                number_of_craters += 1
    return number_of_craters


def file_to_array(path_to_file: str) -> int:
    with open(path_to_file, "r") as f:
        try:
            moon_matrix = ast.literal_eval(f.read())
        except SyntaxError:
            return "Пустой файл!"
        return crater_counter_function(moon_matrix)


if __name__ == "__main__":
    print(file_to_array(text_file))
