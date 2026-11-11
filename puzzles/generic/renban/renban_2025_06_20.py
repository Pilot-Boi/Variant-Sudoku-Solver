"""PuzzleMadness Renban Sudoku — 2025-06-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-06-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/6/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 2, 0],
        [0, 4, 6, 0, 8, 0, 0, 0, 3],
        [9, 1, 0, 0, 0, 3, 7, 0, 0],
        [0, 0, 8, 5, 0, 6, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 7, 3, 0, 1],
        [0, 0, 0, 2, 0, 0, 0, 5, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 7), (5, 7), (6, 7), (7, 7), (8, 7)])
    puzzle.add_renban([(4, 1), (4, 2), (4, 3), (4, 4), (4, 5)])
    puzzle.add_renban([(5, 1), (5, 2), (5, 3), (5, 4), (5, 5)])
    puzzle.add_renban([(2, 4), (1, 4), (1, 3), (1, 2)])
    puzzle.add_renban([(6, 3), (6, 4), (6, 5), (6, 6)])
    puzzle.add_renban([(1, 6), (2, 6), (3, 6), (4, 6)])
    puzzle.add_renban([(3, 2), (3, 3), (2, 3)])
    puzzle.add_renban([(0, 1), (0, 0), (1, 0)])
    puzzle.add_renban([(1, 7), (0, 6), (1, 5)])
    puzzle.add_renban([(7, 5), (8, 5), (8, 6)])
    puzzle.add_renban([(8, 0), (7, 0)])
    puzzle.add_renban([(8, 1), (7, 1)])
    puzzle.add_renban([(6, 1), (6, 2)])
    puzzle.add_renban([(2, 1), (3, 1)])
    puzzle.add_renban([(2, 5), (3, 4)])

    return puzzle
