"""PuzzleMadness Between Lines Sudoku — 2025-04-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-04-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/4/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 2, 0, 0, 0, 0, 5, 0, 4],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 5, 0, 2, 0],
        [0, 0, 0, 3, 0, 0, 6, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 3],
        [3, 0, 0, 1, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(7, 5), (8, 4), (7, 4), (6, 3), (7, 2), (8, 3)])
    puzzle.add_between_line([(2, 5), (2, 4), (1, 4), (0, 4), (0, 3)])
    puzzle.add_between_line([(1, 3), (1, 2), (1, 1), (0, 1), (1, 0)])
    puzzle.add_between_line([(4, 4), (5, 3), (4, 3), (3, 3), (2, 3)])
    puzzle.add_between_line([(5, 4), (6, 4), (6, 5), (5, 6), (6, 7)])
    puzzle.add_between_line([(1, 5), (2, 6), (3, 7), (4, 8)])
    puzzle.add_between_line([(4, 7), (5, 7), (4, 6), (3, 6)])
    puzzle.add_between_line([(6, 1), (6, 0), (7, 0), (7, 1)])
    puzzle.add_between_line([(6, 2), (5, 1), (5, 0)])
    puzzle.add_between_line([(3, 4), (4, 5), (5, 5)])
    puzzle.add_between_line([(5, 2), (4, 1), (3, 1)])

    return puzzle
