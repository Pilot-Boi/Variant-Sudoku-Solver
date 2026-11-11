"""PuzzleMadness Between Lines Sudoku — 2025-06-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-06-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/6/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [8, 4, 0, 0, 0, 0, 0, 3, 0],
        [7, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 1],
        [0, 0, 0, 0, 0, 3, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [3, 2, 7, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(7, 7), (7, 6), (8, 5), (7, 5), (6, 5), (5, 5)])
    puzzle.add_between_line([(8, 1), (7, 2), (6, 1), (7, 1), (6, 0)])
    puzzle.add_between_line([(5, 8), (6, 8), (5, 7), (4, 7), (3, 7)])
    puzzle.add_between_line([(2, 8), (1, 7), (2, 7), (3, 6), (3, 5)])
    puzzle.add_between_line([(6, 2), (5, 3), (6, 3), (7, 4)])
    puzzle.add_between_line([(6, 7), (7, 8), (8, 7), (8, 6)])
    puzzle.add_between_line([(1, 8), (0, 8), (0, 7), (1, 6)])
    puzzle.add_between_line([(1, 1), (1, 0), (2, 1), (2, 2)])
    puzzle.add_between_line([(5, 0), (4, 1), (5, 2)])
    puzzle.add_between_line([(3, 0), (3, 1), (4, 2)])
    puzzle.add_between_line([(4, 3), (5, 4), (4, 5)])
    puzzle.add_between_line([(3, 3), (2, 4), (2, 3)])

    return puzzle
