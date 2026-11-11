"""PuzzleMadness Between Lines Sudoku — 2025-05-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-05-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/5/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 4],
        [0, 0, 3, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 1, 0, 0, 3],
        [4, 0, 0, 0, 0, 2, 0, 0, 0],
        [5, 8, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(7, 4), (6, 4), (6, 5), (6, 6), (7, 6), (7, 7)])
    puzzle.add_between_line([(2, 5), (3, 4), (3, 5), (3, 6), (4, 6)])
    puzzle.add_between_line([(8, 0), (7, 1), (6, 1), (5, 2), (4, 2)])
    puzzle.add_between_line([(3, 3), (2, 2), (1, 1), (0, 1), (1, 0)])
    puzzle.add_between_line([(0, 5), (1, 5), (1, 6), (1, 7), (0, 6)])
    puzzle.add_between_line([(3, 0), (4, 1), (3, 2), (3, 1)])
    puzzle.add_between_line([(1, 2), (1, 3), (1, 4), (0, 4)])
    puzzle.add_between_line([(8, 8), (8, 7), (7, 8), (6, 7)])
    puzzle.add_between_line([(4, 5), (4, 4), (5, 4)])
    puzzle.add_between_line([(8, 2), (7, 2), (6, 2)])
    puzzle.add_between_line([(6, 8), (5, 7), (4, 8)])

    return puzzle
