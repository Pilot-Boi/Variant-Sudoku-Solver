"""PuzzleMadness Renban Sudoku — 2025-04-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-04-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/4/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 9, 0, 0, 0, 6, 8, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 3],
        [4, 8, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 3, 5, 0, 0, 0, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 4), (1, 4), (2, 4), (3, 4), (4, 4)])
    puzzle.add_renban([(4, 1), (4, 2), (4, 3), (3, 3), (2, 3)])
    puzzle.add_renban([(3, 6), (4, 6), (5, 6), (6, 6), (7, 6)])
    puzzle.add_renban([(7, 1), (8, 1), (8, 2), (8, 3)])
    puzzle.add_renban([(0, 3), (0, 2), (1, 2), (2, 2)])
    puzzle.add_renban([(6, 4), (7, 4), (8, 4), (8, 5)])
    puzzle.add_renban([(3, 0), (4, 0), (5, 0)])
    puzzle.add_renban([(7, 7), (7, 8), (6, 8)])
    puzzle.add_renban([(0, 1), (0, 0), (1, 0)])
    puzzle.add_renban([(6, 7), (5, 8), (4, 7)])
    puzzle.add_renban([(4, 5), (5, 4)])
    puzzle.add_renban([(6, 0), (6, 1)])
    puzzle.add_renban([(1, 8), (2, 7)])
    puzzle.add_renban([(0, 8), (1, 7)])
    puzzle.add_renban([(7, 5), (6, 5)])

    return puzzle
