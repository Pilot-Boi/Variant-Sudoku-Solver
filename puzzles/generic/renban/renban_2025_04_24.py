"""PuzzleMadness Renban Sudoku — 2025-04-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-04-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/4/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 8, 0],
        [3, 0, 5, 9, 0, 0, 0, 1, 7],
        [0, 0, 2, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 4, 1, 0, 5],
        [0, 0, 0, 2, 6, 0, 0, 0, 0],
        [0, 8, 1, 6, 0, 3, 2, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 5, 0],
        [6, 0, 0, 5, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 8), (0, 7), (0, 6), (1, 6), (2, 6)])
    puzzle.add_renban([(7, 5), (7, 6), (7, 7), (6, 7), (5, 7)])
    puzzle.add_renban([(2, 4), (3, 4), (4, 4), (5, 4), (6, 4)])
    puzzle.add_renban([(3, 1), (4, 1), (5, 1), (6, 1)])
    puzzle.add_renban([(3, 8), (4, 8), (5, 8), (6, 8)])
    puzzle.add_renban([(3, 2), (4, 2), (5, 2), (6, 2)])
    puzzle.add_renban([(2, 1), (2, 0), (3, 0)])
    puzzle.add_renban([(1, 3), (2, 2), (3, 3)])
    puzzle.add_renban([(8, 3), (7, 4), (6, 5)])
    puzzle.add_renban([(2, 8), (1, 8), (1, 7)])
    puzzle.add_renban([(4, 0), (5, 0)])
    puzzle.add_renban([(1, 5), (2, 5)])
    puzzle.add_renban([(8, 1), (7, 1)])
    puzzle.add_renban([(0, 3), (1, 4)])
    puzzle.add_renban([(4, 7), (4, 6)])

    return puzzle
