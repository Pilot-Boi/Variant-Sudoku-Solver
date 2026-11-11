"""PuzzleMadness Renban Sudoku — 2025-05-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-05-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/5/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 3, 8, 0, 0, 0, 0, 6],
        [0, 0, 0, 7, 0, 0, 0, 0, 4],
        [0, 0, 0, 1, 0, 0, 0, 0, 5],
        [0, 1, 6, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [3, 0, 7, 0, 0, 4, 9, 0, 0],
        [0, 0, 5, 0, 0, 6, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(3, 4), (3, 5), (3, 6), (3, 7), (3, 8)])
    puzzle.add_renban([(0, 6), (0, 5), (0, 4), (1, 4), (2, 4)])
    puzzle.add_renban([(1, 1), (2, 1), (3, 1), (4, 1), (5, 1)])
    puzzle.add_renban([(0, 1), (0, 0), (1, 0), (2, 0)])
    puzzle.add_renban([(7, 7), (6, 6), (7, 5), (8, 4)])
    puzzle.add_renban([(6, 1), (7, 1), (7, 2), (7, 3)])
    puzzle.add_renban([(0, 3), (1, 3), (2, 3)])
    puzzle.add_renban([(6, 7), (5, 6), (6, 5)])
    puzzle.add_renban([(5, 4), (6, 3), (7, 4)])
    puzzle.add_renban([(5, 7), (4, 6), (5, 5)])
    puzzle.add_renban([(6, 0), (5, 0)])
    puzzle.add_renban([(1, 7), (2, 7)])
    puzzle.add_renban([(5, 2), (5, 3)])
    puzzle.add_renban([(7, 8), (6, 8)])
    puzzle.add_renban([(2, 6), (2, 5)])

    return puzzle
