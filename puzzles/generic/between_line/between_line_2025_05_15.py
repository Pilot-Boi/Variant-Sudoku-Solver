"""PuzzleMadness Between Lines Sudoku — 2025-05-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-05-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/5/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 5, 0, 0, 0, 0, 0, 7, 0],
        [8, 0, 0, 0, 0, 0, 5, 0, 6],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [2, 0, 8, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 9, 4, 0, 0, 0, 1],
        [0, 0, 0, 0, 6, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 5), (3, 5), (4, 4), (5, 4), (4, 3), (5, 3)])
    puzzle.add_between_line([(4, 2), (3, 1), (3, 0), (4, 0), (5, 0)])
    puzzle.add_between_line([(4, 7), (5, 7), (6, 7), (5, 8), (6, 8)])
    puzzle.add_between_line([(7, 6), (8, 5), (7, 4), (6, 4), (7, 5)])
    puzzle.add_between_line([(3, 3), (2, 2), (2, 3), (1, 3), (0, 4)])
    puzzle.add_between_line([(2, 6), (1, 7), (1, 8), (0, 7)])
    puzzle.add_between_line([(0, 6), (0, 5), (1, 5), (1, 4)])
    puzzle.add_between_line([(8, 7), (8, 8), (7, 8), (7, 7)])
    puzzle.add_between_line([(3, 6), (4, 6), (5, 6), (4, 5)])
    puzzle.add_between_line([(6, 1), (7, 2), (8, 2)])
    puzzle.add_between_line([(8, 1), (8, 0), (7, 0)])
    puzzle.add_between_line([(5, 1), (5, 2), (6, 2)])

    return puzzle
