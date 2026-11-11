"""PuzzleMadness Between Lines Sudoku — 2025-03-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-03-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/3/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 2, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 6, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 4, 0, 9, 0, 0, 0],
        [0, 0, 9, 0, 1, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 8, 9, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 6), (3, 5), (4, 5), (3, 6), (4, 6), (5, 5)])
    puzzle.add_between_line([(3, 1), (4, 0), (5, 1), (5, 2), (6, 2)])
    puzzle.add_between_line([(1, 0), (1, 1), (2, 0), (2, 1), (3, 2)])
    puzzle.add_between_line([(7, 6), (8, 6), (7, 7), (6, 8), (7, 8)])
    puzzle.add_between_line([(4, 7), (5, 6), (6, 5), (6, 4)])
    puzzle.add_between_line([(1, 8), (0, 8), (0, 7), (0, 6)])
    puzzle.add_between_line([(2, 5), (1, 6), (2, 7), (3, 7)])
    puzzle.add_between_line([(7, 4), (7, 5), (6, 6), (6, 7)])
    puzzle.add_between_line([(1, 3), (1, 2), (0, 1)])
    puzzle.add_between_line([(6, 3), (5, 3), (4, 3)])
    puzzle.add_between_line([(3, 3), (2, 2), (2, 3)])
    puzzle.add_between_line([(5, 4), (4, 4), (3, 4)])

    return puzzle
