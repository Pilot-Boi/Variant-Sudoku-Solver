"""PuzzleMadness Between Lines Sudoku — 2025-04-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-04-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/4/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [2, 0, 0, 0, 5, 0, 0, 0, 0],
        [6, 0, 7, 0, 0, 2, 0, 0, 1],
        [0, 0, 4, 9, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 4, 0, 0, 8, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(1, 7), (1, 6), (2, 5), (1, 5), (0, 6), (0, 7)])
    puzzle.add_between_line([(8, 7), (8, 6), (8, 5), (8, 4), (7, 4)])
    puzzle.add_between_line([(3, 6), (4, 6), (5, 7), (4, 7), (4, 8)])
    puzzle.add_between_line([(4, 4), (4, 5), (3, 4), (3, 3), (2, 4)])
    puzzle.add_between_line([(2, 7), (3, 7), (3, 8), (2, 8), (1, 8)])
    puzzle.add_between_line([(2, 0), (3, 1), (4, 1), (3, 2)])
    puzzle.add_between_line([(1, 2), (2, 1), (2, 2), (1, 3)])
    puzzle.add_between_line([(4, 0), (5, 0), (5, 1), (4, 2)])
    puzzle.add_between_line([(8, 3), (7, 2), (6, 2), (7, 3)])
    puzzle.add_between_line([(6, 6), (7, 7), (7, 8)])
    puzzle.add_between_line([(0, 4), (0, 5), (1, 4)])
    puzzle.add_between_line([(6, 3), (6, 4), (5, 5)])

    return puzzle
