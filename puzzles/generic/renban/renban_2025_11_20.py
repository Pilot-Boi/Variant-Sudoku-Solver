"""PuzzleMadness Renban Sudoku — 2025-11-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-11-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/11/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 1, 0, 2, 0, 0, 4, 5, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 9, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [3, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 7, 0],
        [0, 0, 0, 0, 0, 7, 0, 4, 0],
        [5, 0, 8, 0, 6, 0, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(3, 4), (4, 5), (5, 6), (4, 7), (3, 8)])
    puzzle.add_renban([(5, 2), (5, 1), (5, 0), (6, 0), (7, 0)])
    puzzle.add_renban([(7, 4), (7, 5), (7, 6), (7, 7), (7, 8)])
    puzzle.add_renban([(0, 5), (1, 4), (2, 3), (3, 2)])
    puzzle.add_renban([(0, 8), (0, 7), (0, 6), (1, 6)])
    puzzle.add_renban([(4, 4), (4, 3), (5, 3), (6, 3)])
    puzzle.add_renban([(6, 8), (5, 8), (5, 7)])
    puzzle.add_renban([(1, 0), (1, 1), (1, 2)])
    puzzle.add_renban([(2, 0), (3, 0), (3, 1)])
    puzzle.add_renban([(8, 1), (8, 2), (7, 2)])
    puzzle.add_renban([(1, 8), (2, 7)])
    puzzle.add_renban([(2, 1), (2, 2)])
    puzzle.add_renban([(7, 1), (6, 1)])
    puzzle.add_renban([(6, 5), (5, 4)])
    puzzle.add_renban([(2, 6), (3, 5)])

    return puzzle
