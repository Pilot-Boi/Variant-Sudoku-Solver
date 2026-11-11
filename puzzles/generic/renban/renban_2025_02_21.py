"""PuzzleMadness Renban Sudoku — 2025-02-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-02-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/2/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 3, 5, 1, 6, 0, 0],
        [1, 0, 0, 9, 4, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 4, 8, 0, 0, 9, 0, 0, 3],
        [2, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 7],
        [0, 0, 9, 0, 0, 6, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 3), (3, 4), (2, 5), (1, 4), (0, 3)])
    puzzle.add_renban([(5, 1), (4, 2), (3, 3), (2, 2), (1, 1)])
    puzzle.add_renban([(5, 6), (5, 7), (5, 8), (4, 8), (3, 8)])
    puzzle.add_renban([(7, 8), (7, 7), (7, 6), (7, 5)])
    puzzle.add_renban([(1, 7), (2, 6), (3, 5), (4, 4)])
    puzzle.add_renban([(6, 3), (7, 3), (8, 3), (8, 4)])
    puzzle.add_renban([(6, 4), (6, 5), (6, 6)])
    puzzle.add_renban([(5, 3), (5, 2), (6, 2)])
    puzzle.add_renban([(6, 1), (7, 1), (7, 2)])
    puzzle.add_renban([(4, 7), (3, 7), (3, 6)])
    puzzle.add_renban([(1, 3), (2, 4)])
    puzzle.add_renban([(0, 0), (0, 1)])
    puzzle.add_renban([(0, 6), (1, 6)])
    puzzle.add_renban([(3, 0), (4, 1)])
    puzzle.add_renban([(0, 5), (1, 5)])

    return puzzle
