from csv_profiler.io import read_csv_rows
from csv_profiler.profile import basic_profile
from csv_profiler.render import write_json, write_markdown

def main() -> none:
    rows = read_csv_rows("data/sample.csv")