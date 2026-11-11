"""PuzzleMadness Between Lines Sudoku — 2025-05-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-05-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/5/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 9, 0, 0, 0, 0, 0, 8],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 8, 0, 4, 0, 0],
        [1, 0, 0, 6, 0, 0, 0, 0, 2],
        [0, 3, 0, 0, 0, 0, 8, 7, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 9, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(4, 7), (4, 6), (3, 5), (4, 4), (5, 3), (5, 4)])
    puzzle.add_between_line([(3, 0), (2, 0), (1, 0), (1, 1), (0, 2)])
    puzzle.add_between_line([(5, 1), (4, 2), (5, 2), (4, 3), (3, 3)])
    puzzle.add_between_line([(6, 5), (7, 4), (8, 3), (8, 2), (7, 1)])
    puzzle.add_between_line([(7, 0), (6, 0), (6, 1), (7, 2)])
    puzzle.add_between_line([(7, 6), (6, 6), (5, 7), (5, 6)])
    puzzle.add_between_line([(3, 2), (2, 3), (2, 4), (1, 4)])
    puzzle.add_between_line([(0, 5), (1, 5), (0, 6), (1, 6)])
    puzzle.add_between_line([(6, 4), (7, 3), (6, 2)])
    puzzle.add_between_line([(2, 6), (3, 7), (2, 8)])
    puzzle.add_between_line([(1, 7), (0, 7), (0, 8)])

    return puzzle
