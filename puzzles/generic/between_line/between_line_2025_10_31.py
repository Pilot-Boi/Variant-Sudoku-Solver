"""PuzzleMadness Between Lines Sudoku — 2025-10-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-10-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/10/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 3, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 8, 7, 0, 0, 1],
        [6, 0, 0, 0, 0, 0, 7, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(6, 7), (5, 8), (4, 7), (4, 6), (4, 5), (5, 5)])
    puzzle.add_between_line([(4, 3), (4, 4), (3, 4), (2, 4), (3, 5)])
    puzzle.add_between_line([(0, 5), (1, 5), (1, 4), (2, 3), (2, 2)])
    puzzle.add_between_line([(6, 0), (7, 0), (8, 1), (7, 2), (6, 2)])
    puzzle.add_between_line([(7, 3), (7, 4), (6, 4), (6, 3)])
    puzzle.add_between_line([(0, 4), (1, 3), (1, 2), (0, 3)])
    puzzle.add_between_line([(3, 7), (3, 6), (2, 5), (1, 6)])
    puzzle.add_between_line([(0, 1), (0, 0), (1, 1), (1, 0)])
    puzzle.add_between_line([(3, 8), (2, 8), (2, 7)])
    puzzle.add_between_line([(3, 3), (4, 2), (4, 1)])
    puzzle.add_between_line([(5, 4), (6, 5), (7, 5)])
    puzzle.add_between_line([(7, 1), (6, 1), (5, 0)])

    return puzzle
