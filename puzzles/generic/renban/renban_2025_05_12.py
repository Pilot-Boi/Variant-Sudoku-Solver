"""PuzzleMadness Renban Sudoku — 2025-05-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-05-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/5/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 0, 0, 7, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 2, 4, 0, 0, 0, 0, 5, 0],
        [6, 0, 0, 0, 0, 1, 2, 0, 4],
        [0, 0, 0, 2, 9, 0, 0, 0, 7],
        [0, 0, 0, 3, 0, 5, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 1],
        [8, 6, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(1, 2), (2, 2), (3, 2), (4, 2), (5, 2)])
    puzzle.add_renban([(5, 3), (6, 3), (7, 3), (7, 4), (7, 5)])
    puzzle.add_renban([(2, 7), (1, 7), (0, 7), (0, 6), (0, 5)])
    puzzle.add_renban([(4, 4), (3, 4), (2, 4), (2, 3)])
    puzzle.add_renban([(7, 7), (6, 6), (5, 5), (6, 4)])
    puzzle.add_renban([(3, 8), (3, 7), (3, 6), (4, 6)])
    puzzle.add_renban([(8, 7), (8, 6), (8, 5)])
    puzzle.add_renban([(5, 7), (5, 8), (4, 8)])
    puzzle.add_renban([(4, 0), (5, 0), (6, 0)])
    puzzle.add_renban([(0, 8), (1, 8)])
    puzzle.add_renban([(8, 0), (7, 1)])
    puzzle.add_renban([(0, 4), (1, 3)])
    puzzle.add_renban([(3, 1), (4, 1)])
    puzzle.add_renban([(7, 0), (6, 1)])

    return puzzle
