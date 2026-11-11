"""PuzzleMadness Renban Sudoku — 2025-08-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-08-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/8/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 9, 7, 3],
        [0, 0, 0, 0, 4, 0, 0, 8, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 2, 0, 0, 9, 0, 0, 0],
        [0, 0, 7, 0, 1, 3, 0, 9, 4],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 1, 0, 9, 0, 0, 0, 0],
        [0, 0, 3, 8, 7, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 4, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(6, 5), (5, 5), (4, 5), (4, 4), (4, 3)])
    puzzle.add_renban([(4, 8), (5, 7), (6, 6), (7, 5), (8, 4)])
    puzzle.add_renban([(0, 3), (0, 4), (0, 5), (0, 6), (0, 7)])
    puzzle.add_renban([(3, 1), (3, 0), (4, 0), (5, 0)])
    puzzle.add_renban([(2, 0), (2, 1), (2, 2), (1, 2)])
    puzzle.add_renban([(7, 3), (6, 4), (5, 3), (4, 2)])
    puzzle.add_renban([(0, 2), (0, 1), (1, 1)])
    puzzle.add_renban([(8, 8), (7, 8), (6, 8)])
    puzzle.add_renban([(7, 0), (7, 1), (7, 2)])
    puzzle.add_renban([(1, 4), (2, 4), (2, 5)])
    puzzle.add_renban([(4, 1), (5, 2)])
    puzzle.add_renban([(4, 6), (5, 6)])
    puzzle.add_renban([(8, 0), (8, 1)])
    puzzle.add_renban([(3, 6), (3, 5)])
    puzzle.add_renban([(6, 0), (6, 1)])

    return puzzle
