"""PuzzleMadness Renban Sudoku — 2025-01-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-01-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/1/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 7, 0, 0, 0, 0, 0, 6],
        [0, 0, 4, 0, 0, 6, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 4, 0, 7],
        [0, 0, 9, 0, 4, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 5, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 8],
        [3, 0, 2, 0, 0, 1, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(3, 0), (4, 0), (5, 0), (5, 1), (5, 2)])
    puzzle.add_renban([(6, 0), (7, 0), (8, 0), (8, 1), (8, 2)])
    puzzle.add_renban([(0, 3), (0, 4), (0, 5), (0, 6), (0, 7)])
    puzzle.add_renban([(6, 5), (5, 6), (4, 7), (3, 6)])
    puzzle.add_renban([(7, 3), (6, 4), (5, 3), (4, 2)])
    puzzle.add_renban([(2, 7), (2, 8), (1, 8), (0, 8)])
    puzzle.add_renban([(2, 3), (3, 4), (4, 5)])
    puzzle.add_renban([(8, 8), (7, 7), (6, 6)])
    puzzle.add_renban([(1, 1), (1, 0), (2, 0)])
    puzzle.add_renban([(2, 1), (2, 2), (1, 2)])
    puzzle.add_renban([(3, 3), (4, 3)])
    puzzle.add_renban([(0, 0), (0, 1)])
    puzzle.add_renban([(1, 3), (1, 4)])
    puzzle.add_renban([(2, 5), (3, 5)])
    puzzle.add_renban([(4, 6), (5, 5)])

    return puzzle
