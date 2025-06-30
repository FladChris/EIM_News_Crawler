"""Command line interface for the EIM news crawler."""

import argparse
from .crawler import crawl_news


def main() -> None:
    """Parse command line arguments and trigger crawling."""
    parser = argparse.ArgumentParser(
        description="Download Nachrichtenartikel der EIM-Fakultät als DOCX-Dateien."
    )
    parser.add_argument(
        "year",
        type=int,
        help="Jahr der zu speichernden Artikel",
    )
    args = parser.parse_args()

    count = crawl_news(args.year)
    print(f"Anzahl der News: {count}")


if __name__ == "__main__":
    main()
