"""PuzzleMadness Killer Sudoku — 2025-11-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-11-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/11/19'
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

    puzzle.add_killer_cage([(0, 0), (0, 1), (1, 0)], 15)
    puzzle.add_killer_cage([(0, 2), (0, 3), (0, 4)], 20)
    puzzle.add_killer_cage([(0, 5), (1, 5), (2, 5)], 14)
    puzzle.add_killer_cage([(0, 6), (1, 6), (2, 6)], 15)
    puzzle.add_killer_cage([(0, 7), (0, 8), (1, 7)], 14)
    puzzle.add_killer_cage([(1, 8), (2, 8), (3, 8)], 22)
    puzzle.add_killer_cage([(2, 7), (3, 7), (4, 7)], 18)
    puzzle.add_killer_cage([(4, 8), (5, 8), (6, 8)], 10)
    puzzle.add_killer_cage([(7, 8), (8, 7), (8, 8)], 13)
    puzzle.add_killer_cage([(7, 5), (7, 6), (7, 7)], 15)
    puzzle.add_killer_cage([(6, 5), (6, 6), (6, 7)], 15)
    puzzle.add_killer_cage([(5, 5), (5, 6), (5, 7)], 14)
    puzzle.add_killer_cage([(3, 4), (3, 5), (3, 6)], 7)
    puzzle.add_killer_cage([(1, 4), (2, 4)], 5)
    puzzle.add_killer_cage([(1, 1), (1, 2), (1, 3)], 18)
    puzzle.add_killer_cage([(2, 1), (2, 2), (2, 3)], 13)
    puzzle.add_killer_cage([(3, 1), (3, 2), (3, 3)], 14)
    puzzle.add_killer_cage([(2, 0), (3, 0), (4, 0)], 18)
    puzzle.add_killer_cage([(4, 1), (5, 1), (6, 1)], 16)
    puzzle.add_killer_cage([(5, 0), (6, 0), (7, 0)], 10)
    puzzle.add_killer_cage([(7, 1), (8, 0), (8, 1)], 17)
    puzzle.add_killer_cage([(6, 2), (7, 2), (8, 2)], 10)
    puzzle.add_killer_cage([(6, 3), (7, 3), (8, 3)], 9)
    puzzle.add_killer_cage([(6, 4), (7, 4)], 17)
    puzzle.add_killer_cage([(8, 4), (8, 5), (8, 6)], 20)
    puzzle.add_killer_cage([(4, 2), (4, 3), (4, 4), (4, 5), (4, 6)], 25)
    puzzle.add_killer_cage([(5, 2), (5, 3), (5, 4)], 21)

    return puzzle
