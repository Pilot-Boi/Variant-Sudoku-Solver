"""PuzzleMadness Between Lines Sudoku — 2025-12-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-12-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/12/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 8, 1, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 4, 0, 1],
        [7, 0, 0, 6, 5, 0, 0, 8, 0],
        [0, 0, 0, 2, 0, 0, 6, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(3, 0), (4, 1), (5, 2), (6, 3), (7, 3), (7, 2)])
    puzzle.add_between_line([(8, 3), (7, 4), (8, 4), (8, 5), (7, 5)])
    puzzle.add_between_line([(8, 7), (7, 8), (6, 8), (5, 7), (6, 7)])
    puzzle.add_between_line([(2, 7), (2, 8), (1, 7), (2, 6), (2, 5)])
    puzzle.add_between_line([(4, 2), (3, 2), (3, 1), (2, 2), (1, 2)])
    puzzle.add_between_line([(5, 0), (5, 1), (6, 2), (7, 1)])
    puzzle.add_between_line([(1, 0), (0, 0), (1, 1), (2, 1)])
    puzzle.add_between_line([(4, 6), (5, 5), (6, 5), (6, 4)])
    puzzle.add_between_line([(1, 6), (1, 5), (2, 4), (3, 4)])
    puzzle.add_between_line([(0, 4), (1, 4), (0, 3)])
    puzzle.add_between_line([(5, 4), (4, 5), (3, 5)])
    puzzle.add_between_line([(7, 7), (8, 6), (7, 6)])
    puzzle.add_between_line([(5, 3), (4, 4), (3, 3)])

    return puzzle
