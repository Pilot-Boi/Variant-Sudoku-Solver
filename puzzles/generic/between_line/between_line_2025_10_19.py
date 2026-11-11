"""PuzzleMadness Between Lines Sudoku — 2025-10-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-10-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/10/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 5, 0, 0],
        [0, 3, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 2, 7, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 1, 7, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(4, 4), (5, 3), (6, 3), (7, 2), (8, 3), (8, 2)])
    puzzle.add_between_line([(3, 0), (4, 1), (3, 2), (2, 3), (1, 2)])
    puzzle.add_between_line([(3, 6), (4, 7), (3, 8), (2, 7), (2, 8)])
    puzzle.add_between_line([(1, 3), (0, 3), (0, 4), (0, 5), (1, 4)])
    puzzle.add_between_line([(8, 6), (7, 7), (6, 8), (7, 8)])
    puzzle.add_between_line([(8, 4), (8, 5), (7, 4), (7, 5)])
    puzzle.add_between_line([(4, 8), (5, 8), (6, 7), (5, 6)])
    puzzle.add_between_line([(1, 7), (1, 8), (0, 7), (0, 6)])
    puzzle.add_between_line([(3, 3), (3, 4), (4, 3)])
    puzzle.add_between_line([(2, 5), (1, 6), (1, 5)])
    puzzle.add_between_line([(6, 5), (7, 6), (6, 6)])

    return puzzle
