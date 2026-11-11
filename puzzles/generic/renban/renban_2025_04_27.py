"""PuzzleMadness Renban Sudoku — 2025-04-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-04-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/4/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [7, 0, 0, 0, 0, 0, 5, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 7, 0, 0, 3],
        [0, 0, 0, 0, 1, 5, 9, 0, 8],
        [0, 0, 0, 0, 2, 0, 0, 6, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [2, 9, 0, 4, 0, 0, 6, 0, 0],
        [0, 0, 0, 9, 0, 0, 8, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(3, 7), (4, 7), (5, 7), (6, 7), (7, 7)])
    puzzle.add_renban([(3, 8), (2, 8), (1, 8), (1, 7), (1, 6)])
    puzzle.add_renban([(8, 2), (8, 3), (8, 4), (8, 5), (8, 6)])
    puzzle.add_renban([(2, 5), (2, 4), (2, 3), (3, 3)])
    puzzle.add_renban([(3, 2), (4, 2), (5, 2), (5, 3)])
    puzzle.add_renban([(6, 5), (6, 4), (6, 3), (7, 3)])
    puzzle.add_renban([(7, 4), (7, 5), (7, 6)])
    puzzle.add_renban([(0, 4), (0, 5), (0, 6)])
    puzzle.add_renban([(1, 1), (2, 0), (3, 1)])
    puzzle.add_renban([(7, 0), (8, 0), (8, 1)])
    puzzle.add_renban([(0, 2), (1, 2)])
    puzzle.add_renban([(5, 0), (5, 1)])
    puzzle.add_renban([(2, 6), (3, 6)])
    puzzle.add_renban([(0, 0), (1, 0)])
    puzzle.add_renban([(6, 1), (6, 2)])

    return puzzle
