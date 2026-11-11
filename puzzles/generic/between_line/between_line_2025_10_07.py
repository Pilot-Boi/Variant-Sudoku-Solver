"""PuzzleMadness Between Lines Sudoku — 2025-10-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-10-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/10/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 6, 0, 0, 8],
        [0, 0, 0, 3, 0, 0, 5, 9, 2],
        [0, 2, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(8, 2), (7, 1), (7, 0), (6, 0), (5, 1), (6, 1)])
    puzzle.add_between_line([(2, 1), (2, 2), (3, 2), (2, 3), (3, 3)])
    puzzle.add_between_line([(1, 0), (0, 1), (1, 1), (1, 2), (1, 3)])
    puzzle.add_between_line([(4, 2), (5, 3), (6, 4), (7, 4), (8, 3)])
    puzzle.add_between_line([(2, 5), (2, 6), (3, 7), (4, 7), (5, 7)])
    puzzle.add_between_line([(7, 7), (7, 6), (6, 5), (7, 5)])
    puzzle.add_between_line([(3, 1), (2, 0), (3, 0), (4, 0)])
    puzzle.add_between_line([(8, 4), (8, 5), (8, 6), (8, 7)])
    puzzle.add_between_line([(4, 4), (4, 3), (3, 4)])
    puzzle.add_between_line([(2, 8), (3, 8), (2, 7)])
    puzzle.add_between_line([(5, 2), (6, 2), (6, 3)])

    return puzzle
