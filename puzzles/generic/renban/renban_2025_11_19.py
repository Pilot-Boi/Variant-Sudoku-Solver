"""PuzzleMadness Renban Sudoku — 2025-11-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-11-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/11/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 5, 2, 0, 0],
        [3, 0, 0, 0, 0, 0, 9, 0, 0],
        [5, 0, 0, 0, 3, 0, 0, 0, 7],
        [7, 8, 1, 2, 0, 0, 0, 3, 0],
        [6, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 6, 0, 0, 0, 7, 1],
        [0, 0, 0, 0, 1, 7, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(5, 1), (5, 2), (5, 3), (5, 4), (5, 5)])
    puzzle.add_renban([(4, 6), (3, 6), (2, 6), (2, 5), (2, 4)])
    puzzle.add_renban([(5, 6), (6, 6), (7, 6), (7, 7), (7, 8)])
    puzzle.add_renban([(7, 2), (8, 2), (8, 3), (8, 4)])
    puzzle.add_renban([(0, 2), (0, 3), (0, 4), (0, 5)])
    puzzle.add_renban([(3, 8), (2, 8), (1, 8), (1, 7)])
    puzzle.add_renban([(1, 0), (2, 1), (3, 2)])
    puzzle.add_renban([(2, 2), (1, 2), (1, 1)])
    puzzle.add_renban([(3, 1), (3, 0), (4, 0)])
    puzzle.add_renban([(7, 5), (6, 4), (7, 3)])
    puzzle.add_renban([(8, 5), (7, 4)])
    puzzle.add_renban([(4, 8), (3, 7)])
    puzzle.add_renban([(3, 4), (4, 3)])
    puzzle.add_renban([(1, 6), (1, 5)])
    puzzle.add_renban([(5, 0), (4, 1)])

    return puzzle
