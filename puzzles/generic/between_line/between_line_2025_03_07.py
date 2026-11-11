"""PuzzleMadness Between Lines Sudoku — 2025-03-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-03-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/3/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 2],
        [1, 0, 0, 0, 8, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 1, 3, 0],
        [5, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 1, 0, 7, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(4, 5), (5, 5), (6, 6), (7, 5), (7, 4), (7, 3)])
    puzzle.add_between_line([(6, 7), (7, 6), (8, 6), (7, 7), (8, 7)])
    puzzle.add_between_line([(4, 3), (3, 3), (3, 2), (2, 2), (2, 1)])
    puzzle.add_between_line([(7, 0), (6, 1), (5, 1), (4, 0), (3, 1)])
    puzzle.add_between_line([(1, 5), (2, 5), (3, 4), (2, 4), (2, 3)])
    puzzle.add_between_line([(4, 2), (5, 3), (6, 2), (7, 1)])
    puzzle.add_between_line([(1, 6), (2, 7), (1, 8), (0, 8)])
    puzzle.add_between_line([(5, 7), (4, 6), (3, 6), (3, 7)])
    puzzle.add_between_line([(2, 0), (1, 1), (0, 1), (1, 0)])
    puzzle.add_between_line([(0, 4), (0, 3), (1, 2)])
    puzzle.add_between_line([(2, 8), (3, 8), (4, 8)])
    puzzle.add_between_line([(0, 7), (1, 7), (0, 6)])
    puzzle.add_between_line([(7, 2), (8, 1), (8, 2)])

    return puzzle
