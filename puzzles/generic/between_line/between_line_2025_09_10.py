"""PuzzleMadness Between Lines Sudoku — 2025-09-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-09-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/9/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 7, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 9],
        [9, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 3, 0, 0, 6, 0, 5, 0],
        [0, 0, 0, 0, 5, 0, 6, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(0, 3), (1, 4), (2, 5), (2, 6), (3, 6), (2, 7)])
    puzzle.add_between_line([(5, 6), (5, 5), (4, 6), (5, 7), (4, 7)])
    puzzle.add_between_line([(4, 5), (4, 4), (5, 3), (5, 2), (6, 3)])
    puzzle.add_between_line([(3, 4), (2, 4), (3, 3), (2, 2), (2, 3)])
    puzzle.add_between_line([(3, 1), (4, 0), (5, 1), (4, 1), (3, 2)])
    puzzle.add_between_line([(6, 8), (7, 8), (6, 7), (7, 6)])
    puzzle.add_between_line([(6, 4), (7, 3), (6, 2), (7, 2)])
    puzzle.add_between_line([(0, 0), (1, 1), (2, 1), (1, 2)])
    puzzle.add_between_line([(1, 8), (0, 8), (1, 7)])
    puzzle.add_between_line([(8, 2), (8, 1), (8, 0)])
    puzzle.add_between_line([(5, 0), (6, 1), (7, 1)])

    return puzzle
