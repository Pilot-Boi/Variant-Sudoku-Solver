"""PuzzleMadness Between Lines Sudoku — 2025-03-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-03-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/3/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 8],
        [0, 0, 4, 2, 0, 0, 0, 0, 0],
        [1, 6, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 4, 1, 0],
        [0, 0, 3, 0, 2, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(1, 7), (1, 8), (2, 8), (3, 7), (2, 6), (1, 6)])
    puzzle.add_between_line([(7, 8), (7, 7), (8, 6), (7, 5), (8, 5)])
    puzzle.add_between_line([(4, 4), (5, 5), (6, 4), (7, 4), (7, 3)])
    puzzle.add_between_line([(5, 0), (4, 1), (5, 2), (6, 2), (6, 1)])
    puzzle.add_between_line([(5, 4), (5, 3), (6, 3), (7, 2), (7, 1)])
    puzzle.add_between_line([(6, 0), (7, 0), (8, 1), (8, 2)])
    puzzle.add_between_line([(3, 2), (4, 2), (3, 1), (3, 0)])
    puzzle.add_between_line([(1, 3), (2, 3), (1, 4), (2, 5)])
    puzzle.add_between_line([(2, 1), (2, 0), (1, 0)])
    puzzle.add_between_line([(2, 2), (1, 2), (1, 1)])
    puzzle.add_between_line([(5, 7), (4, 6), (4, 7)])

    return puzzle
