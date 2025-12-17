import pandas as pd
import streamlit as st
import csv
from io import StringIO
import sys
from pathlib import Path
import tempfile

# Allow imports from src/
sys.path.append(str(Path(__file__).resolve().parent / "src"))

from csv_profiler.profile import basic_profile
from csv_profiler.render import write_markdown


# ------------------------
# Streamlit Page Config
# ------------------------
st.set_page_config(page_title="CSV Profiler", layout="wide")
st.title("CSV Profiler")

# ------------------------
# Upload CSV
# ------------------------
uploaded = st.file_uploader("Upload a CSV", type=["csv"])
show_preview = st.checkbox("Show preview", value=True)

rows: list[dict] = []

if uploaded is not None:
    text = uploaded.getvalue().decode("utf-8-sig")
    rows = list(csv.DictReader(StringIO(text)))

    st.write("**Filename:**", uploaded.name)
    st.write("**Rows Loaded:**", len(rows))

    if show_preview:
        st.subheader("Preview (first 5 rows)")
        st.dataframe(pd.DataFrame(rows[:5]), use_container_width=True)
else:
    st.info("Upload a CSV to begin.")

# ------------------------
# Generate Report
# ------------------------
if st.button("Generate Report", disabled=not rows):
    report = basic_profile(rows)
    st.session_state["report"] = report

# ------------------------
# Display Report
# ------------------------
report = st.session_state.get("report")

if report:
    # ===== Tabs =====
    tab1, tab2, tab3 = st.tabs(
        ["📊 Tables", "📝 Markdown Report", "🧾 Raw JSON"]
    )

    # ===== Tab 1: Tables =====
    with tab1:
        st.subheader("Dataset Summary")

        summary_df = pd.DataFrame(
            {
                "Metric": ["Rows", "Columns"],
                "Value": [report["rows"], report["n_cols"]],
            }
        )
        st.table(summary_df)

        st.subheader("Missing & Non-empty Counts per Column")

        cols = report["columns"]
        missing = report["missing"]
        non_empty = report["non_empty"]

        counts_df = pd.DataFrame({
            "Column": cols,
            "Missing": [missing[c] for c in cols],
            "Non-empty": [non_empty[c] for c in cols],
        })

        st.dataframe(counts_df, use_container_width=True)

    # ===== Tab 2: Markdown =====
    with tab2:
        st.subheader("Markdown Report")

        # create temp markdown file
        with tempfile.TemporaryDirectory() as tmpdir:
            md_path = Path(tmpdir) / "report.md"
            write_markdown(report, md_path)

            markdown_text = md_path.read_text(encoding="utf-8")

        st.markdown(markdown_text)

    # ===== Tab 3: Raw JSON =====
    with tab3:
        st.json(report)
