import argparse

from converter import Converter


def main():
    parser = argparse.ArgumentParser(description="Degiro CSV to Koyfin MP.")
    parser.add_argument(
        "--input_csv",
        nargs="*",
        required=True,
        metavar="~/Downloads/Portfolio1.csv ~/Downloads/Portfolio2.csv",
        help="CSV from degiro, multiple can be passed (../Portfolio1.csv ~/Downloads/Portfolio2.csv)",
    )
    args = parser.parse_args()
    Converter(input_csv=args.input_csv).build()


if __name__ == "__main__":
    main()
