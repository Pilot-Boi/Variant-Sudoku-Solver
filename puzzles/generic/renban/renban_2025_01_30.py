"""PuzzleMadness Renban Sudoku — 2025-01-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-01-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/1/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 3, 2, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 5, 0, 0, 0, 3, 0],
        [7, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 7, 4, 0, 6, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 7, 5, 0],
        [0, 0, 5, 0, 6, 0, 0, 2, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(6, 3), (6, 4), (6, 5), (5, 5), (4, 5)])
    puzzle.add_renban([(4, 2), (4, 1), (4, 0), (5, 0), (6, 0)])
    puzzle.add_renban([(5, 6), (6, 6), (7, 6), (7, 7), (7, 8)])
    puzzle.add_renban([(1, 2), (1, 1), (1, 0), (2, 0)])
    puzzle.add_renban([(5, 2), (4, 3), (3, 2), (2, 1)])
    puzzle.add_renban([(2, 8), (1, 8), (0, 8), (0, 7)])
    puzzle.add_renban([(3, 5), (4, 4), (5, 3)])
    puzzle.add_renban([(2, 2), (3, 3), (2, 4)])
    puzzle.add_renban([(0, 0), (0, 1), (0, 2)])
    puzzle.add_renban([(7, 4), (8, 4), (8, 5)])
    puzzle.add_renban([(8, 1), (8, 2)])
    puzzle.add_renban([(1, 6), (2, 5)])
    puzzle.add_renban([(3, 7), (4, 6)])
    puzzle.add_renban([(7, 1), (6, 1)])
    puzzle.add_renban([(0, 4), (0, 5)])

    return puzzle
