"""PuzzleMadness Renban Sudoku — 2025-11-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-11-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/11/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 6, 8, 0, 1, 0],
        [7, 3, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 1, 0, 0, 0, 2, 0, 7],
        [0, 0, 0, 0, 0, 5, 0, 4, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [4, 8, 0, 0, 0, 2, 3, 0, 0],
        [0, 4, 0, 9, 0, 0, 0, 0, 0],
        [2, 6, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 2), (2, 3), (2, 4), (2, 5), (2, 6)])
    puzzle.add_renban([(3, 6), (4, 5), (5, 4), (6, 5), (7, 6)])
    puzzle.add_renban([(6, 0), (6, 1), (6, 2), (5, 2), (4, 2)])
    puzzle.add_renban([(4, 3), (3, 2), (4, 1), (5, 0)])
    puzzle.add_renban([(0, 3), (0, 4), (0, 5), (0, 6)])
    puzzle.add_renban([(2, 8), (1, 8), (1, 7), (1, 6)])
    puzzle.add_renban([(0, 0), (1, 0), (2, 0)])
    puzzle.add_renban([(7, 3), (7, 4), (6, 4)])
    puzzle.add_renban([(3, 8), (4, 7), (5, 6)])
    puzzle.add_renban([(1, 3), (0, 2), (1, 1)])
    puzzle.add_renban([(8, 0), (7, 0)])
    puzzle.add_renban([(6, 8), (6, 7)])
    puzzle.add_renban([(8, 8), (7, 7)])
    puzzle.add_renban([(8, 4), (7, 5)])
    puzzle.add_renban([(4, 8), (5, 7)])

    return puzzle
