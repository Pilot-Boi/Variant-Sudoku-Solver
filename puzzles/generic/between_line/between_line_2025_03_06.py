"""PuzzleMadness Between Lines Sudoku — 2025-03-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-03-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/3/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 0, 0, 0, 0, 0, 0, 8],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 5, 0, 0, 0, 8, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 1, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 3, 2, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(7, 8), (8, 7), (7, 6), (7, 7), (6, 6), (7, 5)])
    puzzle.add_between_line([(3, 1), (2, 2), (3, 3), (3, 4), (4, 5)])
    puzzle.add_between_line([(3, 8), (4, 8), (5, 7), (6, 7), (6, 8)])
    puzzle.add_between_line([(4, 1), (5, 0), (6, 0), (7, 1), (8, 0)])
    puzzle.add_between_line([(8, 3), (7, 3), (8, 2), (8, 1)])
    puzzle.add_between_line([(4, 7), (3, 6), (3, 5), (2, 4)])
    puzzle.add_between_line([(2, 0), (1, 0), (0, 1), (0, 0)])
    puzzle.add_between_line([(1, 5), (1, 4), (0, 4), (1, 3)])
    puzzle.add_between_line([(1, 6), (2, 5), (2, 6)])
    puzzle.add_between_line([(3, 7), (2, 8), (2, 7)])
    puzzle.add_between_line([(0, 2), (1, 1), (1, 2)])

    return puzzle
