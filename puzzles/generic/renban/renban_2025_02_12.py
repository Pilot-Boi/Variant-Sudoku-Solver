"""PuzzleMadness Renban Sudoku — 2025-02-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-02-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/2/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [5, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 8, 0, 4, 0, 3, 6, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 9, 4],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 1, 3, 0, 9, 0, 8, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 3), (4, 4), (4, 5), (4, 6), (4, 7)])
    puzzle.add_renban([(2, 3), (2, 4), (2, 5), (1, 5), (0, 5)])
    puzzle.add_renban([(1, 0), (2, 0), (3, 0), (3, 1), (3, 2)])
    puzzle.add_renban([(8, 8), (7, 7), (6, 6), (5, 5)])
    puzzle.add_renban([(7, 3), (6, 3), (5, 3), (5, 2)])
    puzzle.add_renban([(0, 2), (0, 1), (1, 1), (2, 1)])
    puzzle.add_renban([(1, 8), (1, 7), (1, 6)])
    puzzle.add_renban([(7, 0), (7, 1), (7, 2)])
    puzzle.add_renban([(0, 4), (0, 3), (1, 3)])
    puzzle.add_renban([(5, 7), (4, 8), (3, 7)])
    puzzle.add_renban([(6, 7), (5, 6)])
    puzzle.add_renban([(2, 7), (2, 6)])
    puzzle.add_renban([(7, 5), (6, 4)])
    puzzle.add_renban([(1, 2), (2, 2)])
    puzzle.add_renban([(5, 0), (4, 1)])

    return puzzle
