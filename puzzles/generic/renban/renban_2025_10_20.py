"""PuzzleMadness Renban Sudoku — 2025-10-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-10-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/10/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 0, 0, 0, 2, 0, 3, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 6, 0, 7, 0, 0, 0, 0, 0],
        [3, 0, 9, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 5, 0, 2, 0, 0],
        [0, 0, 1, 0, 0, 3, 0, 0, 7],
        [0, 0, 0, 0, 2, 0, 0, 5, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 4), (5, 3), (6, 2), (7, 1), (8, 0)])
    puzzle.add_renban([(2, 4), (2, 5), (2, 6), (1, 6), (0, 6)])
    puzzle.add_renban([(1, 0), (1, 1), (1, 2), (1, 3), (1, 4)])
    puzzle.add_renban([(3, 0), (4, 0), (4, 1), (4, 2)])
    puzzle.add_renban([(5, 8), (4, 8), (3, 8), (3, 7)])
    puzzle.add_renban([(8, 8), (7, 7), (6, 6), (7, 5)])
    puzzle.add_renban([(4, 6), (5, 6), (5, 7)])
    puzzle.add_renban([(5, 0), (5, 1), (5, 2)])
    puzzle.add_renban([(8, 5), (8, 6), (7, 6)])
    puzzle.add_renban([(3, 4), (3, 5)])
    puzzle.add_renban([(1, 8), (1, 7)])
    puzzle.add_renban([(3, 1), (3, 2)])
    puzzle.add_renban([(7, 3), (6, 3)])
    puzzle.add_renban([(7, 4), (6, 4)])

    return puzzle
