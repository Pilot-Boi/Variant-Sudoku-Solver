"""PuzzleMadness Renban Sudoku — 2025-11-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-11-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/11/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 2, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 8, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 5, 4, 9, 0, 0, 0],
        [0, 0, 9, 3, 0, 0, 0, 0, 8],
        [4, 0, 0, 6, 0, 2, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 4, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 4), (1, 5), (2, 6), (1, 7), (0, 8)])
    puzzle.add_renban([(4, 3), (5, 3), (6, 3), (7, 3), (8, 3)])
    puzzle.add_renban([(4, 7), (5, 7), (6, 7), (7, 7), (8, 7)])
    puzzle.add_renban([(7, 0), (8, 0), (8, 1), (8, 2)])
    puzzle.add_renban([(2, 0), (3, 1), (4, 2), (3, 3)])
    puzzle.add_renban([(8, 8), (7, 8), (6, 8), (5, 8)])
    puzzle.add_renban([(0, 2), (0, 1), (1, 1)])
    puzzle.add_renban([(6, 6), (5, 6), (5, 5)])
    puzzle.add_renban([(7, 1), (7, 2), (6, 2)])
    puzzle.add_renban([(3, 0), (4, 0), (5, 0)])
    puzzle.add_renban([(0, 0), (1, 0)])
    puzzle.add_renban([(7, 6), (6, 5)])
    puzzle.add_renban([(4, 1), (5, 2)])
    puzzle.add_renban([(7, 4), (6, 4)])
    puzzle.add_renban([(3, 8), (4, 8)])

    return puzzle
