"""PuzzleMadness Renban Sudoku — 2025-12-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-12-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/12/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 4, 0, 1, 6, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 6, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 4],
        [0, 5, 6, 0, 3, 0, 0, 0, 9],
        [4, 0, 8, 0, 0, 0, 3, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 1, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 6, 0, 5, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(6, 6), (6, 7), (6, 8), (5, 8), (4, 8)])
    puzzle.add_renban([(1, 7), (2, 7), (3, 7), (4, 7), (5, 7)])
    puzzle.add_renban([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6)])
    puzzle.add_renban([(3, 2), (3, 1), (3, 0), (4, 0)])
    puzzle.add_renban([(8, 5), (7, 5), (6, 5), (5, 5)])
    puzzle.add_renban([(8, 1), (8, 2), (7, 2), (6, 2)])
    puzzle.add_renban([(5, 4), (4, 3), (5, 2)])
    puzzle.add_renban([(4, 4), (3, 4), (3, 3)])
    puzzle.add_renban([(7, 3), (7, 4), (6, 4)])
    puzzle.add_renban([(6, 0), (7, 0), (7, 1)])
    puzzle.add_renban([(5, 0), (4, 1)])
    puzzle.add_renban([(2, 6), (3, 6)])
    puzzle.add_renban([(1, 0), (1, 1)])
    puzzle.add_renban([(0, 0), (0, 1)])
    puzzle.add_renban([(8, 7), (7, 7)])

    return puzzle
