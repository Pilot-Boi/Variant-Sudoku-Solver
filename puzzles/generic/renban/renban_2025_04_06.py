"""PuzzleMadness Renban Sudoku — 2025-04-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-04-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/4/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 6, 4, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 6, 0, 0],
        [7, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 4, 5, 0, 0, 2, 8, 0],
        [3, 0, 0, 7, 0, 0, 0, 5, 0],
        [0, 5, 0, 3, 0, 0, 0, 7, 0],
        [6, 7, 0, 0, 5, 0, 0, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(3, 7), (4, 7), (5, 7), (6, 7), (7, 7)])
    puzzle.add_renban([(2, 2), (3, 2), (4, 2), (4, 3), (4, 4)])
    puzzle.add_renban([(1, 4), (1, 5), (1, 6), (1, 7), (1, 8)])
    puzzle.add_renban([(4, 1), (5, 1), (5, 2), (5, 3)])
    puzzle.add_renban([(6, 2), (6, 3), (6, 4), (6, 5)])
    puzzle.add_renban([(8, 4), (8, 5), (8, 6), (8, 7)])
    puzzle.add_renban([(3, 1), (3, 0), (4, 0)])
    puzzle.add_renban([(3, 8), (4, 8), (5, 8)])
    puzzle.add_renban([(7, 3), (7, 4), (7, 5)])
    puzzle.add_renban([(1, 0), (1, 1), (1, 2)])
    puzzle.add_renban([(8, 0), (7, 1)])
    puzzle.add_renban([(2, 5), (3, 5)])
    puzzle.add_renban([(2, 4), (3, 4)])
    puzzle.add_renban([(2, 0), (2, 1)])
    puzzle.add_renban([(6, 0), (6, 1)])

    return puzzle
