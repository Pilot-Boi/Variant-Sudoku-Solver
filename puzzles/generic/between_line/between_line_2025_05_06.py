"""PuzzleMadness Between Lines Sudoku — 2025-05-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-05-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/5/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 6, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 6, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 2, 4, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 1, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(7, 5), (6, 6), (6, 7), (5, 6), (4, 5), (4, 4)])
    puzzle.add_between_line([(2, 2), (2, 1), (2, 0), (1, 0), (0, 1)])
    puzzle.add_between_line([(6, 4), (5, 3), (4, 2), (3, 2), (3, 3)])
    puzzle.add_between_line([(4, 0), (3, 0), (4, 1), (5, 1), (5, 2)])
    puzzle.add_between_line([(1, 2), (1, 3), (2, 4), (3, 5), (2, 5)])
    puzzle.add_between_line([(7, 7), (6, 8), (5, 7), (5, 8)])
    puzzle.add_between_line([(1, 8), (2, 8), (2, 7), (3, 8)])
    puzzle.add_between_line([(1, 6), (0, 7), (0, 6), (0, 5)])
    puzzle.add_between_line([(8, 3), (7, 2), (7, 1), (6, 0)])
    puzzle.add_between_line([(6, 5), (5, 4), (4, 3)])
    puzzle.add_between_line([(3, 7), (3, 6), (4, 6)])
    puzzle.add_between_line([(0, 4), (1, 4), (1, 5)])

    return puzzle
