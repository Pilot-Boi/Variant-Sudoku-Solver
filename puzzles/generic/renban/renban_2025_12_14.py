"""PuzzleMadness Renban Sudoku — 2025-12-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-12-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/12/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 9, 0, 0, 6, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 9, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 9, 0, 2, 3, 0],
        [0, 0, 0, 0, 6, 1, 0, 0, 0],
        [0, 0, 0, 2, 8, 4, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 5],
        [4, 6, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 8, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(1, 6), (2, 6), (3, 6), (4, 6), (5, 6)])
    puzzle.add_renban([(3, 3), (3, 2), (3, 1), (4, 1), (5, 1)])
    puzzle.add_renban([(7, 0), (7, 1), (7, 2), (6, 2), (5, 2)])
    puzzle.add_renban([(8, 7), (8, 8), (7, 8), (6, 8)])
    puzzle.add_renban([(2, 3), (1, 3), (1, 2), (1, 1)])
    puzzle.add_renban([(8, 1), (8, 2), (8, 3), (7, 3)])
    puzzle.add_renban([(7, 5), (6, 6), (5, 5)])
    puzzle.add_renban([(4, 3), (5, 3), (6, 3)])
    puzzle.add_renban([(3, 8), (4, 8), (5, 8)])
    puzzle.add_renban([(4, 0), (5, 0), (6, 0)])
    puzzle.add_renban([(8, 6), (7, 6)])
    puzzle.add_renban([(1, 0), (2, 0)])
    puzzle.add_renban([(2, 5), (3, 5)])
    puzzle.add_renban([(8, 4), (8, 5)])
    puzzle.add_renban([(0, 7), (0, 6)])

    return puzzle
