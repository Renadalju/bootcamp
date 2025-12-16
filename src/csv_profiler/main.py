from .io import read_csv_rows
from .profile import basic_profile
from .render import write_json, write_markdown


def main() -> None:
    rows = read_csv_rows("data/sample.csv")
    report = basic_profile(rows)
    write_json(report, "outputs/report.json")
    write_markdown(report, "outputs/report.md")
    print("Wrote outputs/report.json and outputs/report.md")


if __name__ == "__main__":
    main()
