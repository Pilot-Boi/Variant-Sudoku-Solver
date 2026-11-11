"""PuzzleMadness Renban Sudoku — 2025-03-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-03-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/3/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 4, 8, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 9, 7],
        [9, 0, 1, 0, 0, 0, 0, 4, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 9, 0, 2, 0],
        [0, 0, 3, 0, 0, 0, 7, 8, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(3, 1), (4, 1), (5, 1), (6, 1), (7, 1)])
    puzzle.add_renban([(2, 8), (2, 7), (2, 6), (3, 6), (4, 6)])
    puzzle.add_renban([(8, 2), (8, 3), (8, 4), (7, 4), (6, 4)])
    puzzle.add_renban([(2, 4), (2, 3), (2, 2), (3, 2)])
    puzzle.add_renban([(7, 5), (8, 5), (8, 6), (8, 7)])
    puzzle.add_renban([(6, 5), (6, 6), (6, 7), (5, 7)])
    puzzle.add_renban([(0, 2), (0, 1), (1, 1)])
    puzzle.add_renban([(7, 7), (7, 8), (6, 8)])
    puzzle.add_renban([(1, 5), (0, 4), (1, 3)])
    puzzle.add_renban([(3, 5), (4, 5), (5, 5)])
    puzzle.add_renban([(4, 8), (4, 7)])
    puzzle.add_renban([(4, 2), (3, 3)])
    puzzle.add_renban([(6, 3), (5, 3)])
    puzzle.add_renban([(1, 4), (2, 5)])
    puzzle.add_renban([(0, 6), (1, 6)])

    return puzzle
