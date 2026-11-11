"""PuzzleMadness Killer Sudoku — 2025-09-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-09-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/9/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_killer_cage([(0, 0), (0, 1), (0, 2), (1, 0)], 21)
    puzzle.add_killer_cage([(1, 1), (1, 2), (2, 0), (2, 1)], 21)
    puzzle.add_killer_cage([(0, 3), (1, 3), (1, 4)], 9)
    puzzle.add_killer_cage([(0, 4), (0, 5)], 8)
    puzzle.add_killer_cage([(0, 6), (0, 7), (1, 5), (1, 6)], 20)
    puzzle.add_killer_cage([(0, 8), (1, 8), (2, 8)], 18)
    puzzle.add_killer_cage([(1, 7), (2, 6), (2, 7), (3, 6), (4, 6)], 19)
    puzzle.add_killer_cage([(3, 7), (3, 8), (4, 7)], 15)
    puzzle.add_killer_cage([(4, 8), (5, 7), (5, 8)], 13)
    puzzle.add_killer_cage([(6, 7), (6, 8), (7, 6), (7, 7)], 17)
    puzzle.add_killer_cage([(7, 8), (8, 6), (8, 7), (8, 8)], 20)
    puzzle.add_killer_cage([(2, 2), (2, 3), (2, 4), (3, 2)], 23)
    puzzle.add_killer_cage([(2, 5), (3, 5), (4, 5)], 22)
    puzzle.add_killer_cage([(3, 3), (3, 4), (4, 4), (5, 4), (5, 5)], 24)
    puzzle.add_killer_cage([(4, 3), (5, 3), (6, 3)], 9)
    puzzle.add_killer_cage([(5, 6), (6, 4), (6, 5), (6, 6)], 26)
    puzzle.add_killer_cage([(7, 4), (7, 5), (8, 5)], 19)
    puzzle.add_killer_cage([(8, 3), (8, 4)], 12)
    puzzle.add_killer_cage([(7, 2), (7, 3), (8, 1), (8, 2)], 18)
    puzzle.add_killer_cage([(4, 2), (5, 2), (6, 1), (6, 2), (7, 1)], 15)
    puzzle.add_killer_cage([(3, 0), (3, 1), (4, 0)], 17)
    puzzle.add_killer_cage([(4, 1), (5, 0), (5, 1)], 18)
    puzzle.add_killer_cage([(6, 0), (7, 0), (8, 0)], 21)

    return puzzle
