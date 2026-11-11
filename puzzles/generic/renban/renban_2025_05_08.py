"""PuzzleMadness Renban Sudoku — 2025-05-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-05-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/5/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 5, 0, 0, 0, 0, 0, 9, 7],
        [0, 0, 0, 0, 0, 1, 0, 0, 6],
        [6, 0, 3, 0, 5, 0, 0, 0, 1],
        [0, 0, 0, 9, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 8, 0, 6, 4, 0, 0, 0],
        [0, 6, 0, 0, 3, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 8, 5],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(8, 5), (7, 5), (6, 5), (6, 4), (6, 3)])
    puzzle.add_renban([(3, 2), (3, 3), (3, 4), (2, 4), (1, 4)])
    puzzle.add_renban([(1, 8), (1, 7), (1, 6), (2, 6), (3, 6)])
    puzzle.add_renban([(1, 5), (0, 4), (1, 3), (2, 2)])
    puzzle.add_renban([(4, 3), (5, 3), (5, 4), (5, 5)])
    puzzle.add_renban([(8, 6), (8, 7), (8, 8), (7, 8)])
    puzzle.add_renban([(6, 7), (6, 6), (7, 6)])
    puzzle.add_renban([(5, 2), (6, 1), (7, 2)])
    puzzle.add_renban([(2, 7), (3, 7), (4, 7)])
    puzzle.add_renban([(3, 1), (4, 1), (5, 1)])
    puzzle.add_renban([(1, 0), (2, 1)])
    puzzle.add_renban([(8, 1), (8, 2)])
    puzzle.add_renban([(7, 3), (7, 4)])
    puzzle.add_renban([(2, 5), (3, 5)])
    puzzle.add_renban([(0, 7), (0, 6)])

    return puzzle
