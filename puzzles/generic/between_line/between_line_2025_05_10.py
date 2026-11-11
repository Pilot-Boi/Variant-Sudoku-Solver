"""PuzzleMadness Between Lines Sudoku — 2025-05-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-05-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/5/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 2, 7, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 3, 9, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(4, 7), (3, 7), (3, 8), (4, 8), (5, 7), (6, 8)])
    puzzle.add_between_line([(0, 8), (1, 7), (2, 6), (3, 5), (2, 5)])
    puzzle.add_between_line([(6, 4), (6, 5), (5, 4), (4, 3), (5, 3)])
    puzzle.add_between_line([(3, 3), (2, 2), (3, 2), (3, 1), (3, 0)])
    puzzle.add_between_line([(1, 0), (0, 1), (1, 1), (2, 1), (2, 0)])
    puzzle.add_between_line([(8, 6), (8, 7), (7, 8), (8, 8)])
    puzzle.add_between_line([(1, 4), (2, 3), (2, 4), (3, 4)])
    puzzle.add_between_line([(8, 3), (8, 4), (7, 3), (8, 2)])
    puzzle.add_between_line([(6, 1), (7, 1), (7, 0), (8, 0)])
    puzzle.add_between_line([(0, 3), (0, 2), (1, 2)])
    puzzle.add_between_line([(4, 6), (4, 5), (5, 5)])
    puzzle.add_between_line([(5, 6), (6, 6), (7, 6)])
    puzzle.add_between_line([(0, 6), (1, 6), (0, 5)])

    return puzzle
