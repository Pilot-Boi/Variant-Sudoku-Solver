"""PuzzleMadness Between Lines Sudoku — 2025-10-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-10-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/10/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 4],
        [1, 0, 0, 3, 0, 0, 6, 0, 0],
        [3, 7, 0, 0, 8, 6, 0, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(8, 6), (7, 5), (7, 6), (6, 6), (5, 6), (4, 5)])
    puzzle.add_between_line([(6, 5), (6, 4), (5, 4), (5, 3), (6, 2)])
    puzzle.add_between_line([(2, 4), (1, 3), (0, 4), (0, 3), (0, 2)])
    puzzle.add_between_line([(7, 1), (7, 2), (7, 3), (8, 2), (8, 1)])
    puzzle.add_between_line([(3, 2), (2, 1), (1, 0), (1, 1)])
    puzzle.add_between_line([(1, 4), (2, 5), (1, 5), (0, 5)])
    puzzle.add_between_line([(3, 8), (4, 7), (3, 7), (2, 6)])
    puzzle.add_between_line([(7, 8), (8, 8), (8, 7)])
    puzzle.add_between_line([(6, 0), (5, 1), (5, 0)])
    puzzle.add_between_line([(0, 8), (0, 7), (1, 7)])
    puzzle.add_between_line([(0, 1), (1, 2), (2, 2)])

    return puzzle
