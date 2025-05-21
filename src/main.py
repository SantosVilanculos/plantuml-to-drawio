import sys
from pathlib import Path

from conversion import conversion


def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <PlantUML-file>")
        sys.exit(1)

    plantuml_file = Path.cwd().joinpath(sys.argv[1])

    if not plantuml_file.is_file():
        print("Error: PlantUML file not found.")
        sys.exit(1)

    i = str(plantuml_file.absolute())
    d = ("-d" in sys.argv) or ("--debug" in sys.argv)

    print(conversion(i, d))


if __name__ == "__main__":
    main()
