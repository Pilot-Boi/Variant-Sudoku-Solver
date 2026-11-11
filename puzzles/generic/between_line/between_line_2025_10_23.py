"""PuzzleMadness Between Lines Sudoku — 2025-10-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-10-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/10/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 6, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 3, 0, 0, 0, 0, 6, 0],
        [1, 0, 0, 0, 0, 0, 3, 0, 0],
        [6, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 1, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(3, 3), (4, 4), (5, 5), (5, 4), (6, 3), (7, 2)])
    puzzle.add_between_line([(8, 3), (8, 2), (7, 3), (6, 4), (6, 5)])
    puzzle.add_between_line([(2, 7), (1, 6), (0, 6), (1, 7), (0, 7)])
    puzzle.add_between_line([(3, 2), (2, 2), (2, 1), (2, 0), (3, 1)])
    puzzle.add_between_line([(7, 1), (6, 1), (6, 0), (7, 0), (8, 1)])
    puzzle.add_between_line([(6, 6), (7, 5), (8, 4), (8, 5)])
    puzzle.add_between_line([(5, 0), (5, 1), (4, 1), (4, 0)])
    puzzle.add_between_line([(1, 1), (0, 1), (0, 0), (1, 0)])
    puzzle.add_between_line([(5, 8), (4, 7), (3, 7)])
    puzzle.add_between_line([(3, 4), (2, 5), (2, 4)])
    puzzle.add_between_line([(2, 6), (3, 5), (4, 5)])

    return puzzle
