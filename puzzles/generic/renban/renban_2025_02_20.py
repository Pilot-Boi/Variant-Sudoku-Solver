"""PuzzleMadness Renban Sudoku — 2025-02-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-02-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/2/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 3, 0, 1, 0],
        [0, 6, 0, 0, 0, 0, 8, 0, 7],
        [9, 0, 0, 8, 5, 0, 0, 2, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 3, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 1, 2, 0, 0, 6, 0, 3, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [3, 0, 8, 0, 2, 0, 6, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(5, 4), (5, 3), (5, 2), (6, 2), (7, 2)])
    puzzle.add_renban([(1, 1), (2, 1), (3, 1), (4, 1), (5, 1)])
    puzzle.add_renban([(5, 5), (4, 6), (3, 7), (2, 6), (1, 5)])
    puzzle.add_renban([(8, 5), (8, 6), (8, 7), (7, 7)])
    puzzle.add_renban([(6, 3), (6, 4), (6, 5), (6, 6)])
    puzzle.add_renban([(2, 4), (1, 4), (1, 3), (1, 2)])
    puzzle.add_renban([(1, 8), (1, 7), (1, 6)])
    puzzle.add_renban([(8, 1), (8, 2), (8, 3)])
    puzzle.add_renban([(0, 1), (0, 2), (0, 3)])
    puzzle.add_renban([(3, 6), (3, 5), (4, 5)])
    puzzle.add_renban([(7, 4), (7, 5)])
    puzzle.add_renban([(5, 8), (5, 7)])
    puzzle.add_renban([(3, 2), (4, 3)])
    puzzle.add_renban([(8, 4), (7, 3)])
    puzzle.add_renban([(2, 0), (3, 0)])

    return puzzle
