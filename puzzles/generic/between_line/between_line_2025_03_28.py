"""PuzzleMadness Between Lines Sudoku — 2025-03-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-03-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/3/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 6, 1, 0],
        [0, 1, 0, 9, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 3, 2, 0, 0, 0],
        [0, 8, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 3, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(7, 0), (6, 0), (5, 1), (4, 1), (3, 0), (3, 1)])
    puzzle.add_between_line([(6, 6), (7, 5), (8, 4), (7, 4), (8, 3)])
    puzzle.add_between_line([(3, 4), (4, 5), (3, 6), (4, 7), (3, 7)])
    puzzle.add_between_line([(2, 6), (2, 7), (2, 8), (1, 8), (0, 7)])
    puzzle.add_between_line([(1, 0), (2, 0), (1, 1), (1, 2)])
    puzzle.add_between_line([(8, 0), (8, 1), (7, 1), (6, 2)])
    puzzle.add_between_line([(4, 2), (5, 3), (5, 4), (5, 5)])
    puzzle.add_between_line([(0, 2), (1, 3), (2, 2), (2, 3)])
    puzzle.add_between_line([(0, 3), (0, 4), (1, 5)])
    puzzle.add_between_line([(7, 6), (7, 7), (7, 8)])
    puzzle.add_between_line([(2, 1), (3, 2), (3, 3)])

    return puzzle
