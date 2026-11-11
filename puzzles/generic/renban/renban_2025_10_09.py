"""PuzzleMadness Renban Sudoku — 2025-10-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-10-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/10/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 7, 4, 2, 0, 6, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 7, 0],
        [0, 5, 0, 0, 0, 9, 4, 8, 7],
        [0, 2, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 3, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(3, 5), (4, 4), (5, 3), (6, 4), (7, 5)])
    puzzle.add_renban([(3, 2), (3, 3), (3, 4), (2, 4), (1, 4)])
    puzzle.add_renban([(3, 6), (4, 5), (5, 4), (6, 5), (7, 6)])
    puzzle.add_renban([(4, 0), (5, 0), (6, 0), (6, 1)])
    puzzle.add_renban([(1, 7), (1, 6), (1, 5), (2, 5)])
    puzzle.add_renban([(0, 2), (0, 1), (0, 0), (1, 0)])
    puzzle.add_renban([(7, 4), (8, 4), (8, 5)])
    puzzle.add_renban([(5, 1), (5, 2), (4, 2)])
    puzzle.add_renban([(2, 1), (2, 2), (1, 2)])
    puzzle.add_renban([(4, 8), (5, 7), (6, 6)])
    puzzle.add_renban([(7, 1), (6, 2)])
    puzzle.add_renban([(3, 7), (4, 6)])
    puzzle.add_renban([(8, 0), (8, 1)])
    puzzle.add_renban([(7, 8), (7, 7)])
    puzzle.add_renban([(3, 0), (4, 1)])

    return puzzle
