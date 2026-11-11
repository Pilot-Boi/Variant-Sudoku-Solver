"""PuzzleMadness Renban Sudoku — 2025-09-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-09-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/9/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 4, 6, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [8, 0, 0, 5, 7, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 7],
        [0, 5, 0, 0, 0, 0, 9, 0, 0],
        [3, 0, 0, 0, 4, 0, 0, 8, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 4), (5, 3), (6, 2), (7, 1), (8, 0)])
    puzzle.add_renban([(3, 6), (2, 5), (1, 4), (2, 3), (3, 2)])
    puzzle.add_renban([(6, 5), (6, 4), (6, 3), (7, 3), (8, 3)])
    puzzle.add_renban([(3, 8), (4, 7), (5, 6), (6, 7)])
    puzzle.add_renban([(5, 4), (4, 5), (3, 4)])
    puzzle.add_renban([(1, 7), (1, 6), (2, 6)])
    puzzle.add_renban([(1, 3), (1, 2), (2, 2)])
    puzzle.add_renban([(0, 2), (0, 3), (0, 4)])
    puzzle.add_renban([(8, 5), (7, 5)])
    puzzle.add_renban([(3, 0), (3, 1)])
    puzzle.add_renban([(1, 8), (2, 7)])
    puzzle.add_renban([(2, 0), (2, 1)])
    puzzle.add_renban([(8, 4), (7, 4)])

    return puzzle
