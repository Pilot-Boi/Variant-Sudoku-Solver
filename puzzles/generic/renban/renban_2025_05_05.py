"""PuzzleMadness Renban Sudoku — 2025-05-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-05-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/5/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 9, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 3, 0, 2, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 7],
        [0, 7, 0, 3, 0, 0, 0, 9, 0],
        [5, 6, 0, 0, 0, 2, 0, 0, 4],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 6, 0, 2],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 8, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)])
    puzzle.add_renban([(1, 1), (1, 2), (1, 3), (1, 4), (1, 5)])
    puzzle.add_renban([(2, 6), (2, 7), (2, 8), (1, 8), (0, 8)])
    puzzle.add_renban([(6, 0), (7, 1), (8, 2), (7, 3)])
    puzzle.add_renban([(4, 2), (4, 1), (4, 0), (5, 0)])
    puzzle.add_renban([(5, 5), (5, 4), (5, 3), (6, 3)])
    puzzle.add_renban([(7, 2), (6, 2), (6, 1)])
    puzzle.add_renban([(7, 7), (6, 7), (6, 6)])
    puzzle.add_renban([(5, 6), (5, 7), (4, 7)])
    puzzle.add_renban([(8, 8), (7, 8), (6, 8)])
    puzzle.add_renban([(3, 6), (3, 5)])
    puzzle.add_renban([(0, 7), (0, 6)])
    puzzle.add_renban([(8, 7), (8, 6)])
    puzzle.add_renban([(3, 1), (3, 2)])
    puzzle.add_renban([(3, 4), (4, 5)])

    return puzzle
