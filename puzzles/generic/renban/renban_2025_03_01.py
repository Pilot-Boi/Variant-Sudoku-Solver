"""PuzzleMadness Renban Sudoku — 2025-03-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-03-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/3/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 8, 0, 0, 0, 0, 0],
        [0, 8, 9, 6, 3, 0, 0, 0, 5],
        [0, 9, 0, 0, 2, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 5, 0],
        [5, 0, 1, 0, 0, 8, 0, 0, 0],
        [0, 0, 3, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 2, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 4), (5, 5), (6, 6), (7, 7), (8, 8)])
    puzzle.add_renban([(0, 7), (0, 6), (0, 5), (1, 5), (2, 5)])
    puzzle.add_renban([(3, 5), (3, 4), (3, 3), (4, 3), (5, 3)])
    puzzle.add_renban([(3, 6), (3, 7), (3, 8), (2, 8)])
    puzzle.add_renban([(6, 2), (6, 3), (6, 4), (6, 5)])
    puzzle.add_renban([(8, 2), (8, 3), (8, 4), (7, 4)])
    puzzle.add_renban([(2, 6), (2, 7), (1, 7)])
    puzzle.add_renban([(4, 0), (5, 0), (5, 1)])
    puzzle.add_renban([(8, 7), (8, 6), (8, 5)])
    puzzle.add_renban([(0, 3), (1, 4)])
    puzzle.add_renban([(2, 1), (3, 1)])
    puzzle.add_renban([(6, 0), (6, 1)])
    puzzle.add_renban([(2, 2), (3, 2)])
    puzzle.add_renban([(1, 2), (2, 3)])

    return puzzle
