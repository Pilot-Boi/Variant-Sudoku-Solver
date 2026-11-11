"""PuzzleMadness Renban Sudoku — 2025-11-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-11-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/11/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 8, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 3, 0, 0, 0, 5, 8],
        [5, 2, 0, 9, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 2, 5],
        [0, 0, 4, 0, 8, 9, 0, 0, 2],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 7, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 6), (3, 6), (4, 6), (5, 6), (6, 6)])
    puzzle.add_renban([(3, 5), (4, 4), (5, 3), (6, 2), (7, 1)])
    puzzle.add_renban([(1, 2), (2, 2), (3, 2), (4, 2), (5, 2)])
    puzzle.add_renban([(8, 8), (7, 8), (6, 8), (6, 7)])
    puzzle.add_renban([(7, 3), (8, 3), (8, 4), (8, 5)])
    puzzle.add_renban([(6, 1), (6, 0), (7, 0), (8, 0)])
    puzzle.add_renban([(7, 6), (8, 6), (8, 7)])
    puzzle.add_renban([(4, 7), (4, 8), (3, 8)])
    puzzle.add_renban([(8, 1), (8, 2), (7, 2)])
    puzzle.add_renban([(0, 0), (0, 1), (0, 2)])
    puzzle.add_renban([(1, 0), (2, 1)])
    puzzle.add_renban([(2, 3), (3, 4)])
    puzzle.add_renban([(0, 4), (1, 5)])
    puzzle.add_renban([(6, 4), (6, 5)])
    puzzle.add_renban([(4, 0), (3, 1)])

    return puzzle
