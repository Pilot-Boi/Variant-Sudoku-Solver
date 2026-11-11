"""PuzzleMadness Renban Sudoku — 2025-10-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-10-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/10/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [8, 0, 0, 1, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 5],
        [0, 0, 8, 0, 0, 5, 6, 0, 0],
        [0, 7, 5, 9, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 5, 0, 0],
        [4, 9, 0, 0, 0, 0, 0, 2, 8],
        [0, 0, 0, 0, 0, 0, 4, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 1), (1, 1), (2, 1), (2, 2), (2, 3)])
    puzzle.add_renban([(8, 2), (7, 3), (6, 4), (5, 3), (4, 2)])
    puzzle.add_renban([(3, 8), (2, 8), (1, 8), (1, 7), (1, 6)])
    puzzle.add_renban([(2, 4), (3, 4), (3, 5), (3, 6)])
    puzzle.add_renban([(8, 5), (8, 6), (7, 6), (6, 6)])
    puzzle.add_renban([(7, 8), (6, 8), (5, 8), (5, 7)])
    puzzle.add_renban([(0, 8), (0, 7), (0, 6)])
    puzzle.add_renban([(4, 4), (4, 5), (4, 6)])
    puzzle.add_renban([(4, 3), (3, 2), (4, 1)])
    puzzle.add_renban([(6, 3), (6, 2), (7, 2)])
    puzzle.add_renban([(8, 0), (7, 0)])
    puzzle.add_renban([(8, 7), (7, 7)])
    puzzle.add_renban([(0, 3), (1, 4)])
    puzzle.add_renban([(7, 5), (6, 5)])
    puzzle.add_renban([(5, 6), (5, 5)])

    return puzzle
