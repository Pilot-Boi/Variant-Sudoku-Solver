"""PuzzleMadness Between Lines Sudoku — 2025-04-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-04-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/4/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [3, 2, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 7, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 3, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 7, 2, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 2), (2, 3), (1, 4), (1, 3), (0, 3), (0, 4)])
    puzzle.add_between_line([(4, 6), (3, 6), (2, 6), (1, 7), (0, 8)])
    puzzle.add_between_line([(3, 3), (4, 2), (4, 1), (5, 0), (5, 1)])
    puzzle.add_between_line([(8, 7), (7, 6), (7, 7), (6, 8), (7, 8)])
    puzzle.add_between_line([(5, 3), (5, 2), (6, 1), (6, 0)])
    puzzle.add_between_line([(3, 8), (4, 7), (4, 8), (5, 7)])
    puzzle.add_between_line([(0, 0), (1, 0), (0, 1), (1, 1)])
    puzzle.add_between_line([(7, 4), (8, 5), (7, 5), (6, 5)])
    puzzle.add_between_line([(2, 0), (3, 0), (4, 0)])
    puzzle.add_between_line([(8, 1), (7, 2), (6, 2)])
    puzzle.add_between_line([(5, 8), (6, 7), (5, 6)])

    return puzzle
