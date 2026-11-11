"""PuzzleMadness Between Lines Sudoku — 2025-12-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-12-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/12/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 5, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 2, 0, 0, 0],
        [0, 0, 3, 5, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 4, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 4, 0, 0, 0, 0, 8, 3],
        [9, 0, 0, 0, 0, 0, 0, 1, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(3, 8), (2, 7), (3, 7), (4, 8), (4, 7), (4, 6)])
    puzzle.add_between_line([(7, 1), (8, 2), (7, 3), (6, 4), (7, 5)])
    puzzle.add_between_line([(5, 8), (5, 7), (5, 6), (6, 5), (5, 5)])
    puzzle.add_between_line([(6, 7), (7, 8), (8, 8), (7, 7), (8, 7)])
    puzzle.add_between_line([(0, 3), (0, 2), (1, 1), (2, 2), (1, 3)])
    puzzle.add_between_line([(1, 4), (0, 5), (1, 5), (0, 6)])
    puzzle.add_between_line([(8, 4), (8, 5), (8, 6), (7, 6)])
    puzzle.add_between_line([(2, 6), (3, 6), (2, 5), (3, 5)])
    puzzle.add_between_line([(3, 0), (2, 0), (2, 1), (3, 1)])
    puzzle.add_between_line([(3, 3), (4, 3), (3, 4)])
    puzzle.add_between_line([(6, 0), (6, 1), (5, 2)])
    puzzle.add_between_line([(4, 1), (4, 2), (5, 1)])
    puzzle.add_between_line([(0, 1), (1, 0), (0, 0)])

    return puzzle
