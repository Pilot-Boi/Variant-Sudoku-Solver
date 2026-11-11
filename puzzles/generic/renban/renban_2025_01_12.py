"""PuzzleMadness Renban Sudoku — 2025-01-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-01-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/1/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 7, 0, 0, 0, 0, 0, 0, 0],
        [4, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 4],
        [0, 0, 0, 1, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [5, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 3, 0, 0, 9, 6],
        [0, 3, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 7, 0, 1, 0, 0, 2, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 4), (1, 4), (2, 4), (2, 5), (2, 6)])
    puzzle.add_renban([(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)])
    puzzle.add_renban([(3, 5), (4, 4), (5, 3), (6, 2), (7, 1)])
    puzzle.add_renban([(6, 7), (5, 7), (5, 6), (5, 5)])
    puzzle.add_renban([(7, 6), (6, 6), (6, 5), (6, 4)])
    puzzle.add_renban([(3, 6), (3, 7), (3, 8), (2, 8)])
    puzzle.add_renban([(7, 7), (7, 8), (6, 8)])
    puzzle.add_renban([(2, 3), (3, 3), (4, 3)])
    puzzle.add_renban([(5, 2), (5, 1), (6, 1)])
    puzzle.add_renban([(0, 0), (1, 0), (2, 0)])
    puzzle.add_renban([(7, 0), (6, 0)])
    puzzle.add_renban([(7, 3), (6, 3)])
    puzzle.add_renban([(0, 8), (1, 7)])
    puzzle.add_renban([(8, 7), (8, 6)])
    puzzle.add_renban([(0, 2), (1, 3)])

    return puzzle
