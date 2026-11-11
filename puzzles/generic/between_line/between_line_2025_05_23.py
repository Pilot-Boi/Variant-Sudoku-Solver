"""PuzzleMadness Between Lines Sudoku — 2025-05-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-05-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/5/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 6, 0, 0, 0, 2],
        [0, 0, 7, 0, 0, 0, 6, 0, 0],
        [0, 4, 0, 0, 0, 0, 7, 0, 5],
        [7, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 9, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 9, 0, 0, 2, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [5, 7, 0, 0, 0, 1, 0, 0, 0],
        [1, 3, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(7, 5), (7, 4), (6, 3), (5, 2), (6, 2), (7, 2)])
    puzzle.add_between_line([(5, 5), (4, 5), (3, 4), (4, 4), (5, 4)])
    puzzle.add_between_line([(4, 1), (5, 0), (4, 0), (3, 0), (2, 0)])
    puzzle.add_between_line([(3, 1), (2, 2), (1, 2), (1, 3), (0, 2)])
    puzzle.add_between_line([(2, 7), (3, 6), (3, 5), (2, 4)])
    puzzle.add_between_line([(3, 2), (4, 3), (4, 2), (5, 1)])
    puzzle.add_between_line([(4, 7), (5, 8), (4, 8), (3, 7)])
    puzzle.add_between_line([(6, 5), (7, 6), (7, 7)])
    puzzle.add_between_line([(7, 0), (8, 1), (8, 2)])
    puzzle.add_between_line([(6, 6), (5, 7), (4, 6)])
    puzzle.add_between_line([(0, 0), (0, 1), (1, 1)])

    return puzzle
