"""PuzzleMadness Between Lines Sudoku — 2025-04-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-04-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/4/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 4],
        [6, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 8, 0, 5, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(8, 3), (7, 2), (6, 3), (5, 3), (6, 2), (7, 1)])
    puzzle.add_between_line([(6, 1), (5, 2), (4, 3), (3, 4), (2, 5)])
    puzzle.add_between_line([(4, 8), (3, 8), (3, 7), (4, 7), (3, 6)])
    puzzle.add_between_line([(3, 3), (2, 3), (1, 2), (2, 2), (1, 1)])
    puzzle.add_between_line([(1, 8), (1, 7), (0, 6), (1, 6), (0, 5)])
    puzzle.add_between_line([(6, 7), (6, 6), (5, 6), (5, 7)])
    puzzle.add_between_line([(4, 0), (5, 1), (4, 1), (3, 0)])
    puzzle.add_between_line([(2, 0), (2, 1), (1, 0), (0, 0)])
    puzzle.add_between_line([(6, 5), (7, 5), (8, 4)])
    puzzle.add_between_line([(5, 5), (4, 6), (4, 5)])
    puzzle.add_between_line([(7, 7), (7, 8), (8, 7)])
    puzzle.add_between_line([(1, 3), (2, 4), (1, 5)])

    return puzzle
