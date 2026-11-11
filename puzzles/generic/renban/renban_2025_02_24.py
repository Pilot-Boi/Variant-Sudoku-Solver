"""PuzzleMadness Renban Sudoku — 2025-02-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-02-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/2/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 0, 0, 7, 0, 2, 0],
        [0, 7, 0, 0, 1, 0, 0, 0, 0],
        [0, 5, 9, 0, 0, 0, 4, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 7, 6, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 8],
        [0, 0, 0, 2, 0, 0, 7, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(1, 5), (2, 5), (3, 5), (4, 5), (5, 5)])
    puzzle.add_renban([(4, 2), (5, 2), (6, 2), (7, 2), (8, 2)])
    puzzle.add_renban([(4, 8), (3, 8), (2, 8), (2, 7), (2, 6)])
    puzzle.add_renban([(8, 5), (8, 6), (7, 6), (6, 6)])
    puzzle.add_renban([(4, 7), (5, 7), (6, 7), (7, 7)])
    puzzle.add_renban([(4, 4), (5, 4), (6, 4), (6, 5)])
    puzzle.add_renban([(1, 3), (0, 2), (1, 1)])
    puzzle.add_renban([(3, 1), (3, 2), (3, 3)])
    puzzle.add_renban([(4, 3), (3, 4), (2, 3)])
    puzzle.add_renban([(8, 0), (7, 0)])
    puzzle.add_renban([(3, 0), (4, 1)])
    puzzle.add_renban([(1, 8), (1, 7)])
    puzzle.add_renban([(4, 0), (5, 1)])
    puzzle.add_renban([(8, 3), (7, 4)])

    return puzzle
