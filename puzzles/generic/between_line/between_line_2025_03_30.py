"""PuzzleMadness Between Lines Sudoku — 2025-03-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-03-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/3/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 4],
        [0, 0, 0, 3, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 7, 0, 0, 0, 0, 6],
        [5, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 1, 0, 9, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(6, 3), (5, 2), (4, 2), (5, 3), (5, 4), (4, 3)])
    puzzle.add_between_line([(2, 4), (1, 5), (0, 4), (0, 3), (1, 4)])
    puzzle.add_between_line([(3, 1), (4, 0), (5, 1), (6, 2), (7, 1)])
    puzzle.add_between_line([(4, 4), (4, 5), (3, 5), (3, 6), (2, 5)])
    puzzle.add_between_line([(8, 7), (7, 7), (6, 7), (5, 6), (5, 7)])
    puzzle.add_between_line([(7, 5), (6, 4), (6, 5), (6, 6)])
    puzzle.add_between_line([(0, 5), (1, 6), (1, 7), (1, 8)])
    puzzle.add_between_line([(3, 7), (2, 7), (3, 8), (4, 8)])
    puzzle.add_between_line([(1, 0), (2, 0), (2, 1), (3, 2)])
    puzzle.add_between_line([(8, 8), (7, 8), (6, 8)])
    puzzle.add_between_line([(8, 0), (8, 1), (7, 0)])
    puzzle.add_between_line([(3, 3), (2, 3), (2, 2)])

    return puzzle
