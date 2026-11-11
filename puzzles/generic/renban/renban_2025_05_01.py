"""PuzzleMadness Renban Sudoku — 2025-05-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-05-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/5/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 5, 0, 0, 0, 9],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 3, 7, 0, 0],
        [4, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 8, 0, 0, 2, 0, 0, 7, 0],
        [0, 0, 6, 4, 0, 0, 2, 8, 5],
        [0, 4, 0, 0, 0, 0, 0, 0, 2],
        [0, 1, 0, 9, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 3, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(3, 3), (2, 3), (1, 3), (1, 2), (1, 1)])
    puzzle.add_renban([(7, 4), (7, 5), (7, 6), (7, 7), (7, 8)])
    puzzle.add_renban([(0, 4), (0, 5), (0, 6), (0, 7)])
    puzzle.add_renban([(4, 4), (4, 3), (5, 3), (6, 3)])
    puzzle.add_renban([(3, 8), (4, 8), (5, 8), (6, 8)])
    puzzle.add_renban([(5, 5), (4, 6), (3, 5)])
    puzzle.add_renban([(7, 0), (7, 1), (7, 2)])
    puzzle.add_renban([(4, 7), (5, 7), (6, 7)])
    puzzle.add_renban([(0, 1), (0, 0), (1, 0)])
    puzzle.add_renban([(1, 5), (2, 4)])
    puzzle.add_renban([(3, 0), (4, 0)])
    puzzle.add_renban([(3, 1), (4, 2)])
    puzzle.add_renban([(8, 7), (8, 6)])
    puzzle.add_renban([(1, 7), (2, 7)])

    return puzzle
