from pathlib import Path

import click

from conversion import conversion


@click.command()
@click.argument(
    "path", nargs=1, type=click.Path(exists=True, resolve_path=True)
)
@click.option(
    "-o",
    "--output",
    required=True,
    help="The output file path.",
    type=click.Path(exists=False, resolve_path=True),
)
@click.option(
    "-d",
    "--debug",
    is_flag=True,
    help="Enable debug mode. If present, debug is True; otherwise, it's False.",
)
def main(path, output, debug):
    """
    A command-line tool to transform your PlantUML into interactive diagrams.net (draw.io) files.
    """
    content = conversion(path, debug)

    output_file = Path(output)
    output_file.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    main()
