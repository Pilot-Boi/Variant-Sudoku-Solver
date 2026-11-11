"""PuzzleMadness Between Lines Sudoku — 2025-03-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-03-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/3/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 3, 0, 0, 0, 0, 9],
        [0, 3, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 5, 4, 0, 0, 0, 0, 0, 8],
        [0, 9, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 9, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(8, 0), (8, 1), (7, 2), (6, 3), (6, 4), (7, 4)])
    puzzle.add_between_line([(0, 0), (1, 0), (1, 1), (0, 2), (0, 1)])
    puzzle.add_between_line([(1, 7), (2, 7), (2, 6), (3, 6), (3, 7)])
    puzzle.add_between_line([(1, 3), (2, 3), (2, 4), (3, 4), (4, 3)])
    puzzle.add_between_line([(7, 8), (8, 8), (7, 7), (8, 6)])
    puzzle.add_between_line([(0, 7), (1, 6), (2, 5), (3, 5)])
    puzzle.add_between_line([(3, 0), (2, 0), (2, 1), (1, 2)])
    puzzle.add_between_line([(4, 6), (4, 7), (5, 6)])
    puzzle.add_between_line([(2, 2), (3, 3), (3, 2)])
    puzzle.add_between_line([(5, 0), (4, 1), (4, 2)])

    return puzzle
