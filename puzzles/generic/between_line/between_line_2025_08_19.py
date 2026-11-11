"""PuzzleMadness Between Lines Sudoku — 2025-08-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-08-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/8/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 1, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 6, 1],
        [0, 2, 0, 5, 0, 0, 0, 0, 8],
        [7, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 7, 0],
        [0, 0, 0, 6, 0, 0, 0, 9, 0],
        [0, 0, 0, 1, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(7, 5), (8, 4), (7, 4), (6, 4), (5, 3), (6, 2)])
    puzzle.add_between_line([(7, 0), (6, 1), (7, 1), (7, 2), (7, 3)])
    puzzle.add_between_line([(3, 3), (3, 2), (4, 3), (5, 4), (5, 5)])
    puzzle.add_between_line([(1, 0), (0, 1), (1, 1), (1, 2), (0, 2)])
    puzzle.add_between_line([(0, 5), (0, 4), (0, 3), (1, 3)])
    puzzle.add_between_line([(1, 6), (2, 6), (3, 7), (2, 7)])
    puzzle.add_between_line([(3, 4), (2, 4), (3, 5), (3, 6)])
    puzzle.add_between_line([(1, 4), (2, 3), (2, 2)])
    puzzle.add_between_line([(0, 7), (1, 7), (2, 8)])
    puzzle.add_between_line([(7, 8), (6, 8), (5, 7)])
    puzzle.add_between_line([(6, 0), (5, 0), (4, 1)])

    return puzzle
