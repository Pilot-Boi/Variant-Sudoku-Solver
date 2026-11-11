"""PuzzleMadness Renban Sudoku — 2025-09-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-09-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/9/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 4, 7, 0, 0, 0, 9, 0, 2],
        [3, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 3, 5, 0],
        [0, 0, 3, 0, 0, 0, 8, 0, 6],
        [0, 2, 9, 0, 0, 4, 0, 0, 0],
        [0, 1, 0, 0, 0, 7, 0, 0, 0],
        [0, 3, 1, 0, 0, 0, 0, 7, 0],
        [0, 7, 0, 0, 0, 1, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 3), (4, 4), (4, 5), (4, 6), (4, 7)])
    puzzle.add_renban([(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)])
    puzzle.add_renban([(5, 3), (6, 2), (7, 3), (8, 4)])
    puzzle.add_renban([(1, 2), (0, 2), (0, 1), (0, 0)])
    puzzle.add_renban([(6, 3), (6, 4), (6, 5), (5, 5)])
    puzzle.add_renban([(8, 7), (7, 7), (6, 7)])
    puzzle.add_renban([(2, 7), (1, 7), (1, 6)])
    puzzle.add_renban([(4, 1), (5, 1), (6, 1)])
    puzzle.add_renban([(1, 8), (2, 8), (3, 8)])
    puzzle.add_renban([(3, 0), (4, 0)])
    puzzle.add_renban([(7, 8), (6, 8)])
    puzzle.add_renban([(7, 1), (7, 2)])
    puzzle.add_renban([(3, 2), (3, 3)])
    puzzle.add_renban([(0, 3), (1, 4)])

    return puzzle
