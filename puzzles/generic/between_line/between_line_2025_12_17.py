"""PuzzleMadness Between Lines Sudoku — 2025-12-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-12-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/12/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 1, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 6],
        [0, 0, 0, 0, 4, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(0, 6), (0, 5), (1, 6), (2, 7), (2, 8), (1, 7)])
    puzzle.add_between_line([(2, 5), (3, 6), (4, 7), (5, 7), (4, 6)])
    puzzle.add_between_line([(2, 3), (1, 4), (1, 3), (2, 2), (2, 1)])
    puzzle.add_between_line([(3, 8), (4, 8), (5, 8), (6, 7), (6, 8)])
    puzzle.add_between_line([(4, 3), (4, 2), (5, 3), (6, 2), (5, 1)])
    puzzle.add_between_line([(7, 7), (6, 6), (5, 6), (4, 5)])
    puzzle.add_between_line([(3, 0), (4, 1), (4, 0), (5, 0)])
    puzzle.add_between_line([(7, 4), (8, 3), (7, 2), (6, 3)])
    puzzle.add_between_line([(7, 3), (6, 4), (5, 5), (6, 5)])
    puzzle.add_between_line([(3, 2), (3, 3), (3, 4)])
    puzzle.add_between_line([(6, 1), (7, 1), (7, 0)])
    puzzle.add_between_line([(7, 8), (8, 7), (8, 6)])
    puzzle.add_between_line([(7, 6), (8, 5), (7, 5)])

    return puzzle
