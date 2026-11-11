"""PuzzleMadness Renban Sudoku — 2025-11-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-11-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/11/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 1],
        [0, 0, 4, 0, 0, 0, 0, 0, 2],
        [0, 0, 1, 7, 0, 0, 4, 9, 0],
        [0, 0, 0, 8, 3, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [9, 2, 0, 5, 0, 0, 0, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 3), (2, 4), (2, 5), (2, 6), (2, 7)])
    puzzle.add_renban([(4, 1), (5, 1), (6, 1), (7, 1), (8, 1)])
    puzzle.add_renban([(4, 3), (5, 3), (6, 3), (7, 3), (8, 3)])
    puzzle.add_renban([(5, 4), (5, 5), (4, 5), (3, 5)])
    puzzle.add_renban([(1, 2), (0, 2), (0, 1), (0, 0)])
    puzzle.add_renban([(3, 8), (2, 8), (1, 8), (1, 7)])
    puzzle.add_renban([(3, 7), (4, 6), (5, 7)])
    puzzle.add_renban([(4, 8), (5, 8), (6, 8)])
    puzzle.add_renban([(0, 4), (0, 3), (1, 3)])
    puzzle.add_renban([(7, 5), (6, 4)])
    puzzle.add_renban([(1, 4), (1, 5)])
    puzzle.add_renban([(1, 1), (2, 2)])
    puzzle.add_renban([(0, 7), (1, 6)])
    puzzle.add_renban([(6, 6), (6, 5)])

    return puzzle
