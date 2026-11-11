"""PuzzleMadness Renban Sudoku — 2025-04-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-04-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/4/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 2, 5, 0, 3, 1, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 3],
        [0, 0, 9, 0, 0, 0, 0, 0, 2],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 4, 0, 0, 0, 0],
        [6, 0, 0, 0, 1, 0, 0, 3, 0],
        [0, 0, 8, 0, 0, 4, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 7), (1, 7), (2, 7), (3, 7), (4, 7)])
    puzzle.add_renban([(0, 6), (1, 6), (2, 6), (3, 6), (4, 6)])
    puzzle.add_renban([(3, 1), (4, 1), (5, 1), (5, 2), (5, 3)])
    puzzle.add_renban([(8, 8), (7, 8), (6, 8), (6, 7)])
    puzzle.add_renban([(6, 2), (7, 3), (6, 4), (5, 5)])
    puzzle.add_renban([(8, 3), (8, 4), (8, 5), (8, 6)])
    puzzle.add_renban([(7, 1), (8, 1), (8, 2)])
    puzzle.add_renban([(2, 5), (1, 4), (2, 3)])
    puzzle.add_renban([(6, 1), (6, 0), (7, 0)])
    puzzle.add_renban([(4, 4), (3, 3), (4, 2)])
    puzzle.add_renban([(0, 0), (0, 1)])
    puzzle.add_renban([(6, 6), (6, 5)])
    puzzle.add_renban([(0, 3), (1, 3)])
    puzzle.add_renban([(4, 8), (5, 7)])
    puzzle.add_renban([(1, 1), (2, 2)])

    return puzzle
