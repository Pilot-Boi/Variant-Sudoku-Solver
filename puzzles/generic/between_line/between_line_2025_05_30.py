"""PuzzleMadness Between Lines Sudoku — 2025-05-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-05-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/5/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 4, 0, 0, 5, 7, 8, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [5, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 7, 0],
        [0, 0, 0, 0, 0, 2, 0, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(6, 2), (6, 1), (6, 0), (7, 0), (8, 0), (8, 1)])
    puzzle.add_between_line([(8, 4), (8, 5), (7, 6), (7, 7), (6, 7)])
    puzzle.add_between_line([(6, 3), (6, 4), (5, 5), (6, 5), (6, 6)])
    puzzle.add_between_line([(3, 6), (4, 5), (5, 6), (5, 7), (4, 6)])
    puzzle.add_between_line([(7, 1), (8, 2), (7, 2), (7, 3)])
    puzzle.add_between_line([(5, 0), (4, 1), (3, 1), (2, 2)])
    puzzle.add_between_line([(0, 5), (1, 4), (2, 3), (3, 3)])
    puzzle.add_between_line([(5, 2), (4, 3), (5, 3)])
    puzzle.add_between_line([(1, 2), (0, 2), (0, 1)])
    puzzle.add_between_line([(4, 7), (3, 7), (2, 6)])

    return puzzle
