"""PuzzleMadness Between Lines Sudoku — 2025-02-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-02-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/2/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 3, 0, 6, 0, 0, 0, 5, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 7, 9, 0, 4],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 2, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(8, 1), (7, 1), (6, 1), (5, 0), (4, 0), (3, 0)])
    puzzle.add_between_line([(8, 8), (8, 7), (8, 6), (7, 5), (6, 6)])
    puzzle.add_between_line([(7, 3), (6, 3), (6, 2), (5, 3), (6, 4)])
    puzzle.add_between_line([(3, 3), (4, 2), (3, 2), (2, 3), (2, 4)])
    puzzle.add_between_line([(4, 4), (3, 5), (2, 5), (2, 6), (1, 6)])
    puzzle.add_between_line([(6, 7), (7, 7), (7, 8), (6, 8)])
    puzzle.add_between_line([(0, 4), (1, 4), (0, 3), (1, 3)])
    puzzle.add_between_line([(1, 0), (2, 1), (3, 1), (4, 1)])
    puzzle.add_between_line([(3, 6), (4, 5), (4, 6)])
    puzzle.add_between_line([(4, 7), (4, 8), (5, 8)])
    puzzle.add_between_line([(3, 7), (3, 8), (2, 8)])

    return puzzle
