"""PuzzleMadness Renban Sudoku — 2025-07-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-07-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/7/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 8, 0, 9, 0],
        [0, 0, 0, 0, 4, 1, 0, 0, 2],
        [0, 8, 9, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 5, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 7, 0, 9, 4, 0, 0, 0],
        [0, 6, 0, 0, 8, 0, 0, 0, 3],
        [4, 9, 0, 0, 6, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 3), (4, 4), (4, 5), (3, 5), (2, 5)])
    puzzle.add_renban([(3, 3), (4, 2), (5, 1), (6, 2), (7, 3)])
    puzzle.add_renban([(3, 8), (4, 7), (5, 6), (6, 5), (7, 4)])
    puzzle.add_renban([(8, 7), (7, 7), (6, 7), (5, 7)])
    puzzle.add_renban([(6, 1), (6, 0), (7, 0), (8, 0)])
    puzzle.add_renban([(3, 1), (3, 0), (4, 0), (5, 0)])
    puzzle.add_renban([(0, 4), (1, 4), (2, 4)])
    puzzle.add_renban([(0, 2), (0, 1), (1, 1)])
    puzzle.add_renban([(2, 6), (3, 6), (4, 6)])
    puzzle.add_renban([(0, 8), (1, 7)])
    puzzle.add_renban([(4, 1), (3, 2)])
    puzzle.add_renban([(2, 7), (3, 7)])
    puzzle.add_renban([(2, 3), (3, 4)])
    puzzle.add_renban([(6, 4), (5, 3)])

    return puzzle
