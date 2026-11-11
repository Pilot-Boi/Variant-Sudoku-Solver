"""PuzzleMadness Between Lines Sudoku — 2025-07-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-07-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/7/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 4, 0, 0, 0, 0, 0, 8, 7],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 6, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 1, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 2, 0, 1, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(1, 6), (1, 5), (2, 6), (3, 7), (2, 8), (1, 8)])
    puzzle.add_between_line([(3, 1), (3, 2), (2, 1), (1, 1), (1, 2)])
    puzzle.add_between_line([(3, 8), (4, 8), (4, 7), (5, 6), (4, 6)])
    puzzle.add_between_line([(7, 3), (7, 2), (6, 3), (7, 4), (6, 4)])
    puzzle.add_between_line([(1, 3), (2, 4), (3, 4), (3, 3)])
    puzzle.add_between_line([(3, 0), (4, 0), (5, 1), (5, 2)])
    puzzle.add_between_line([(0, 4), (0, 5), (0, 6), (1, 7)])
    puzzle.add_between_line([(1, 0), (0, 1), (0, 0)])
    puzzle.add_between_line([(6, 2), (5, 3), (4, 3)])
    puzzle.add_between_line([(8, 5), (8, 6), (7, 5)])
    puzzle.add_between_line([(7, 7), (7, 8), (8, 7)])

    return puzzle
