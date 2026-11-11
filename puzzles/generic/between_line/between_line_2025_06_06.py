"""PuzzleMadness Between Lines Sudoku — 2025-06-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-06-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/6/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 8, 0, 5, 0, 0, 0, 0, 0],
        [6, 1, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 5, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 3, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(5, 7), (4, 7), (3, 6), (2, 5), (1, 5), (0, 4)])
    puzzle.add_between_line([(6, 0), (6, 1), (6, 2), (5, 1), (5, 2)])
    puzzle.add_between_line([(0, 7), (1, 8), (2, 8), (3, 7), (2, 7)])
    puzzle.add_between_line([(8, 5), (7, 6), (6, 5), (5, 6), (6, 7)])
    puzzle.add_between_line([(2, 1), (1, 1), (1, 2), (2, 3)])
    puzzle.add_between_line([(3, 4), (4, 5), (5, 5), (5, 4)])
    puzzle.add_between_line([(7, 1), (8, 1), (8, 0), (7, 0)])
    puzzle.add_between_line([(2, 0), (3, 1), (4, 0), (3, 0)])
    puzzle.add_between_line([(5, 8), (4, 8), (3, 8)])
    puzzle.add_between_line([(2, 2), (3, 2), (4, 1)])
    puzzle.add_between_line([(4, 4), (4, 3), (4, 2)])

    return puzzle
