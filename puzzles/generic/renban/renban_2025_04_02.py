"""PuzzleMadness Renban Sudoku — 2025-04-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-04-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/4/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 5, 0, 0, 0, 7, 8],
        [0, 0, 0, 0, 0, 1, 0, 0, 3],
        [0, 7, 0, 0, 0, 9, 4, 0, 0],
        [0, 0, 0, 0, 7, 5, 0, 0, 0],
        [0, 0, 3, 0, 6, 0, 7, 0, 0],
        [0, 9, 0, 3, 0, 2, 0, 0, 0],
        [2, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 5, 0, 7],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(6, 1), (5, 2), (4, 3), (3, 2), (2, 1)])
    puzzle.add_renban([(2, 4), (1, 3), (0, 2), (1, 1), (2, 0)])
    puzzle.add_renban([(6, 5), (6, 4), (6, 3), (7, 3), (8, 3)])
    puzzle.add_renban([(3, 6), (3, 5), (4, 5), (5, 5)])
    puzzle.add_renban([(8, 5), (8, 6), (7, 6), (6, 6)])
    puzzle.add_renban([(2, 6), (2, 7), (1, 7), (0, 7)])
    puzzle.add_renban([(3, 1), (4, 1), (4, 2)])
    puzzle.add_renban([(5, 7), (5, 8), (4, 8)])
    puzzle.add_renban([(2, 3), (3, 4), (2, 5)])
    puzzle.add_renban([(1, 8), (2, 8), (3, 8)])
    puzzle.add_renban([(7, 0), (7, 1)])
    puzzle.add_renban([(1, 6), (1, 5)])
    puzzle.add_renban([(2, 2), (3, 3)])
    puzzle.add_renban([(8, 8), (8, 7)])
    puzzle.add_renban([(8, 0), (8, 1)])

    return puzzle
