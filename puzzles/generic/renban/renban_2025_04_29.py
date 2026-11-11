"""PuzzleMadness Renban Sudoku — 2025-04-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-04-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/4/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 8, 3, 0],
        [0, 0, 6, 0, 0, 0, 9, 0, 0],
        [0, 0, 1, 2, 0, 0, 0, 6, 9],
        [0, 0, 7, 0, 0, 3, 1, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 8, 0, 0, 5, 1, 0],
        [0, 3, 0, 0, 0, 2, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(1, 5), (1, 4), (1, 3), (2, 3), (3, 3)])
    puzzle.add_renban([(3, 0), (4, 0), (5, 0), (5, 1), (5, 2)])
    puzzle.add_renban([(7, 1), (7, 2), (7, 3), (7, 4), (7, 5)])
    puzzle.add_renban([(2, 5), (3, 5), (3, 6), (3, 7)])
    puzzle.add_renban([(6, 2), (6, 3), (5, 3), (4, 3)])
    puzzle.add_renban([(3, 4), (4, 5), (5, 6), (6, 7)])
    puzzle.add_renban([(0, 3), (0, 2), (1, 2)])
    puzzle.add_renban([(2, 2), (3, 1), (4, 2)])
    puzzle.add_renban([(2, 8), (1, 8), (1, 7)])
    puzzle.add_renban([(7, 6), (6, 6), (6, 5)])
    puzzle.add_renban([(8, 7), (8, 6)])
    puzzle.add_renban([(8, 4), (8, 5)])
    puzzle.add_renban([(7, 0), (6, 0)])
    puzzle.add_renban([(0, 0), (1, 1)])
    puzzle.add_renban([(1, 6), (2, 6)])

    return puzzle
