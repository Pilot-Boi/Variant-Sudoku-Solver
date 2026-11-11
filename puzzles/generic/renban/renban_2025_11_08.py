"""PuzzleMadness Renban Sudoku — 2025-11-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-11-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/11/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 3, 0, 0, 0, 0, 0, 4, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 7, 0, 8, 0, 0, 0],
        [0, 6, 5, 0, 0, 3, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 1],
        [3, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 7, 0, 0, 5, 0, 0, 9, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)])
    puzzle.add_renban([(4, 0), (5, 0), (6, 0), (7, 0), (8, 0)])
    puzzle.add_renban([(4, 5), (5, 5), (6, 5), (6, 6), (6, 7)])
    puzzle.add_renban([(4, 3), (5, 3), (6, 3), (6, 4)])
    puzzle.add_renban([(1, 6), (1, 5), (1, 4), (2, 4)])
    puzzle.add_renban([(8, 2), (7, 2), (6, 2), (5, 2)])
    puzzle.add_renban([(0, 7), (1, 7), (2, 7)])
    puzzle.add_renban([(1, 1), (2, 1), (3, 1)])
    puzzle.add_renban([(8, 5), (8, 6), (7, 6)])
    puzzle.add_renban([(3, 4), (4, 4), (5, 4)])
    puzzle.add_renban([(0, 3), (1, 3)])
    puzzle.add_renban([(5, 7), (5, 6)])
    puzzle.add_renban([(4, 1), (5, 1)])
    puzzle.add_renban([(4, 8), (4, 7)])
    puzzle.add_renban([(8, 1), (7, 1)])

    return puzzle
