"""PuzzleMadness Renban Sudoku — 2025-02-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-02-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/2/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 5, 0, 1, 0, 0, 9, 0],
        [0, 0, 0, 2, 5, 0, 0, 0, 4],
        [6, 0, 0, 0, 0, 0, 2, 0, 0],
        [2, 8, 0, 0, 0, 0, 6, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 3, 8, 0, 0, 0, 0],
        [0, 6, 3, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(3, 1), (4, 1), (5, 1), (6, 1), (7, 1)])
    puzzle.add_renban([(6, 4), (5, 4), (4, 4), (4, 3), (4, 2)])
    puzzle.add_renban([(7, 5), (7, 6), (7, 7), (6, 7), (5, 7)])
    puzzle.add_renban([(2, 2), (1, 2), (1, 1), (1, 0)])
    puzzle.add_renban([(0, 2), (1, 3), (2, 4), (1, 5)])
    puzzle.add_renban([(8, 8), (8, 7), (8, 6), (8, 5)])
    puzzle.add_renban([(6, 2), (7, 2), (7, 3)])
    puzzle.add_renban([(4, 5), (5, 5), (6, 5)])
    puzzle.add_renban([(2, 7), (1, 7), (1, 6)])
    puzzle.add_renban([(3, 7), (3, 8), (2, 8)])
    puzzle.add_renban([(4, 8), (5, 8)])
    puzzle.add_renban([(8, 0), (7, 0)])
    puzzle.add_renban([(8, 2), (8, 3)])
    puzzle.add_renban([(4, 7), (3, 6)])
    puzzle.add_renban([(4, 6), (5, 6)])

    return puzzle
