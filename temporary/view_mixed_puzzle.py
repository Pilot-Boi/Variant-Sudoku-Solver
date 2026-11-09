from puzzles.thermo_killer_002 import NAME, create_puzzle
from visualization.html_renderer import show_puzzle


def main():
    puzzle = create_puzzle()

    path = show_puzzle(
        puzzle,
        title=NAME,
        output="output/thermo_killer_002.html"
    )

    print(f"Puzzle visualization saved to: {path}")


if __name__ == "__main__":
    main()