"""PuzzleMadness Renban Sudoku — 2025-10-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-10-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/10/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 8, 0, 0, 4, 3, 0, 0, 5],
        [4, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 6, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 6, 0, 2],
        [0, 9, 0, 0, 1, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 1, 0, 0, 3, 8, 9, 0, 0],
        [0, 7, 0, 0, 0, 0, 1, 0, 4],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 4), (0, 5), (0, 6), (0, 7), (0, 8)])
    puzzle.add_renban([(8, 4), (7, 4), (6, 4), (6, 3), (6, 2)])
    puzzle.add_renban([(8, 6), (8, 7), (8, 8), (7, 8), (6, 8)])
    puzzle.add_renban([(4, 0), (5, 0), (5, 1), (5, 2)])
    puzzle.add_renban([(3, 4), (4, 3), (5, 4), (6, 5)])
    puzzle.add_renban([(3, 2), (2, 2), (2, 1), (2, 0)])
    puzzle.add_renban([(3, 7), (3, 6), (4, 6)])
    puzzle.add_renban([(7, 1), (7, 2), (7, 3)])
    puzzle.add_renban([(1, 4), (1, 5), (1, 6)])
    puzzle.add_renban([(1, 0), (1, 1), (1, 2)])
    puzzle.add_renban([(2, 7), (2, 6)])
    puzzle.add_renban([(1, 8), (2, 8)])
    puzzle.add_renban([(8, 0), (7, 0)])
    puzzle.add_renban([(4, 7), (5, 6)])
    puzzle.add_renban([(4, 2), (5, 3)])

    return puzzle
