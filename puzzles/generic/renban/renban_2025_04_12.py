"""PuzzleMadness Renban Sudoku — 2025-04-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-04-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/4/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 4, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 5, 0],
        [7, 2, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [9, 0, 0, 0, 1, 3, 0, 0, 6],
        [0, 1, 0, 0, 0, 9, 0, 4, 7],
        [0, 0, 0, 6, 0, 0, 9, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [5, 0, 0, 0, 3, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(8, 0), (8, 1), (8, 2), (7, 2), (6, 2)])
    puzzle.add_renban([(5, 2), (4, 2), (3, 2), (3, 1), (3, 0)])
    puzzle.add_renban([(2, 3), (3, 3), (4, 3), (5, 3), (6, 3)])
    puzzle.add_renban([(4, 7), (5, 7), (6, 7), (7, 7)])
    puzzle.add_renban([(4, 8), (5, 8), (6, 8), (7, 8)])
    puzzle.add_renban([(6, 4), (7, 4), (7, 5), (7, 6)])
    puzzle.add_renban([(3, 5), (4, 6), (3, 7)])
    puzzle.add_renban([(2, 8), (1, 8), (1, 7)])
    puzzle.add_renban([(6, 0), (7, 0), (7, 1)])
    puzzle.add_renban([(1, 6), (2, 5), (3, 4)])
    puzzle.add_renban([(0, 0), (1, 0)])
    puzzle.add_renban([(4, 0), (5, 0)])
    puzzle.add_renban([(0, 4), (0, 5)])
    puzzle.add_renban([(0, 1), (1, 1)])
    puzzle.add_renban([(0, 6), (1, 5)])

    return puzzle
