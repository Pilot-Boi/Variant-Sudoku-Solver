"""PuzzleMadness Renban Sudoku — 2025-08-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-08-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/8/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 6, 4, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 2, 0, 4, 0, 0, 0, 7],
        [1, 0, 0, 0, 0, 0, 7, 2, 0],
        [0, 0, 3, 8, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 9, 0],
        [0, 0, 0, 7, 9, 0, 0, 0, 3],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 2), (5, 3), (6, 4), (5, 5), (4, 6)])
    puzzle.add_renban([(1, 4), (2, 5), (3, 6), (2, 7), (1, 8)])
    puzzle.add_renban([(0, 2), (0, 1), (0, 0), (1, 0), (2, 0)])
    puzzle.add_renban([(7, 1), (8, 1), (8, 2), (8, 3)])
    puzzle.add_renban([(3, 1), (4, 1), (5, 1), (5, 2)])
    puzzle.add_renban([(3, 4), (2, 4), (2, 3), (2, 2)])
    puzzle.add_renban([(0, 8), (1, 7), (2, 6)])
    puzzle.add_renban([(2, 8), (3, 8), (4, 8)])
    puzzle.add_renban([(8, 7), (7, 7), (6, 7)])
    puzzle.add_renban([(8, 8), (7, 8), (6, 8)])
    puzzle.add_renban([(8, 6), (7, 6)])
    puzzle.add_renban([(8, 4), (7, 3)])
    puzzle.add_renban([(0, 6), (1, 5)])
    puzzle.add_renban([(4, 3), (5, 4)])
    puzzle.add_renban([(6, 6), (6, 5)])

    return puzzle
