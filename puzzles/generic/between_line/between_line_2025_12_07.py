"""PuzzleMadness Between Lines Sudoku — 2025-12-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-12-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/12/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 5, 4, 0, 0, 0, 0, 0, 0],
        [8, 0, 3, 6, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(6, 1), (6, 0), (7, 0), (8, 1), (7, 2), (7, 1)])
    puzzle.add_between_line([(8, 6), (7, 5), (6, 4), (5, 5), (4, 5)])
    puzzle.add_between_line([(7, 3), (6, 2), (5, 3), (5, 4), (6, 3)])
    puzzle.add_between_line([(4, 6), (5, 6), (6, 5), (6, 6), (5, 7)])
    puzzle.add_between_line([(1, 1), (1, 0), (2, 1), (1, 2)])
    puzzle.add_between_line([(1, 6), (0, 5), (0, 4), (1, 5)])
    puzzle.add_between_line([(4, 1), (3, 1), (2, 2), (1, 3)])
    puzzle.add_between_line([(0, 8), (1, 8), (1, 7), (2, 6)])
    puzzle.add_between_line([(8, 7), (7, 6), (7, 7)])
    puzzle.add_between_line([(1, 4), (2, 4), (2, 3)])
    puzzle.add_between_line([(4, 8), (4, 7), (3, 6)])
    puzzle.add_between_line([(0, 3), (0, 2), (0, 1)])

    return puzzle
