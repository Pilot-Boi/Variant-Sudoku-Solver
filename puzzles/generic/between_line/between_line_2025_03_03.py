"""PuzzleMadness Between Lines Sudoku — 2025-03-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-03-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/3/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 0, 0, 0, 0, 5, 3],
        [0, 0, 0, 9, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 9, 7, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 1, 9, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 5, 0, 9, 0, 2, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(0, 6), (0, 7), (0, 8), (1, 7), (1, 6), (0, 5)])
    puzzle.add_between_line([(3, 1), (4, 1), (5, 2), (5, 3), (4, 2)])
    puzzle.add_between_line([(6, 1), (5, 0), (6, 0), (7, 1), (8, 0)])
    puzzle.add_between_line([(0, 0), (1, 1), (1, 2), (2, 1), (3, 2)])
    puzzle.add_between_line([(4, 0), (5, 1), (6, 2), (7, 2), (7, 3)])
    puzzle.add_between_line([(3, 6), (4, 7), (5, 8), (4, 8)])
    puzzle.add_between_line([(5, 5), (6, 5), (7, 6), (8, 7)])
    puzzle.add_between_line([(5, 7), (4, 6), (4, 5), (4, 4)])
    puzzle.add_between_line([(2, 6), (2, 7), (3, 8)])
    puzzle.add_between_line([(7, 5), (8, 5), (8, 4)])
    puzzle.add_between_line([(0, 4), (1, 4), (1, 5)])

    return puzzle
