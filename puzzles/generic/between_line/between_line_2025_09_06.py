"""PuzzleMadness Between Lines Sudoku — 2025-09-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-09-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/9/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 8, 0, 0, 0, 0, 4],
        [0, 0, 3, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 1, 0, 5, 0, 6, 0],
        [0, 0, 0, 4, 7, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [2, 8, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 1, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(3, 1), (2, 2), (1, 2), (2, 1), (3, 0), (4, 1)])
    puzzle.add_between_line([(7, 7), (7, 6), (8, 5), (8, 4), (7, 5)])
    puzzle.add_between_line([(6, 4), (7, 4), (6, 5), (5, 5), (4, 4)])
    puzzle.add_between_line([(6, 6), (6, 7), (7, 8), (8, 8), (8, 7)])
    puzzle.add_between_line([(3, 2), (4, 3), (3, 3), (2, 3)])
    puzzle.add_between_line([(5, 8), (6, 8), (5, 7), (4, 7)])
    puzzle.add_between_line([(8, 1), (7, 2), (8, 3), (8, 2)])
    puzzle.add_between_line([(6, 1), (7, 1), (6, 0), (7, 0)])
    puzzle.add_between_line([(1, 1), (0, 1), (0, 2)])
    puzzle.add_between_line([(0, 6), (1, 6), (2, 7)])
    puzzle.add_between_line([(5, 1), (4, 0), (5, 0)])

    return puzzle
